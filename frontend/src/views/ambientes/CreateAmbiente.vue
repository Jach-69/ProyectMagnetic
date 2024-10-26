<template>
  <div class="form-container">
    <h1>Crear Ambiente</h1>

    <div class="options">
      <!-- Opción de Campus -->
      <div class="option">
        <h2>Campus</h2>
        <div class="select-container">
          <select v-model="selectedCampus" @change="checkCreate('campus')">
            <option v-for="campus in campuses" :key="campus.id" :value="campus.id">
              {{ campus.nombre_campus }}
            </option>
          </select>
          <button @click="openModal('campus')">Crear Campus</button>
        </div>
      </div>

      <!-- Opción de Bloques -->
      <div class="option">
        <h2>Bloques</h2>
        <div class="select-container">
          <select v-model="selectedBloque" @change="checkCreate('bloque')">
            <option v-for="bloque in bloques" :key="bloque.id" :value="bloque.id">
              {{ bloque.nombre_bloque }}
            </option>
          </select>
          <button @click="openModal('bloque')">Crear Bloque</button>
        </div>
      </div>

      <!-- Opción de Aulas -->
      <div class="option">
        <h2>Aulas</h2>
        <div class="select-container">
          <select v-model="selectedAula">
            <option v-for="aula in aulas" :key="aula.id" :value="aula.id">
              {{ aula.nombre_aula }}
            </option>
          </select>
          <button @click="openModal('aula')">Crear Aula</button>
        </div>
      </div>
    </div>

    <!-- Modal para agregar datos -->
    <BaseModal :isOpen="modalOpen" :title="modalTitle" @close="closeModal">
      <form @submit.prevent="submitForm">
        <div v-if="currentOption === 'campus'">
          <label for="campusName">Nombre del Campus:</label>
          <input type="text" v-model="formData.campusName" required />
        </div>
        <div v-if="currentOption === 'bloque'">
          <label for="bloqueName">Nombre del Bloque:</label>
          <input type="text" v-model="formData.bloqueName" required />
        </div>
        <div v-if="currentOption === 'aula'">
          <label for="aulaName">Nombre del Aula:</label>
          <input type="text" v-model="formData.aulaName" required />
        </div>
        <button type="submit">Confirmar</button>
      </form>
    </BaseModal>

    <!-- Modal de Confirmación -->
    <BaseModal :isOpen="confirmModalOpen" title="Confirmación" @close="closeConfirmModal">
      <p>{{ confirmMessage }}</p>
      <div class="confirm-buttons">
        <button class="confirm-button" @click="handleConfirm">Sí, crear</button>
        <button class="cancel-button" @click="closeConfirmModal">Cancelar</button>
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
      modalOpen: false,
      confirmModalOpen: false,
      modalTitle: '',
      confirmMessage: '',
      currentOption: '',
      formData: {
        campusName: '',
        bloqueName: '',
        aulaName: ''
      },
      campuses: [],
      bloques: [],
      aulas: [],
      selectedCampus: null,
      selectedBloque: null,
      selectedAula: null
    };
  },
  created() {
    this.fetchOptions();
  },
  methods: {
    async fetchOptions() {
      try {
        const [campusResponse, bloqueResponse, aulaResponse] = await Promise.all([
          axios.get('/campus'),
          axios.get('/bloques'),
          axios.get('/aulas')
        ]);
        
        this.campuses = campusResponse.data;
        this.bloques = bloqueResponse.data;
        this.aulas = aulaResponse.data;
      } catch (error) {
        console.error('Error cargando opciones', error);
      }
    },
    checkCreate(type) {
      if (this[`selected${type.charAt(0).toUpperCase() + type.slice(1)}`] === 'create') {
        this.openModal(type);
      }
    },
    openModal(option) {
      this.currentOption = option;
      this.modalTitle = `Crear ${option.charAt(0).toUpperCase() + option.slice(1)}`;
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
      this.resetForm();
    },
    resetForm() {
      this.formData = {
        campusName: '',
        bloqueName: '',
        aulaName: ''
      };
    },
    submitForm() {
      if (this.currentOption === 'campus') {
        this.confirmMessage = `Seguro que se creará "${this.formData.campusName}"`;
      } else if (this.currentOption === 'bloque') {
        this.confirmMessage = `Seguro que se creará "${this.formData.bloqueName}" en este campus: "${this.campuses.find(c => c.id === this.selectedCampus).nombre_campus}"`;
      } else if (this.currentOption === 'aula') {
        this.confirmMessage = `Seguro que se creará "${this.formData.aulaName}" en este bloque: "${this.bloques.find(b => b.id === this.selectedBloque).nombre_bloque}"`;
      }

      this.confirmModalOpen = true;
    },
    closeConfirmModal() {
      this.confirmModalOpen = false;
    },
    async handleConfirm() {
      try {
        if (this.currentOption === 'campus') {
          const response = await axios.post('/campus', { nombre_campus: this.formData.campusName });
          this.campuses.push(response.data);
        } else if (this.currentOption === 'bloque') {
          const response = await axios.post('/bloques', { nombre_bloque: this.formData.bloqueName, campus_id: this.selectedCampus });
          this.bloques.push(response.data);
        } else if (this.currentOption === 'aula') {
          const response = await axios.post('/aulas', { nombre_aula: this.formData.aulaName, bloque_id: this.selectedBloque });
          this.aulas.push(response.data);
        }
        this.fetchOptions(); // Actualiza la lista después de crear
        this.closeConfirmModal(); // Cierra el modal de confirmación
        this.closeModal(); // Cierra el modal de entrada
      } catch (error) {
        console.error(`Error creando ${this.currentOption}`, error);
      }
    }
  }
};
</script>

<style scoped>
.form-container {
  padding: 20px;
  background-color: #333;
  border-radius: 10px;
  color: white;
  max-width: 600px;
  margin: 0 auto;
}

.options {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.option {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
}

.select-container {
  display: flex;
  align-items: center;
}

select {
  width: 200px;
  padding: 8px;
  border-radius: 5px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 5px;
  border: none;
  cursor: pointer;
  margin-left: 10px;
  border-radius: 5px;
}

button:hover {
  background-color: #45a049;
}

.confirm-buttons {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.confirm-button {
  background-color: #4CAF50;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
}

.cancel-button {
  background-color: red;
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
}

.confirm-button:hover {
  background-color: #45a049;
}

button[type="submit"] {
  margin-top: 15px; /* Espaciado adicional entre el input y el botón */
}

.cancel-button:hover {
  background-color: darkred;
}
</style>



