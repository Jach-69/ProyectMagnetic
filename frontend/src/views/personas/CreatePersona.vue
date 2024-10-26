<template>
  <div class="form-container">
    <h1>Crear Usuario</h1>

    <div class="options">
      <div class="option">
        <h2>Personas</h2>
        <div class="select-container">
          <select v-model="selectedPersona">
            <option value="" disabled>Seleccione una persona</option>
            <option v-for="persona in personas" :key="persona.id" :value="persona.id">
              {{ persona.nombre }}
            </option>
          </select>
          <button class="create-button" @click="openModal('crearPersona')">Crear Persona</button>
        </div>
      </div>

      <div class="option">
        <h2>Roles</h2>
        <div class="select-container">
          <select v-model="selectedRol">
            <option value="" disabled>Seleccione un rol</option>
            <option v-for="rol in roles" :key="rol.id" :value="rol.id">
              {{ rol.nombre_rol }}
            </option>
          </select>
          <button class="create-button" @click="openModal('crearRol')">Crear Rol</button>
        </div>
      </div>

      <button class="create-button" @click="createUsuario" :disabled="!selectedPersona || !selectedRol">Crear Usuario</button>
    </div>

    <BaseModal :isOpen="modalOpen" :title="modalTitle" @close="closeModal">
      <form @submit.prevent="submitForm" class="modal-content">
        <div v-if="currentOption === 'crearPersona'">
          <div class="form-group">
            <label class="form-label">Nombre:</label>
            <input class="form-input" v-model="formData.nombre" required />
          </div>
          <div class="form-group">
            <label class="form-label">Email:</label>
            <input class="form-input" v-model="formData.email" required />
          </div>
          <div class="form-group">
            <label class="form-label">Tarjeta RFID:</label>
            <input class="form-input" v-model="formData.tarjeta_rfid" required />
          </div>
          <div class="form-group">
            <label class="form-label">Clave:</label>
            <input class="form-input" v-model="formData.clave" required />
          </div>
          <div class="form-group">
            <label class="form-label">Nombre de Usuario:</label>
            <input class="form-input" v-model="formData.nombre_usuario" required />
          </div>
          <div class="form-group">
            <label class="form-label">Contraseña:</label>
            <input class="form-input" type="password" v-model="formData.password" required />
          </div>
        </div>
        
        <div v-if="currentOption === 'crearRol'">
          <div class="form-group">
            <label class="form-label">Nombre del Rol:</label>
            <input class="form-input" v-model="formData.rolNombre" required />
          </div>
        </div>
        
        <button type="submit" class="submit-button">Confirmar</button>
      </form>
    </BaseModal>

    <BaseModal :isOpen="alertOpen" title="Éxito" @close="alertOpen = false">
      <p class="alert-message">{{ alertMessage }}</p>
      <button class="close-button" @click="alertOpen = false">Cerrar</button>
    </BaseModal>
  </div>
</template>

<script>
import axios from '@/plugins/axios';
import BaseModal from '@/components/BaseModal.vue';

