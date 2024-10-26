<template>
  <div class="form-container">
    <h1>Crear Permiso</h1>

    <form @submit.prevent="submitForm" class="modal-content">
      <div class="form-group">
        <h2>Persona</h2>
        <select v-model="formData.persona_id" required>
          <option value="" disabled>Seleccione una persona</option>
          <option v-for="persona in personas" :key="persona.id" :value="persona.id">
            {{ persona.nombre }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <button type="button" @click="openSelectModal">Seleccionar Aula</button>
        <span v-if="selectedAula">
          {{ selectedAula.nombre_aula }} - Bloque {{ getBloqueName(selectedAula.bloque_id).nombre_bloque }} - Campus {{ getCampusName(getBloqueName(selectedAula.bloque_id).campus_id) }}
        </span>
      </div>

      <div class="form-group">
        <h6>¿Llave Maestra?</h6>
        <input type="checkbox" v-model="formData.es_universal" />
      </div>

      <button type="submit" class="submit-button">Confirmar</button>
    </form>


    <BaseModal 
      :isOpen="modalOpen" 
      title="Seleccionar Aula" 
      @close="closeModal" 
      :customStyle="{ maxWidth: '800px', maxHeight: '600px', overflowY: 'auto' }">
      <div class="modal-content">
        <table class="table">
          <thead>
            <tr>
              <th>Aula</th>
              <th>Bloque</th>
              <th>Campus</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="aula in aulas" :key="aula.id">
              <td>{{ aula.nombre_aula }}</td>
              <td>{{ getBloqueName(aula.bloque_id).nombre_bloque }}</td>
              <td>{{ getCampusName(getBloqueName(aula.bloque_id).campus_id) }}</td>
              <td>
                <button @click="selectAula(aula)">Seleccionar</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </BaseModal>




    
  </div>
</template>

<script>
import axios from '@/plugins/axios';
import BaseModal from '@/components/BaseModal.vue';

export default {
  components: { BaseModal },
  data() {
    return {
      formData: {
        persona_id: '',
        aula_id: '',
        es_universal: false,
      },
      personas: [],
      aulas: [],
      bloques: [], // Inicializar como array
      campuses: [], // Inicializar como array
      modalOpen: false,
      selectedAula: null,
    };
  },
  created() {
    this.loadPersonas();
    this.loadAulas();
    this.loadBloques(); // Asegúrate de cargar bloques
    this.loadCampuses(); // Asegúrate de cargar campus
  },
  methods: {
    async loadPersonas() {
      const response = await axios.get('/personas/');
      this.personas = response.data;
    },
    async loadAulas() {
      const response = await axios.get('/aulas');
      this.aulas = response.data;
    },
    async loadBloques() {
      const response = await axios.get('/bloques');
      this.bloques = response.data; // Asegúrate de que esto devuelva una lista de bloques
    },
    async loadCampuses() {
      const response = await axios.get('/campus');
      this.campuses = response.data; // Asegúrate de que esto devuelva una lista de campus
    },
    openSelectModal() {
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
    },
    selectAula(aula) {
      this.selectedAula = aula;
      this.formData.aula_id = aula.id;
      this.closeModal();
    },
    async submitForm() {
      try {
        await axios.post('/permisos', this.formData);
        alert('Permiso creado exitosamente!');
        this.resetForm();
      } catch (error) {
        console.error('Error al crear permiso:', error);
        alert('Hubo un error al crear el permiso.');
      }
    },
    resetForm() {
      this.formData = {
        persona_id: '',
        aula_id: '',
        es_universal: false,
      };
      this.selectedAula = null;
    },
    getBloqueName(bloqueId) {
      const bloque = this.bloques.find(b => b.id === bloqueId);
      return bloque ? bloque : { nombre_bloque: 'No definido', campus_id: null };
    },
    getCampusName(campusId) {
      const campus = this.campuses.find(c => c.id === campusId);
      return campus ? campus.nombre_campus : 'No definido';
    },
  },
};
</script>

<style scoped>
.form-container {
  padding: 20px;
  background-color: #333;
  border-radius: 10px;
  color: white;
  max-width: 400px;
  margin: 0 auto;
}

.modal-content {
  display: flex;
  flex-direction: column;
  background-color: #333;
  padding: 20px;
  border-radius: 10px;
}

.form-group {
  margin-bottom: 15px;
}

select {
  padding: 8px;
  border-radius: 5px;
  background-color: #555;
  color: white;
  border: 1px solid #888;
}

button.submit-button {
  margin-top: 15px;
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.table {
  width: 100%;
  margin-top: 20px;
  color: white;
}

.table th,
.table td {
  padding: 10px;
  text-align: left;
}

.table th {
  background-color: #444;
}

.selected-info {
  margin-top: 20px;
  padding: 10px;
  background-color: #444;
  border-radius: 5px;
}
</style>
