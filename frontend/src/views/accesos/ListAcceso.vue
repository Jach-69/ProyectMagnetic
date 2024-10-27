<template>
  <div class="container">
    <h1>Historial de Accesos</h1>
    
    <div class="filters">
      <input
        type="text"
        v-model="filters.personaName"
        placeholder="Buscar por nombre de persona"
      />
      <input
        type="text"
        v-model="filters.aulaName"
        placeholder="Buscar por nombre de aula"
      />
      <input
        type="date"
        v-model="filters.fecha"
      />
      <select v-model="filters.esValido">
        <option value="">Todos</option>
        <option value="true">Sí</option>
        <option value="false">No</option>
      </select>
      <button @click="resetFilters" class="reset-button">Borrar Filtros</button>
    </div>

    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre de Persona</th>
          <th>Nombre de Aula</th>
          <th>Fecha y Hora</th>
          <th>Es Válido</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in sortedHistorial" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ getPersonaName(item.persona_id) }}</td>
          <td>{{ getAulaName(item.aula_id) }}</td>
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
      historial: [],
      personas: [],
      aulas: [],
      filters: {
        personaName: '',
        aulaName: '',
        fecha: '',
        esValido: ''
      }
    };
  },
  mounted() {
    this.fetchHistorial();
    this.fetchPersonas();
    this.fetchAulas();
  },
  computed: {
    filteredHistorial() {
      return this.historial.filter(item => {
        const personaName = this.getPersonaName(item.persona_id).toLowerCase();
        const aulaName = this.getAulaName(item.aula_id).toLowerCase();
        
        const fecha = new Date(item.fecha_hora).toISOString().split('T')[0]; // Formato YYYY-MM-DD

        const matchesPersonaName = personaName.includes(this.filters.personaName.toLowerCase());
        const matchesAulaName = aulaName.includes(this.filters.aulaName.toLowerCase());
        const matchesFecha = this.filters.fecha ? fecha === this.filters.fecha : true;
        const matchesEsValido = this.filters.esValido ? String(item.es_valido) === this.filters.esValido : true;

        return matchesPersonaName && matchesAulaName && matchesFecha && matchesEsValido;
      });
    },
    sortedHistorial() {
      return this.filteredHistorial.slice().sort((a, b) => a.id - b.id);
    }
  },
  methods: {
    async fetchHistorial() {
      try {
        const response = await axios.get('/historial');
        this.historial = response.data;
      } catch (error) {
        console.error('Error fetching historial:', error);
      }
    },
    async fetchPersonas() {
      try {
        const response = await axios.get('/personas/');
        this.personas = response.data;
      } catch (error) {
        console.error('Error fetching personas:', error);
      }
    },
    async fetchAulas() {
      try {
        const response = await axios.get('/aulas');
        this.aulas = response.data;
      } catch (error) {
        console.error('Error fetching aulas:', error);
      }
    },
    getPersonaName(personaId) {
      const persona = this.personas.find(p => p.id === personaId);
      return persona ? persona.nombre : 'No definido';
    },
    getAulaName(aulaId) {
      const aula = this.aulas.find(a => a.id === aulaId);
      return aula ? aula.nombre_aula : 'No definido';
    },
    resetFilters() {
      this.filters = {
        personaName: '',
        aulaName: '',
        fecha: '',
        esValido: ''
      };
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

.filters {
  margin-bottom: 20px;
  display: flex;
  align-items: center; /* Alinear verticalmente */
}

.filters input,
.filters select {
  margin-right: 10px;
  padding: 5px;
  border-radius: 4px;
  border: 1px solid #444;
  background-color: #2c2c2c;
  color: white;
}

.reset-button {
  padding: 3px 6px; /* Ajuste del tamaño */
  border: none;
  border-radius: 4px;
  background-color: #c0392b; /* Color para el botón */
  color: white;
  cursor: pointer;
  font-size: 0.85rem; /* Tamaño de fuente más pequeño */
}

.reset-button:hover {
  background-color: #e74c3c; /* Color al pasar el mouse */
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
  background-color: #2c2c2c;
  border-bottom: 2px solid #444;
}

tr:nth-child(even) {
  background-color: #2a2a2a;
}

tr:hover {
  background-color: #3a3a3a;
}

tr td {
  border-bottom: 1px solid #444;
}
</style>
