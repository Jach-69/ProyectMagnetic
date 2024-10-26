<template>
  <div>
    <h2>Lista de Roles</h2>
    <TableComponent 
      :headers="headers" 
      :items="roles" 
      @edit="editRol" 
      @delete="deleteRol" 
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
      roles: [],
      headers: ['ID', 'Nombre del Rol']
    };
  },
  mounted() {
    this.getRoles();
  },
  methods: {
    async getRoles() {
      try {
        const response = await axios.get('/roles');
        this.roles = response.data;
      } catch (error) {
        console.error('Error al obtener lista de roles', error);
      }
    },
    editRol(item) {
      this.$router.push(`/dashboard/edit-rol/${item.id}`);
    },
    async deleteRol(id) {
      if (confirm('¿Estás seguro de que deseas eliminar este rol?')) {
        try {
          await axios.delete(`/roles/${id}`);
          this.getRoles(); // Actualizar la lista después de la eliminación
        } catch (error) {
          console.error('Error al eliminar rol', error);
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
