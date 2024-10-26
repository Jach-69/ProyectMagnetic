<template>
  <div class="form-container">
    <h2>Editar Aula</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Actualizar Aula" 
      @submit="updateAula" 
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
        nombre_aula: '',
        bloque_id: null
      },
      fields: [
        { name: 'nombre_aula', label: 'Nombre del Aula', type: 'text' },
        { name: 'bloque_id', label: 'ID del Bloque', type: 'number' }
      ]
    };
  },
  props: ['id'],
  mounted() {
    this.getAula();
  },
  methods: {
    async getAula() {
      try {
        const response = await axios.get(`/aulas/${this.id}`);
        this.form = response.data;
      } catch (error) {
        console.error('Error al obtener aula', error);
      }
    },
    async updateAula(data) {
      try {
        await axios.put(`/aulas/${this.id}`, data);
        this.$router.push('/dashboard/list-aulas');
      } catch (error) {
        console.error('Error actualizando aula', error);
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
