<template>
  <div>
    <h2>Lista de Bloques</h2>
    <TableComponent
      :headers="headers"
      :items="bloqueList"
      @edit="editarBloque"
      @delete="eliminarBloque"
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
      headers: ['IdCampus','ID', 'Nombre del Bloque'],
      bloqueList: []
    };
  },
  mounted() {
    this.obtenerBloques();
  },
  methods: {
    async obtenerBloques() {
      try {
        const response = await axios.get('/bloques');
        this.bloqueList = response.data;
      } catch (error) {
        console.error('Error al obtener la lista de bloques:', error);
      }
    },
    editarBloque(bloque) {
      this.$router.push(`/dashboard/bloques/edit/${bloque.id}`);
    },
    async eliminarBloque(id) {
      if (confirm('¿Estás seguro de que deseas eliminar este bloque?')) {
        try {
          await axios.delete(`/bloques/${id}`);
          this.obtenerBloques(); // Actualiza la lista después de la eliminación
        } catch (error) {
          console.error('Error al eliminar bloque:', error);
        }
      }
    }
  }
};
</script>

<style scoped>
h2 {
  margin-bottom: 20px;
}
</style>
