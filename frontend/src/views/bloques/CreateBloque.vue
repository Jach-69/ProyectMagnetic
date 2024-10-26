<template>
  <div class="form-container">
    <h2>Crear Bloque</h2>
    <FormComponent
      :fields="fields"
      :formData="form"
      buttonText="Crear Bloque"
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
        nombre_bloque: '',
        campus_id: '' // Agregar campus_id aquí
      },
      fields: [
        { name: 'nombre_bloque', label: 'Nombre del Bloque', type: 'text' },
        { name: 'campus_id', label: 'ID del Campus', type: 'number' } // Agregar campo para campus_id
      ]
    };
  },
  methods: {
    async submitForm(formData) {
      try {
        await axios.post('/bloques', formData);
        this.$router.push('/dashboard/bloques/list');
      } catch (error) {
        console.error('Error creando bloque:', error);
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
