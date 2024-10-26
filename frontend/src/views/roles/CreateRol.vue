<template>
  <div class="form-container">
    <h2>Crear Rol</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Crear Rol" 
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
        nombre_rol: ''
      },
      fields: [
        { name: 'nombre_rol', label: 'Nombre del Rol', type: 'text' }
      ]
    };
  },
  methods: {
  async submitForm(data) {
    try {
      const response = await axios.post('/roles', data);
      
      // Verifica si la respuesta es exitosa
      if (response.status === 201) { // 201 es el código de éxito para creación
        this.$router.push('/dashboard/roles/list');
      } else {
        alert('Error al crear el rol. Intenta de nuevo.');
      }
    } catch (error) {
      console.error('Error creando rol', error);
      alert('Error al crear el rol. Intenta de nuevo.');
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
