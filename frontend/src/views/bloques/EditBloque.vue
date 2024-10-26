<template>
  <div class="form-container">
    <h2>Editar Bloque</h2>
    <FormComponent
      :fields="fields"
      :formData="form"
      buttonText="Actualizar Bloque"
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
        nombre_bloque: ''
      },
      fields: [
        { name: 'nombre_bloque', label: 'Nombre del Bloque', type: 'text' }
      ]
    };
  },
  props: ['id'],
  mounted() {
    this.obtenerBloque();
  },
  methods: {
    async obtenerBloque() {
      try {
        const response = await axios.get(`/bloques/${this.id}`);
        this.form = response.data;
      } catch (error) {
        console.error('Error al obtener bloque:', error);
      }
    },
    async submitForm(formData) {
      try {
        await axios.put(`/bloques/${this.id}`, formData);
        this.$router.push('/dashboard/bloques/list');
      } catch (error) {
        console.error('Error actualizando bloque:', error);
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
