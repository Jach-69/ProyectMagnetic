<template>
  <div class="form-container">
    <h2>Crear Usuario</h2>
    <FormComponent 
      :fields="fields" 
      :formData="form" 
      buttonText="Crear Usuario" 
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
        persona_id: null, // Agregar persona_id
        rol_id: null      // Agregar rol_id
      },
      fields: [
        { name: 'persona_id', label: 'ID de Persona', type: 'number' },
        { name: 'rol_id', label: 'ID de Rol', type: 'number' }
      ]
    };
  },
  methods: {
    async submitForm(data) {
      try {
        const response = await axios.post('/usuarios', data);

        // Verifica si la respuesta es exitosa
        if (response.status === 201) {
          this.$router.push('/dashboard/usuarios/list');
        } else {
          alert('Error al crear el usuario. Intenta de nuevo.');
        }
      } catch (error) {
        console.error('Error creando usuario', error);
        alert('Error al crear el usuario. Intenta de nuevo.');
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
