<template>
  <div class="container mt-4">
    <h1>Listar Ambientes</h1>
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'campus' }" @click="setActiveTab('campus')">Campus</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'bloques' }" @click="setActiveTab('bloques')">Bloques</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'aulas' }" @click="setActiveTab('aulas')">Aulas</a>
      </li>
    </ul>

    <div v-if="activeTab === 'campus'">
      <h2>Lista de Campus</h2>
      <ul class="list-group">
        <li class="list-group-item campus-item" v-for="campus in campuses" :key="campus.id">
          {{ campus.nombre_campus }}
          <div class="action-buttons">
            <button class="btn btn-warning btn-sm" @click="openEditModal('campus', campus)">Editar</button>
            <button class="btn btn-danger btn-sm" @click="confirmDelete('campus', campus.nombre_campus, campus.id)">Eliminar</button>
          </div>
        </li>
      </ul>
    </div>

    <div v-if="activeTab === 'bloques'">
      <h2>Lista de Bloques</h2>
      <table class="table table-dark">
        <thead>
          <tr>
            <th>Campus</th>
            <th>Bloques</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="bloque in bloques" :key="bloque.id">
            <td>{{ getCampusName(bloque.campus_id) }}</td>
            <td>{{ bloque.nombre_bloque }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="openEditModal('bloque', bloque)">Editar</button>
              <button class="btn btn-danger btn-sm" @click="confirmDelete('bloque', bloque.nombre_bloque, bloque.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="activeTab === 'aulas'">
      <h2>Lista de Aulas</h2>
      <table class="table table-dark">
        <thead>
          <tr>
            <th>Campus</th>
            <th>Bloque</th>
            <th>Aula</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="aula in aulas" :key="aula.id">
            <td>{{ getCampusName(getBloqueName(aula.bloque_id).campus_id) }}</td>
            <td>{{ getBloqueName(aula.bloque_id).nombre_bloque }}</td>
            <td>{{ aula.nombre_aula }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="openEditModal('aula', aula)">Editar</button>
              <button class="btn btn-danger btn-sm" @click="confirmDelete('aula', aula.nombre_aula, aula.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal para editar -->
    <div v-if="showEditModal" class="modal" @click="closeEditModal">
      <div class="modal-content" @click.stop>
        <h2>Editar {{ editingEntity }}</h2>
        <input v-model="editingData.nombre" placeholder="Nombre" class="modal-input" required />
        <div class="button-group">
          <button class="confirm-button" @click="confirmSaveChanges" :disabled="!editingData.nombre">Confirmar</button>
          <button class="cancel-button" @click="closeEditModal">Cancelar</button>
        </div>
      </div>
    </div>

    <!-- Modal de Confirmación para Editar -->
    <div v-if="showConfirmModal" class="modal" @click="closeConfirmModal">
      <div class="modal-content" @click.stop>
        <h2>Confirmación</h2>
        <p>¿Está seguro de que desea guardar los cambios?</p>
        <div class="button-group">
          <button class="confirm-button" @click="saveChanges">Sí, guardar</button>
          <button class="cancel-button" @click="closeConfirmModal">Cancelar</button>
        </div>
      </div>
    </div>

    <!-- Modal de Confirmación para Eliminar -->
    <div v-if="showDeleteConfirmModal" class="modal" @click="closeDeleteConfirmModal">
      <div class="modal-content" @click.stop>
        <h2>Confirmación</h2>
        <p>{{ confirmMessage }}</p>
        <div class="button-group">
          <button class="confirm-button" @click="executeDelete">Sí, continuar</button>
          <button class="cancel-button" @click="closeDeleteConfirmModal">Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from '@/plugins/axios';

export default {
  data() {
    return {
      activeTab: 'campus',
      campuses: [],
      bloques: [],
      aulas: [],
      showEditModal: false,
      showConfirmModal: false,
      showDeleteConfirmModal: false,
      editingEntity: '',
      editingData: { id: null, nombre: '' },
      confirmMessage: '',
      entityIdToDelete: null,
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
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
        console.error('Error cargando datos', error);
      }
    },
    setActiveTab(tab) {
      this.activeTab = tab;
    },
    getCampusName(campusId) {
      const campus = this.campuses.find(c => c.id === campusId);
      return campus ? campus.nombre_campus : 'No definido';
    },
    getBloqueName(bloqueId) {
      const bloque = this.bloques.find(b => b.id === bloqueId);
      return bloque ? bloque : { nombre_bloque: 'No definido', campus_id: null };
    },
    openEditModal(entity, data) {
      this.editingEntity = entity;
      this.editingData = { id: data.id, nombre: data.nombre || data.nombre_campus || data.nombre_bloque || data.nombre_aula };
      this.showEditModal = true;
    },
    closeEditModal() {
      this.showEditModal = false;
      this.editingData = { id: null, nombre: '' };
    },
    confirmSaveChanges() {
      this.showConfirmModal = true; // Muestra el modal de confirmación
    },
    async saveChanges() {
      try {
        if (this.editingEntity === 'campus') {
          await axios.put(`/campus/${this.editingData.id}`, { nombre_campus: this.editingData.nombre });
        } else if (this.editingEntity === 'bloque') {
          await axios.put(`/bloques/${this.editingData.id}`, { nombre_bloque: this.editingData.nombre });
        } else if (this.editingEntity === 'aula') {
          await axios.put(`/aulas/${this.editingData.id}`, { nombre_aula: this.editingData.nombre });
        }
        this.fetchData();
        this.closeEditModal();
        this.showConfirmModal = false; // Cierra el modal de confirmación
      } catch (error) {
        console.error('Error guardando cambios', error);
      }
    },
    async executeDelete() {
      try {
        if (this.editingEntity === 'campus') {
          await axios.delete(`/campus/${this.entityIdToDelete}`);
        } else if (this.editingEntity === 'bloque') {
          await axios.delete(`/bloques/${this.entityIdToDelete}`);
        } else if (this.editingEntity === 'aula') {
          await axios.delete(`/aulas/${this.entityIdToDelete}`);
        }
        this.fetchData();
        this.closeDeleteConfirmModal();
      } catch (error) {
        console.error('Error eliminando entidad', error);
      }
    },
    confirmDelete(entity, name, id) {
      this.confirmMessage = `¿Seguro que desea eliminar "${name}"?`;
      this.showDeleteConfirmModal = true;
      this.editingEntity = entity;
      this.entityIdToDelete = id;
    },
    closeDeleteConfirmModal() {
      this.showDeleteConfirmModal = false;
    },
    closeConfirmModal() {
      this.showConfirmModal = false;
    }
  }
};
</script>



<style scoped>
.container {
  max-width: 800px;
  background-color: #1e1e1e;
  color: white;
  padding: 20px;
  border-radius: 8px;
}
.list-group-item {
  max-width: 350px;
}
.table {
  margin-top: 20px;
}
.action-buttons {
  float: right;
}
.list-group {
  display: flex;
  justify-content: center;
  list-style-type: none;
  padding: 0;
}
.list-group-item.campus-item {
  margin: 10px;
  background-color: #2e2e2e;
  color: white;
  text-align: center;
  margin-bottom: 10px;
}
.nav-link {
  color: #ffffff;
  font-weight: normal;
  background-color: #5e5e5e;
  border: 2px solid #ffffff;
  border-radius: 5px;
  padding: 10px;
}
.nav-link.active {
  background-color: #477572;
  color: white;
  border: 2px solid #ffffff;
}
.modal {
  display: block;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.5);
}
.modal-content {
  background-color: #1e1e1e;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 40%;
}
.modal-input {
  width: 100%;
  max-width: 300px;
  margin: 10px auto;
}
.confirm-button {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  width: 120px;
  margin: 10px;
}
.cancel-button {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  width: 120px;
  margin: 10px;
}
.button-group {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
</style>
