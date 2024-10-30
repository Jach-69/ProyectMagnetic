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
    </div>

    <div class="button-container">
      <div class="descripcion-container">
        <label for="descripcion">Descripción:</label>
        <input
          type="text"
          v-model="descripcion"
          id="descripcion"
          placeholder="Descripción"
        />
      </div>
      <button @click="resetFilters" class="reset-button">Borrar Filtros</button>
      <button @click="generatePDF" class="pdf-button">Generar PDF</button>
    </div>

    <table>
      <thead>
        <tr>
          <th>Nro</th>
          <th>Nombre de Persona</th>
          <th>Nombre de Aula</th>
          <th>Fecha y Hora</th>
          <th>Es Válido</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in sortedHistorial" :key="item.id">
          <td>{{ index + 1 }}</td>
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
import { jsPDF } from 'jspdf';
import 'jspdf-autotable';

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
      },
      descripcion: ''
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
        
        const fecha = new Date(item.fecha_hora).toISOString().split('T')[0];

        const matchesPersonaName = personaName.includes(this.filters.personaName.toLowerCase());
        const matchesAulaName = aulaName.includes(this.filters.aulaName.toLowerCase());
        const matchesFecha = this.filters.fecha ? fecha === this.filters.fecha : true;
        const matchesEsValido = this.filters.esValido ? String(item.es_valido) === this.filters.esValido : true;

        return matchesPersonaName && matchesAulaName && matchesFecha && matchesEsValido;
      });
    },
    sortedHistorial() {
      return this.filteredHistorial.slice().sort((a, b) => new Date(b.fecha_hora) - new Date(a.fecha_hora));
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
      return persona ? persona.nombre : 'Desconocido';
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
      this.descripcion = '';
    },
    async generatePDF() {
      const pdf = new jsPDF();

      const logoUrl = require('@/../public/logotipo-A.png');
      const img = new Image();
      img.src = logoUrl;

      img.onload = async () => {
        pdf.addImage(img, 'PNG', 14, 10, 50, 20);

        const date = new Date().toLocaleDateString('es-ES');
        pdf.setFontSize(12);
        pdf.text(date, 160, 20);

        pdf.setFontSize(22);
        pdf.text("Historial de Accesos", pdf.internal.pageSize.getWidth() / 2, 40, { align: 'center' });

        // Añadir la descripción con formato
        pdf.setFontSize(12);
        pdf.text(`Descripción: ${this.descripcion}`, 14, 50);

        const col = ["Nro", "Nombre de Persona", "Nombre de Aula", "Fecha y Hora", "Es Válido"];
        const rows = this.sortedHistorial.map((item, index) => [
          index + 1,
          this.getPersonaName(item.persona_id),
          this.getAulaName(item.aula_id),
          item.fecha_hora,
          item.es_valido ? 'Sí' : 'No'
        ]);

        pdf.autoTable(col, rows, {
          startY: 60,
          headStyles: { fillColor: [44, 44, 44], textColor: [255, 255, 255] },
          styles: { fillColor: [255, 255, 255], textColor: [0, 0, 0] }
        });

        const pageCount = pdf.internal.getNumberOfPages();
        for (let i = 1; i <= pageCount; i++) {
          pdf.setPage(i);
          pdf.setFontSize(10);
          pdf.text(`Página ${i} de ${pageCount}`, pdf.internal.pageSize.getWidth() - 20, pdf.internal.pageSize.getHeight() - 10, { align: 'right' });
        }

        pdf.save('historial_de_accesos.pdf');
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
  align-items: center;
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

.button-container {
  display: flex;
  align-items: center;
  justify-content: space-between; /* Alinear los elementos a los extremos */
  margin-top: 10px;
}

.descripcion-container {
  display: flex;
  align-items: center;
  margin-right: 10px;
}

.descripcion-container label {
  margin-right: 5px;
  color: white; /* Para que el label sea visible */
}

.reset-button {
  padding: 3px 6px;
  border: none;
  border-radius: 4px;
  background-color: #c0392b;
  color: white;
  cursor: pointer;
  font-size: 0.85rem;
}

.pdf-button {
  padding: 3px 6px;
  border: none;
  border-radius: 4px;
  background-color: #27ae60;
  color: white;
  cursor: pointer;
  font-size: 0.85rem;
  margin-left: 10px;
}

.pdf-button:hover {
  background-color: #2ecc71; 
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
