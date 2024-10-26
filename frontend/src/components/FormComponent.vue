<template>
  <form @submit.prevent="handleSubmit" class="form-container">
    <div v-for="(field, index) in fields" :key="index" class="form-group">
      <label :for="field.name">{{ field.label }}</label>
      <input
        :type="field.type"
        :id="field.name"
        :name="field.name"
        v-model="localFormData[field.name]"
        class="form-control"
      />
    </div>
    <button type="submit" class="btn-submit">{{ buttonText }}</button>
  </form>
</template>

<script>
export default {
  props: {
    fields: Array, // Definir campos dinámicamente desde el padre
    formData: Object, // Los datos para el formulario
    buttonText: {
      type: String,
      default: "Enviar"
    },
  },
  data() {
    return {
      localFormData: { ...this.formData } // Crea una copia local de formData
    };
  },
  methods: {
    handleSubmit() {
      this.$emit("submit", this.localFormData);
    }
  },
  watch: {
    // Si formData cambia, actualiza la copia local
    formData: {
      handler(newVal) {
        this.localFormData = { ...newVal };
      },
      deep: true
    }
  }
};
</script>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 600px;
  margin: auto;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  padding: 10px;
  font-size: 16px;
  width: 100%;
}

.btn-submit {
  background-color: #4CAF50;
  color: white;
  padding: 10px;
  border: none;
  cursor: pointer;
}

.btn-submit:hover {
  background-color: #45a049;
}
</style>
