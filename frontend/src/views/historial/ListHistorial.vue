<template>
  <div class="sidebar-menu">
    <div class="logo-container">
      <img src="/logo-infl.png" alt="Logo" class="logo" />
    </div>
    <ul class="nav flex-column">
      <!-- Ambientes -->
      <li class="nav-item">
        <a @click="toggleSubmenu" class="nav-link" style="display: flex; align-items: center;">
          <img :src="require('@/assets/houseW.png')" alt="Ambientes" class="icon" />
          <span>Ambientes</span>
        </a>
        <ul v-if="submenuVisible" class="submenu">
          <li class="nav-subitem">
            <a class="nav-link" @click="navigateTo('ambientes/create')" style="display: flex; align-items: center;">
              <span>Crear Ambiente</span>
            </a>
          </li>
          <li class="nav-subitem">
            <a class="nav-link" @click="navigateTo('ambientes/list')" style="display: flex; align-items: center;">
              <span>Lista Ambientes</span>
            </a>
          </li>
        </ul>
      </li>

      <!-- Historial Accesos -->
      <li class="nav-item">
        <a class="nav-link" @click="navigateTo('accesos/list')" style="display: flex; align-items: center;">
          <img :src="require('@/assets/historialW.png')" alt="Historial Accesos" class="icon" />
          <span>Historial Accesos</span>
        </a>
      </li>

      <!-- Otros enlaces -->
      <li class="nav-item">
        <a class="nav-link" @click="navigateTo('personas/create')" style="display: flex; align-items: center;">
          <img :src="require('@/assets/personasW.png')" alt="Personas" class="icon" />
          <span>Crear Persona</span>
        </a>
      </li>

      <!-- Permisos -->
      <li class="nav-item">
        <a class="nav-link" @click="navigateTo('permisos/create')" style="display: flex; align-items: center;">
          <img :src="require('@/assets/permisosW.png')" alt="Permisos" class="icon" />
          <span>Crear Permiso</span>
        </a>
      </li>

      <!-- Logout -->
      <li class="nav-item">
        <a class="nav-link" @click="logout" style="display: flex; align-items: center;">
          <img :src="require('@/assets/logoutW.png')" alt="Cerrar Sesión" class="icon" />
          <span>Cerrar Sesión</span>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      submenuVisible: false
    };
  },
  methods: {
    toggleSubmenu() {
      this.submenuVisible = !this.submenuVisible;
    },
    navigateTo(route) {
      this.$router.push(`/dashboard/${route}`);
    },
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/login'); // Redirige a la página de login
    }
  }
};
</script>
