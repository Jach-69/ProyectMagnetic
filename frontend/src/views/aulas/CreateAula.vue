<template>
  <div class="form-container">
    <h2>Crear Aula</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Crear Aula" 
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
        nombre_aula: '',
        bloque_id: null // Agregar bloque_id
      },
      fields: [
        { name: 'nombre_aula', label: 'Nombre del Aula', type: 'text' },
        { name: 'bloque_id', label: 'ID del Bloque', type: 'number' } // Campo para bloque_id
      ]
    };
  },
  methods: {
    submitForm(data) {
      axios.post('/aulas', data)
        .then(() => {
          this.$router.push('/dashboard/aulas/list');
        })
        .catch(error => {
          console.error('Error creando aula', error);
        });
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