export default {
  components: {
    BaseModal
  },
  data() {
    return {
      modalOpen: false,
      alertOpen: false,
      alertMessage: '',
      currentOption: '',
      formData: {
        nombre: '',
        email: '',
        tarjeta_rfid: '',
        clave: '',
        nombre_usuario: '',
        password: '',
        // rolNombre: '' // Eliminar esto
      },
      personas: [],
      roles: [],
      selectedPersona: null,
      selectedRol: null,
    };
  },
  created() {
    this.loadData();
  },
  methods: {
    async loadData() {
      try {
        const [personasResponse, rolesResponse] = await Promise.all([
          axios.get('/personas/'),
          axios.get('/roles')
        ]);
        this.personas = personasResponse.data;
        this.roles = rolesResponse.data;
      } catch (error) {
        console.error('Error al cargar personas o roles:', error);
      }
    },
    createUsuario() {
      const token = localStorage.getItem('token');
      if (!token) {
        alert('No estás autenticado. Por favor, inicia sesión.');
        return;
      }

      const usuarioData = {
        persona_id: this.selectedPersona,
        rol_id: this.selectedRol,
      };

      axios.post('/usuarios/', usuarioData, {
        headers: { Authorization: `Bearer ${token}` }
      })
      .then(() => {
        this.alertMessage = 'Usuario creado exitosamente!';
        this.alertOpen = true;
        this.selectedPersona = null; // Reiniciar selección
        this.selectedRol = null; // Reiniciar selección
      })
      .catch(error => {
        console.error('Error al crear usuario:', error);
        this.alertMessage = 'Hubo un error al crear el usuario. Por favor, intenta nuevamente.';
        this.alertOpen = true;
      });
    },

    openModal(option) {
      this.currentOption = option;
      this.modalOpen = true;
    },
    closeModal() {
      this.modalOpen = false;
      this.resetForm();
    },
    resetForm() {
      this.formData = {
        nombre: '',
        email: '',
        tarjeta_rfid: '',
        clave: '',
        nombre_usuario: '',
        password: ''
      };
    },
    async submitForm() {
      const token = localStorage.getItem('token');

      if (!token) {
        alert('No estás autenticado. Por favor, inicia sesión.');
        return;
      }

      try {
        if (this.currentOption === 'crearPersona') {
          const response = await axios.post('/personas/', this.formData, {
            headers: { Authorization: `Bearer ${token}` }
          });
          this.personas.push(response.data);
          this.alertMessage = 'Persona creada exitosamente!';
        } else if (this.currentOption === 'crearRol') {
          const response = await axios.post('/roles', { nombre_rol: this.formData.rolNombre }, {
            headers: { Authorization: `Bearer ${token}` }
          });
          this.roles.push(response.data);
          this.alertMessage = 'Rol creado exitosamente!';
        }
        this.loadData(); // Refresca la lista después de crear
        this.closeModal();
        this.alertOpen = true;
      } catch (error) {
        console.error('Error al crear:', error);
        this.alertMessage = 'Hubo un error al crear. Por favor, intenta nuevamente.';
        this.alertOpen = true;
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
  max-width: 400px; /* Aumenta el ancho del contenedor principal */
  margin: 0 auto;
}

.options {
  display: flex;
  flex-direction: column;
  gap: 15px;
  align-items: center;
}

.option {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  background-color: #444; /* Fondo oscuro */
  
}

.select-container {
  display: flex;
  align-items: center;
}

select {
  width: 200px;
  padding: 8px;
  border-radius: 5px;
  background-color: #555; /* Fondo oscuro */
  color: white; /* Texto blanco */
  border: 1px solid #888;
}

button.create-button {
  background-color: #4CAF50;
  color: white;
  padding: 5px;
  border: none;
  cursor: pointer;
  margin-left: 10px;
  border-radius: 5px;
  align-items: center;
  max-width: 200px;
  
}

button.create-button:disabled {
  background-color: #ccc; /* Un color gris para el botón deshabilitado */
  cursor: not-allowed; /* Cambiar el cursor para indicar que no se puede hacer clic */
}

button.create-button:hover {
  background-color: #45a049;
}

button[type="submit"] {
  margin-top: 15px;
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px; /* Aumenta el padding del botón */
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #45a049;
}

.modal-content {
  display: flex;
  flex-direction: column;
  background-color: #333; /* Fondo oscuro para el modal */
  padding: 20px;
  border-radius: 10px;
  max-width: 800px; /* Aumenta el ancho del modal */
  margin: auto; /* Centra el modal */
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  background-color: #444; /* Fondo oscuro para el grupo */
  padding: 10px; /* Espacio interno */
  border-radius: 5px; /* Bordes redondeados */
}

.form-label {
  margin-right: 10px;
  flex: 1; /* Asegura que el label ocupe el espacio necesario */
  color: white; /* Texto blanco */
}

.form-input {
  flex: 2; /* Asegura que el input ocupe el espacio restante */
  padding: 10px; /* Aumenta el padding */
  border: 1px solid #888;
  background-color: #555; /* Fondo oscuro */
  color: white; /* Texto blanco */
  width: 100%; /* Asegura que los inputs no se salgan */
}

.alert-message {
  text-align: center;
  color: #4CAF50; /* Verde para el mensaje de éxito */
  margin: 10px 0; /* Espaciado alrededor del mensaje */
}

.close-button {
  background-color: red; /* Color rojo para el botón */
  color: white; /* Texto blanco */
  padding: 5px 10px; /* Espaciado del botón */
  border: none; /* Sin borde */
  border-radius: 5px; /* Bordes redondeados */
  cursor: pointer; /* Cambia el cursor al pasar */
  display: block; /* Asegura que el botón esté en una nueva línea */
  margin: 0 auto; /* Centra el botón */
}

.close-button:hover {
  background-color: darkred; /* Color más oscuro al pasar el ratón */
}

</style>
