<template>
  <div class="form-container">
    <h2>Editar Rol</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Actualizar Rol" 
      @submit="updateRol" 
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
        nombre_rol: ''
      },
      fields: [
        { name: 'nombre_rol', label: 'Nombre del Rol', type: 'text' }
      ]
    };
  },
  props: ['id'],
  mounted() {
    this.getRol();
  },
  methods: {
    async getRol() {
      try {
        const response = await axios.get(`/roles/${this.id}`);
        this.form = response.data;
      } catch (error) {
        console.error('Error al obtener rol', error);
      }
    },
    async updateRol(data) {
      try {
        await axios.put(`/roles/${this.id}`, data);
        this.$router.push('/dashboard/list-roles');
      } catch (error) {
        console.error('Error actualizando rol', error);
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
