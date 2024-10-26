<template>
  <div class="form-container">
    <h2>Editar Usuario</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Actualizar Usuario" 
      @submit="submitForm" 
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
        persona_id: null,
        rol_id: null
      },
      fields: [
        { name: 'persona_id', label: 'ID de Persona', type: 'number' },
        { name: 'rol_id', label: 'ID de Rol', type: 'number' }
      ]
    };
  },
  mounted() {
    this.getUsuario();
  },
  methods: {
    async getUsuario() {
      const id = this.$route.params.id;
      try {
        const response = await axios.get(`/usuarios/${id}`);
        this.form = response.data; // Suponiendo que la respuesta tenga el formato adecuado
      } catch (error) {
        console.error('Error al obtener usuario', error);
      }
    },
    async submitForm(data) {
      const id = this.$route.params.id;
      try {
        await axios.put(`/usuarios/${id}`, data);
        this.$router.push('/dashboard/usuarios/list');
      } catch (error) {
        console.error('Error actualizando usuario', error);
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
