<template>
  <div class="login-container">
    <div class="login-box">
      <img src="/logo-infl.png" alt="Logo" class="login-logo" />
      <h2>Iniciar sesión</h2>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="nombre_usuario">Nombre de Usuario</label>
          <input type="text" v-model="nombre_usuario" id="nombre_usuario" placeholder="Ingrese su nombre de usuario" />
        </div>
        <div class="form-group">
          <label for="password">Contraseña</label>
          <input type="password" v-model="password" id="password" placeholder="Ingrese su contraseña" />
        </div>
        <button type="submit" class="btn-login">Iniciar Sesión</button>
      </form>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from '@/plugins/axios';

export default {
  data() {
    return {
      nombre_usuario: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('/login', {
          nombre_usuario: this.nombre_usuario,
          password: this.password
        });

        if (response.data.status === 'success') {
          localStorage.setItem('token', response.data.token);
          this.$router.push('/dashboard'); // Redirige a donde quieras
        } else {
          this.errorMessage = response.data.message;
        }
      } catch (error) {
        this.errorMessage = 'Usuario o Contraseña incorrecta. Intente nuevamente.';
      }
    }
  }
};
</script>



<style scoped>

.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
  margin-bottom: 2px;
  color: white; /* Cambia el color del texto de la etiqueta a blanco */
}

.form-group input {
  width: 100%;
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ddd; /* Puedes ajustar el color del borde si es necesario */
  background-color: #ffffff; /* Cambia el fondo del input a blanco */
  color: #000000; /* Cambia el color del texto dentro del input a negro (o lo que prefieras) */
}

.login-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #2c2c2c;
}

.login-box {
  background-color: #000;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  width: 300px;
  text-align: center;
}

.login-logo {
  width: 200px;
  margin-bottom: 20px;
}

.login-box h2 {
  color: #ff4c4c;
  text-align: center;
  margin-bottom: 20px;
}

.login-box input {
  width: 90%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ff4c4c;
  border-radius: 4px;
  background-color: #333;
  color: #fff;
}

.login-box button {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 4px;
  background-color: #ff4c4c;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}

.login-box button:hover {
  background-color: #e03a3a;
}


.error-message {
  color: #ff4c4c;
  margin-top: 10px;
}
</style>

<style>
  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: #2c2c2c; 
  }

  #app {
    height: 100%;
  }
</style>
