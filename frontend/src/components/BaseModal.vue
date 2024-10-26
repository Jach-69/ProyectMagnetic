<template>
  <div v-if="isOpen" class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content" :style="customStyle">
      <button class="close-button" @click="$emit('close')">✖</button>
      <h2>{{ title }}</h2>
      <slot></slot> <!-- Aquí se insertará el contenido del formulario -->
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isOpen: Boolean,
    title: String,
    customStyle: Object, // Nueva prop para estilos personalizados
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: #444;
  padding: 20px;
  border-radius: 10px;
  max-width: 400px; /* Tamaño por defecto */
  width: 100%;
  color: white;
  position: relative;
}

.close-button {
  background: none;
  color: white;
  border: none;
  cursor: pointer;
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 20px;
}
</style>
