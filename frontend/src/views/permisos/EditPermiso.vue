<template>
  <div class="form-container">
    <h2>Editar Permiso de Acceso</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Actualizar Permiso" 
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
        usuario_id: null,
        aula_id: null
      },
      fields: [
        { name: 'usuario_id', label: 'ID de Usuario', type: 'number' },
        { name: 'aula_id', label: 'ID de Aula', type: 'number' }
      ]
    };
  },
  mounted() {
    this.getPermiso();
  },
  methods: {
    async getPermiso() {
      const id = this.$route.params.id;
      try {
        const response = await axios.get(`/permisos/${id}`);
        this.form = response.data; // Suponiendo que la respuesta tenga el formato adecuado
      } catch (error) {
        console.error('Error al obtener permiso', error);
      }
    },
    async submitForm(data) {
      const id = this.$route.params.id;
      try {
        await axios.put(`/permisos/${id}`, data);
        this.$router.push('/dashboard/permisos/list');
      } catch (error) {
        console.error('Error actualizando permiso', error);
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
