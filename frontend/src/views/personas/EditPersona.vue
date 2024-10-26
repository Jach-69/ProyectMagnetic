<template>
  <div class="form-container">
    <h2>Editar Persona</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Actualizar Persona" 
      @submit="updatePersona" 
    />
  </div>
</template>

<script>
import axios from '@/plugins/axios';
import FormComponent from '@/components/FormComponent.vue';

export default {
  components: {
    FormComponent
  },
  data() {
    return {
      form: {
        nombre: '',
        email: '',
        tarjeta_rfid: '',
        clave: '',
        nombre_usuario: '',
        password: ''
      },
      fields: [
        { name: 'nombre', label: 'Nombre', type: 'text' },
        { name: 'email', label: 'Email', type: 'email' },
        { name: 'tarjeta_rfid', label: 'Tarjeta RFID', type: 'text' },
        { name: 'clave', label: 'Clave', type: 'password' },
        { name: 'nombre_usuario', label: 'Nombre de Usuario', type: 'text' },
        { name: 'password', label: 'Contraseña', type: 'password' }
      ]
    };
  },
  props: ['id'],
  mounted() {
    this.getPersona();
  },
  methods: {
    async getPersona() {
      try {
        const response = await axios.get(`/personas/${this.id}`);
        this.form = response.data;
      } catch (error) {
        console.error('Error al obtener persona', error);
      }
    },
    async updatePersona(data) {
      try {
        await axios.put(`/personas/${this.id}`, data);
        this.$router.push('/dashboard/personas/list');
      } catch (error) {
        console.error('Error actualizando persona', error);
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
}
</style>
