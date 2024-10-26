<template>
  <div class="container">
    <h1>Historial de Accesos</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Persona ID</th>
          <th>Aula ID</th>
          <th>Fecha y Hora</th>
          <th>Es Válido</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in historial" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.persona_id }}</td>
          <td>{{ item.aula_id }}</td>
          <td>{{ item.fecha_hora }}</td>
          <td>{{ item.es_valido ? 'Sí' : 'No' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from '@/plugins/axios';

export default {
  data() {
    return {
      historial: []
    };
  },
  mounted() {
    this.fetchHistorial();
  },
  methods: {
    async fetchHistorial() {
      try {
        const response = await axios.get('/historial'); // Usa la ruta relativa
        this.historial = response.data;
      } catch (error) {
        console.error('Error fetching historial:', error);
      }
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 800px;
  background-color: #1e1e1e;
  color: white;
  padding: 20px;
  border-radius: 8px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  padding: 12px;
  text-align: left;
}

th {
  background-color: #2c2c2c; /* Fondo más oscuro para encabezados */
  border-bottom: 2px solid #444; /* Línea separadora */
}

tr:nth-child(even) {
  background-color: #2a2a2a; /* Color de fila alternativo */
}

tr:hover {
  background-color: #3a3a3a; /* Color al pasar el mouse */
}

tr td {
  border-bottom: 1px solid #444; /* Línea separadora entre filas */
}
</style>

