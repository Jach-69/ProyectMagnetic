<template>
  <div>
    <h2>Lista de Aulas</h2>
    <TableComponent 
      :headers="headers" 
      :items="aulas" 
      @edit="editAula" 
      @delete="deleteAula" 
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
      aulas: [],
      headers: ['ID', 'Nombre del Aula', 'ID del Bloque']
    };
  },
  mounted() {
    this.getAulas();
  },
  methods: {
    async getAulas() {
      try {
        const response = await axios.get('/aulas');
        this.aulas = response.data;
      } catch (error) {
        console.error('Error al obtener lista de aulas', error);
      }
    },
    editAula(item) {
      this.$router.push(`/dashboard/edit-aula/${item.id}`);
    },
    async deleteAula(id) {
      if (confirm('¿Estás seguro de que deseas eliminar esta aula?')) {
        try {
          await axios.delete(`/aulas/${id}`);
          this.getAulas(); // Actualizar la lista después de la eliminación
        } catch (error) {
          console.error('Error al eliminar aula', error);
        }
      }
    }
  }
};
</script>

<style scoped>
.table-container {
  padding: 20px;
  background-color: #333;
  border-radius: 10px;
  color: white;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 10px;
  border: 1px solid #444;
}

button {
  margin-right: 10px;
}
</style>
