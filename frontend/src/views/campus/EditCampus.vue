<template>
  <div class="form-container">
    <h2>Editar Campus</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Actualizar Campus" 
      @submit="actualizarCampus" 
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
        nombre_campus: ''
      },
      fields: [
        { name: 'nombre_campus', label: 'Nombre del Campus', type: 'text' }
      ]
    };
  },
  props: ['id'],
  mounted() {
    this.obtenerCampus();
  },
  methods: {
    async obtenerCampus() {
      try {
        const response = await axios.get(`/campus/${this.id}`);
        this.form = response.data;
      } catch (error) {
        console.error('Error al obtener campus', error);
      }
    },
    async actualizarCampus(data) {
      try {
        await axios.put(`/campus/${this.id}`, data);
        this.$router.push('/dashboard/campus/list');
      } catch (error) {
        console.error('Error al actualizar campus', error);
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
