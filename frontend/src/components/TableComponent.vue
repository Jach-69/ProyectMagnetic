<template>
  <table class="table-container">
    <thead>
      <tr>
        <th v-for="(header, index) in headers" :key="index">{{ header }}</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in items" :key="index">
        <td v-for="(value, key) in item" :key="key">{{ value }}</td>
        <td>
          <button @click="$emit('edit', item)" class="btn-action">Editar</button>
          <button @click="$emit('delete', item.id)" class="btn-action btn-delete">Eliminar</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    headers: Array,
    items: Array
  }
};
</script>

<style scoped>
.table-container {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

th {
  background-color: #000000
}

tr:hover {
  background-color: #f5f5f5;
}

.btn-action {
  padding: 5px 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

.btn-action.btn-delete {
  background-color: #f44336;
}

.btn-action:hover {
  background-color: #45a049;
}

.btn-action.btn-delete:hover {
  background-color: #e03a3a;
}
</style>
