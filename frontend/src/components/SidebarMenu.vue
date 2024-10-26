<template>
  <div class="sidebar-menu">
    <div class="logo-container">
      <img src="/logo-infl.png" alt="Logo" class="logo" />
    </div>
    <ul class="nav flex-column">
      <!-- Ambientes -->
      <li class="nav-item">
        <a @click="toggleAmbientesSubmenu" class="nav-link menu-title" style="display: flex; align-items: center;">
          <img :src="require('@/assets/houseW.png')" alt="Ambientes" class="icon" />
          <span>Ambientes</span>
        </a>
        <ul v-if="ambientesSubmenuVisible" class="submenu">
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

      <!-- Personas -->
      <li class="nav-item">
        <a @click="togglePersonasSubmenu" class="nav-link menu-title" style="display: flex; align-items: center;">
          <img :src="require('@/assets/personasW.png')" alt="Personas" class="icon" />
          <span>Personas</span>
        </a>
        <ul v-if="personasSubmenuVisible" class="submenu">
          <li class="nav-subitem">
            <a class="nav-link" @click="navigateTo('personas/create')" style="display: flex; align-items: center;">
              <span>Crear Persona</span>
            </a>
          </li>
          <li class="nav-subitem">
            <a class="nav-link" @click="navigateTo('personas/list')" style="display: flex; align-items: center;">
              <span>Lista Personas</span>
            </a>
          </li>
        </ul>
      </li>

      <!-- Permisos -->
      <li class="nav-item">
        <a @click="togglePermisosSubmenu" class="nav-link menu-title" style="display: flex; align-items: center;">
          <img :src="require('@/assets/permisosW.png')" alt="Permisos" class="icon" />
          <span>Permisos</span>
        </a>
        <ul v-if="permisosSubmenuVisible" class="submenu">
          <li class="nav-subitem">
            <a class="nav-link" @click="navigateTo('permisos/create')" style="display: flex; align-items: center;">
              <span>Crear Permiso</span>
            </a>
          </li>
          <li class="nav-subitem">
            <a class="nav-link" @click="navigateTo('permisos/list')" style="display: flex; align-items: center;">
              <span>Lista Permisos</span>
            </a>
          </li>
        </ul>
      </li>

      <!-- Logout -->
      <li class="nav-item">
        <a class="nav-link logout-button" @click="logout" style="display: flex; align-items: center;">
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
      ambientesSubmenuVisible: false,
      personasSubmenuVisible: false,
      permisosSubmenuVisible: false,
    };
  },
  methods: {
    toggleAmbientesSubmenu() {
      this.ambientesSubmenuVisible = !this.ambientesSubmenuVisible;
    },
    togglePersonasSubmenu() {
      this.personasSubmenuVisible = !this.personasSubmenuVisible;
    },
    togglePermisosSubmenu() {
      this.permisosSubmenuVisible = !this.permisosSubmenuVisible;
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

<style scoped>
.sidebar-menu {
  width: 250px;
  background-color: #1e1e1e;
  height: 100vh;
  padding: 20px;
  color: white;
  overflow-y: auto;
}

.logo-container {
  margin-bottom: 20px; /* Espacio entre el logo y los enlaces */
}

.submenu {
  margin-left: 20px;
  list-style-type: none;
  padding: 0;
}

.nav-subitem {
  margin-bottom: 10px;
}

.menu-title {
  font-weight: bold;
  color: #e03a3a; /* Color para diferenciar los menús */
}

.nav-link {
  color: white;
  text-decoration: none;
  padding: 10px 5px; /* Espacio alrededor del texto */
}

.nav-link:hover {
  background-color: #e03a3a;
  color: white;
}

.logout-button {
  background-color: #c0392b; /* Color de fondo para el botón de cerrar sesión */
  color: white;
  border-radius: 10px;
  margin-top: 15px;
}

.logout-button:hover {
  background-color: #a83229; /* Color más oscuro al pasar el ratón */
}

.icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}

.logo {
  max-width: 70%;
  height: auto;
}
</style>
