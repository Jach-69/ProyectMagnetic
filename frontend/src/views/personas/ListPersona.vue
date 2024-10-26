<template>
  <div class="container mt-4">
    <h1>Gestión de Entidades</h1>
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'personas' }" @click="setActiveTab('personas')">Personas</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'roles' }" @click="setActiveTab('roles')">Roles</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'usuarios' }" @click="setActiveTab('usuarios')">Usuarios</a>
      </li>
    </ul>

    <!-- Pestaña Personas -->
    <div v-if="activeTab === 'personas'">
      <h2>Lista de Personas</h2>
      <table class="table table-dark">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Email</th>
            <th>Tarjeta RFID</th>
            <th>Nombre de Usuario</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="persona in personas" :key="persona.id">
            <td>{{ persona.nombre }}</td>
            <td>{{ persona.email }}</td>
            <td>{{ persona.tarjeta_rfid }}</td>
            <td>{{ persona.nombre_usuario }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="openEditModal('persona', persona)">Editar</button>
              <button class="btn btn-danger btn-sm" @click="confirmDelete('persona', persona.nombre, persona.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

      <!-- Pestaña Roles -->
      <div v-if="activeTab === 'roles'">
        <h2>Lista de Roles</h2>
        <table class="table table-dark">
          <thead>
            <tr>
              <th>Nombre del Rol</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="rol in roles" :key="rol.id">
              <td>{{ rol.nombre_rol }}</td> <!-- Cambiado a nombre_rol -->
              <td>
                <button class="btn btn-warning btn-sm" @click="openEditModal('rol', rol)">Editar</button>
                <button class="btn btn-danger btn-sm" @click="confirmDelete('rol', rol.nombre_rol, rol.id)">Eliminar</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>


    <!-- Pestaña Usuarios -->
    <div v-if="activeTab === 'usuarios'">
      <h2>Lista de Usuarios</h2>
      <table class="table table-dark">
        <thead>
          <tr>
            <th>Nombre de Persona</th>
            <th>Nombre de Rol</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="usuario in usuarios" :key="usuario.id">
            <td>{{ getPersonaName(usuario.persona_id) }}</td>
            <td>
              {{ getRolName(usuario.rol_id) }}
              <span v-if="!getRolName(usuario.rol_id)">{{ usuario.rol_id }}</span> <!-- Para ver el ID si no se encuentra -->
            </td>
            <td>
              <button class="btn btn-warning btn-sm" @click="openEditModal('usuario', usuario)">Editar</button>
              <button class="btn btn-danger btn-sm" @click="confirmDelete('usuario', usuario.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>

      </table>
    </div>

    <!-- Modal para editar -->
    <div v-if="showEditModal" class="modal" @click="closeEditModal">
      <div class="modal-content" @click.stop>
        <h2>Editar {{ editingEntity }}</h2>
        <label v-if="editingEntity === 'persona'" for="nombre">Nombre:</label>
        <input v-if="editingEntity === 'persona'" v-model="editingData.nombre" id="nombre" class="modal-input" required />
        
        <label v-if="editingEntity === 'persona'" for="email">Email:</label>
        <input v-if="editingEntity === 'persona'" v-model="editingData.email" id="email" class="modal-input" required />
        
        <label v-if="editingEntity === 'persona'" for="tarjeta_rfid">Tarjeta RFID:</label>
        <input v-if="editingEntity === 'persona'" v-model="editingData.tarjeta_rfid" id="tarjeta_rfid" class="modal-input" required />
        
        <label v-if="editingEntity === 'persona'" for="nombre_usuario">Nombre de Usuario:</label>
        <input v-if="editingEntity === 'persona'" v-model="editingData.nombre_usuario" id="nombre_usuario" class="modal-input" required />
        
        <label v-if="editingEntity === 'persona'" for="clave">Clave:</label>
        <input v-if="editingEntity === 'persona'" v-model="editingData.clave" id="clave" class="modal-input" required />
        
        <label v-if="editingEntity === 'persona'" for="password">Contraseña:</label>
        <input v-if="editingEntity === 'persona'" v-model="editingData.password" id="password" type="password" class="modal-input" required />

        <label v-if="editingEntity === 'rol'" for="nombre_rol">Nombre del Rol:</label>
        <input v-if="editingEntity === 'rol'" v-model="editingData.nombre" id="nombre_rol" class="modal-input" required />
        
        <label v-if="editingEntity === 'usuario'" for="persona_id">Selecciona Persona:</label>
        <select v-if="editingEntity === 'usuario'" v-model="editingData.persona_id" id="persona_id" class="modal-input" required>
          <option v-for="persona in personas" :key="persona.id" :value="persona.id">
            {{ persona.nombre }}
          </option>
        </select>

        <label v-if="editingEntity === 'usuario'" for="rol_id">Selecciona Rol:</label>
        <select v-if="editingEntity === 'usuario'" v-model="editingData.rol_id" id="rol_id" class="modal-input" required>
          <option v-for="rol in roles" :key="rol.id" :value="rol.id">
            {{ rol.nombre_rol }}
          </option>
        </select>

        <div class="button-group">
          <button class="confirm-button" @click="confirmSaveChanges" :disabled="!isFormValid">Confirmar</button>
          <button class="cancel-button" @click="closeEditModal">Cancelar</button>
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
      activeTab: 'personas',
      personas: [],
      roles: [],
      usuarios: [],
      showEditModal: false,
      showDeleteConfirmModal: false,
      editingEntity: '',
      editingData: {
        id: null,
        nombre: '',
        email: '',
        tarjeta_rfid: '',
        nombre_usuario: '',
        clave: '',
        password: '',
        persona_id: '',
        rol_id: ''
      },
      confirmMessage: '',
      entityIdToDelete: null,
    };
  },
  created() {
    this.fetchData();
  },
  computed: {
    isFormValid() {
      if (this.editingEntity === 'persona') {
        return this.editingData.nombre && this.editingData.email && this.editingData.tarjeta_rfid && this.editingData.nombre_usuario && this.editingData.clave && this.editingData.password;
      } else if (this.editingEntity === 'rol') {
        return this.editingData.nombre; // Asegúrate de que se valide nombre
      } else if (this.editingEntity === 'usuario') {
        return this.editingData.persona_id && this.editingData.rol_id;
      }
      return false;
    }

  },
  methods: {
    async fetchData() {
      try {
        const [personasResponse, rolesResponse, usuariosResponse] = await Promise.all([
          axios.get('/personas/'),
          axios.get('/roles'),
          axios.get('/usuarios/')
        ]);
        
        this.personas = personasResponse.data;
        this.roles = rolesResponse.data;
        this.usuarios = usuariosResponse.data;
      } catch (error) {
        console.error('Error cargando datos', error);
      }
    },
    setActiveTab(tab) {
      this.activeTab = tab;
    },
    openEditModal(entity, data) {
      this.editingEntity = entity;
      this.editingData = {
        id: data.id,
        nombre: entity === 'rol' ? data.nombre_rol : data.nombre || '', // Cambiar para que refleje nombre_rol
        email: data.email || '',
        tarjeta_rfid: data.tarjeta_rfid || '',
        nombre_usuario: data.nombre_usuario || '',
        clave: entity === 'persona' ? data.clave : '',
        password: entity === 'persona' ? data.password : '',
        persona_id: entity === 'usuario' ? data.persona_id : '',
        rol_id: entity === 'usuario' ? data.rol_id : ''
      };
      this.showEditModal = true;
    },

    closeEditModal() {
      this.showEditModal = false;
      this.editingData = { id: null, nombre: '', email: '', tarjeta_rfid: '', nombre_usuario: '', clave: '', password: '', persona_id: '', rol_id: '' };
    },
    confirmSaveChanges() {
      this.saveChanges();
    },
    async saveChanges() {
      try {
        if (this.editingEntity === 'persona') {
          await axios.put(`/personas/${this.editingData.id}`, this.editingData);
        } else if (this.editingEntity === 'rol') {
          await axios.put(`/roles/${this.editingData.id}`, {
            nombre_rol: this.editingData.nombre // Asegúrate de usar nombre_rol
          });
        } else if (this.editingEntity === 'usuario') {
          await axios.put(`/usuarios/${this.editingData.id}`, this.editingData);
        }
        this.fetchData();
        this.closeEditModal();
      } catch (error) {
        console.error('Error guardando cambios', error);
      }
    },

    async executeDelete() {
      try {
        if (this.editingEntity === 'persona') {
          await axios.delete(`/personas/${this.entityIdToDelete}`);
        } else if (this.editingEntity === 'rol') {
          await axios.delete(`/roles/${this.entityIdToDelete}`);
        } else if (this.editingEntity === 'usuario') {
          await axios.delete(`/usuarios/${this.entityIdToDelete}`);
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
    getPersonaName(id) {
      const persona = this.personas.find(p => p.id === id);
      return persona ? persona.nombre : 'Desconocido';
    },
    getRolName(id) {
      const rol = this.roles.find(r => r.id === id);
      console.log(`Buscando rol con id: ${id}, encontrado:`, rol);
      return rol ? rol.nombre_rol : 'Rol no encontrado';
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
.table {
  margin-top: 20px;
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
