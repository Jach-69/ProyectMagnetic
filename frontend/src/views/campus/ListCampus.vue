<template>
  <div>
    <h2>Lista de Campus</h2>
    <TableComponent
      :headers="headers"
      :items="campusList"
      @edit="editarCampus"
      @delete="eliminarCampus"
    />
  </div>
</template>

<script>
import axios from '@/plugins/axios';
import TableComponent from '@/components/TableComponent.vue';

export default {
  components: {
    TableComponent
  },
  data() {
    return {
      headers: ['ID', 'Nombre del Campus'],
      campusList: []
    };
  },
  mounted() {
    this.obtenerCampus();
  },
  methods: {
    async obtenerCampus() {
      try {
        const response = await axios.get('/campus');
        this.campusList = response.data;
      } catch (error) {
        console.error('Error al obtener la lista de campus:', error);
      }
    },
    editarCampus(campus) {
      this.$router.push(`/dashboard/campus/edit/${campus.id}`);
    },
    async eliminarCampus(id) {
      if (confirm('¿Estás seguro de que deseas eliminar este campus?')) {
        try {
          await axios.delete(`/campus/${id}`);
          this.obtenerCampus(); // Actualiza la lista después de la eliminación
        } catch (error) {
          console.error('Error al eliminar campus:', error);
        }
      }
    }
  }
};
</script>