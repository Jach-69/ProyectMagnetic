<template>
  <div class="form-container">
    <h2>Crear Campus</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Crear Campus" 
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
        nombre_campus: ''
      },
      fields: [
        { name: 'nombre_campus', label: 'Nombre del Campus', type: 'text' }
      ]
    };
  },
  methods: {
    async submitForm(data) { // Mantén el mismo nombre que llamas en el template
      try {
        const response = await axios.post('/campus', data);
        if (response.status === 201) {
          this.$router.push('/dashboard/campus/list');
        } else {
          alert('Error al crear el campus. Intenta de nuevo.');
        }
      } catch (error) {
        console.error('Error creando campus', error);
        alert('Error al crear el campus. Intenta de nuevo.');
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
