<template>
  <div class="container">
    <h1>Lista de Permisos</h1>
    <table class="table table-dark">
      <thead>
        <tr>
          <th>Nombre de Persona</th>
          <th>Aula</th>
          <th>Acceso Total</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="permiso in permisos" :key="permiso.id">
          <td>{{ getPersonaName(permiso.persona_id) }}</td>
          <td>{{ getAulaName(permiso.aula_id) }}</td>
          <td>{{ permiso.es_universal ? 'Sí' : 'No' }}</td>
          <td>
            <button class="btn btn-warning" @click="openEditModal(permiso)">Editar</button>
            <button class="btn btn-danger" @click="confirmDelete(permiso)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal para editar -->
    <BaseModal :isOpen="showEditModal" title="Editar Permiso" @close="closeEditModal">
      <div class="modal-content edit-modal">
        <form @submit.prevent="submitEdit">
          <div class="form-group">
            <label>Nombre de Persona</label>
            <select v-model="editingPermiso.persona_id" required>
              <option value="" disabled>Seleccione una persona</option>
              <option v-for="persona in personas" :key="persona.id" :value="persona.id">
                {{ persona.nombre }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label>Aula</label>
            <select v-model="editingPermiso.aula_id" required>
              <option value="" disabled>Seleccione un aula</option>
              <option v-for="aula in aulas" :key="aula.id" :value="aula.id">
                {{ aula.nombre_aula }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label>Acceso Total</label>
            <input type="checkbox" v-model="editingPermiso.es_universal" />
          </div>

          <button type="submit" class="btn btn-success">Guardar Cambios</button>
        </form>
      </div>
    </BaseModal>

    <!-- Modal de Confirmación para Eliminar -->
    <BaseModal :isOpen="showDeleteConfirmModal" title="Confirmación" @close="closeDeleteConfirmModal">
      <div class="modal-content delete-modal">
        <p>¿Está seguro de que desea eliminar este permiso?</p>
        <div class="button-group">
          <button class="btn btn-danger" @click="executeDelete">Sí, eliminar</button>
          <button class="btn btn-secondary" @click="closeDeleteConfirmModal">Cancelar</button>
        </div>
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
      permisos: [],
      personas: [],
      aulas: [],
      showEditModal: false,
      showDeleteConfirmModal: false,
      editingPermiso: null,
      permisoIdToDelete: null,
    };
  },
  created() {
    this.fetchPermisos();
    this.fetchPersonas();
    this.fetchAulas();
  },
  methods: {
    async fetchPermisos() {
      const response = await axios.get('/permisos');
      this.permisos = response.data;
    },
    async fetchPersonas() {
      const response = await axios.get('/personas/');
      this.personas = response.data;
    },
    async fetchAulas() {
      const response = await axios.get('/aulas');
      this.aulas = response.data;
    },
    getPersonaName(personaId) {
      const persona = this.personas.find(p => p.id === personaId);
      return persona ? persona.nombre : 'No definido';
    },
    getAulaName(aulaId) {
      const aula = this.aulas.find(a => a.id === aulaId);
      return aula ? aula.nombre_aula : 'No definido';
    },
    openEditModal(permiso) {
      this.editingPermiso = { ...permiso };
      this.showEditModal = true;
    },
    closeEditModal() {
      this.showEditModal = false;
      this.editingPermiso = null;
    },
    async submitEdit() {
      await axios.put(`/permisos/${this.editingPermiso.id}`, this.editingPermiso);
      this.fetchPermisos();
      this.closeEditModal();
    },
    confirmDelete(permiso) {
      this.permisoIdToDelete = permiso.id;
      this.showDeleteConfirmModal = true;
    },
    closeDeleteConfirmModal() {
      this.showDeleteConfirmModal = false;
      this.permisoIdToDelete = null;
    },
    async executeDelete() {
      await axios.delete(`/permisos/${this.permisoIdToDelete}`);
      this.fetchPermisos();
      this.closeDeleteConfirmModal();
    },
  },
};
</script>

<style scoped>
.container {
  padding: 20px;
  background-color: #333;
  color: white;
  border-radius: 10px;
}

.table {
  width: 100%;
  margin-top: 20px;
}

.modal-content {
  background: #444;
  color: white;
  padding: 20px;
  border-radius: 10px;
}

.edit-modal .modal-content,
.delete-modal .modal-content {
  background: #444;
  color: white;
  padding: 20px;
  border-radius: 10px;
}

.form-group {
  margin-bottom: 15px;
  background-color: #555; /* Fondo para el grupo del formulario */
  padding: 15px; /* Padding para el grupo */
  border-radius: 5px; /* Esquinas redondeadas */
}

label {
  display: block;
  margin-bottom: 5px;
  color: white;
}

select {
  padding: 10px;
  border-radius: 5px;
  background-color: #666; /* Fondo para el select */
  color: white;
  border: 1px solid #888;
  width: 100%;
}

.button-group {
  display: flex;
  justify-content: space-between;
}
</style>
