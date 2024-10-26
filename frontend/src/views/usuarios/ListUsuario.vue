<template>
  <div>
    <h2>Lista de Usuarios</h2>
    <TableComponent 
      :headers="headers" 
      :items="usuarios" 
      @edit="editUsuario" 
      @delete="deleteUsuario" 
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
      usuarios: [],
      headers: ['ID', 'ID de Persona', 'ID de Rol']
    };
  },
  mounted() {
    this.getUsuarios();
  },
  methods: {
    async getUsuarios() {
      try {
        const response = await axios.get('/usuarios');
        this.usuarios = response.data;
      } catch (error) {
        console.error('Error al obtener lista de usuarios', error);
      }
    },
    editUsuario(item) {
      this.$router.push(`/dashboard/usuarios/edit/${item.id}`);
    },
    async deleteUsuario(id) {
      if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
        try {
          await axios.delete(`/usuarios/${id}`);
          this.getUsuarios(); // Actualizar la lista después de la eliminación
        } catch (error) {
          console.error('Error al eliminar usuario', error);
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
