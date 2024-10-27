<template>
  <div :class="['sidebar-menu', { 'collapsed': isCollapsed }]">
    <div class="logo-container">
      <img v-if="!isCollapsed" src="/logo-infl.png" alt="Logo" class="logo" />
      <button @click="toggleMenu" class="toggle-button">
        <img :src="require('@/assets/hide.png')" alt="Toggle Menu" class="hide-icon" />
      </button>
    </div>
    <ul class="nav flex-column" v-show="!isCollapsed">
      <!-- Ambientes -->
      <li class="nav-item">
        <a class="nav-link menu-title" @click="toggleAmbientesSubmenu" style="display: flex; align-items: center;">
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
        <a class="nav-link menu-title" @click="toggleHistorialSubmenu" style="display: flex; align-items: center;">
          <img :src="require('@/assets/historialW.png')" alt="Historial Accesos" class="icon" />
          <span>Historial Accesos</span>
        </a>
        <ul v-if="historialSubmenuVisible" class="submenu">
          <li class="nav-subitem">
            <a class="nav-link" @click="navigateTo('accesos/list')" style="display: flex; align-items: center;">
              <span>Reporte de Acceso</span>
            </a>
          </li>
        </ul>
      </li>

      <!-- Personas -->
      <li class="nav-item">
        <a class="nav-link menu-title" @click="togglePersonasSubmenu" style="display: flex; align-items: center;">
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
        <a class="nav-link menu-title" @click="togglePermisosSubmenu" style="display: flex; align-items: center;">
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

    <!-- Íconos para el menú colapsado -->
    <ul class="nav collapsed-icons" v-show="isCollapsed">
      <li class="nav-item">
        <a @click="openAndNavigate('ambientes', 'create')">
          <img :src="require('@/assets/houseW.png')" alt="Crear Ambiente" class="icon" />
        </a>
      </li>
      <li class="nav-item">
        <a @click="openAndNavigate('accesos', 'list')">
          <img :src="require('@/assets/historialW.png')" alt="Historial Accesos" class="icon" />
        </a>
      </li>
      <li class="nav-item">
        <a @click="openAndNavigate('personas', 'create')">
          <img :src="require('@/assets/personasW.png')" alt="Crear Persona" class="icon" />
        </a>
      </li>
      <li class="nav-item">
        <a @click="openAndNavigate('permisos', 'create')">
          <img :src="require('@/assets/permisosW.png')" alt="Crear Permiso" class="icon" />
        </a>
      </li>
      <li class="nav-item">
        <a @click="logout">
          <img :src="require('@/assets/logoutW.png')" alt="Cerrar Sesión" class="icon" />
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isCollapsed: false,
      ambientesSubmenuVisible: false,
      personasSubmenuVisible: false,
      permisosSubmenuVisible: false,
      historialSubmenuVisible: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isCollapsed = !this.isCollapsed; // Alternar el estado del menú
    },
    toggleAmbientesSubmenu() {
      this.closeAllSubmenus();
      this.ambientesSubmenuVisible = !this.ambientesSubmenuVisible;
    },
    toggleHistorialSubmenu() {
      this.closeAllSubmenus();
      this.historialSubmenuVisible = !this.historialSubmenuVisible;
    },
    togglePersonasSubmenu() {
      this.closeAllSubmenus();
      this.personasSubmenuVisible = !this.personasSubmenuVisible;
    },
    togglePermisosSubmenu() {
      this.closeAllSubmenus();
      this.permisosSubmenuVisible = !this.permisosSubmenuVisible;
    },
    closeAllSubmenus() {
      this.ambientesSubmenuVisible = false;
      this.historialSubmenuVisible = false;
      this.personasSubmenuVisible = false;
      this.permisosSubmenuVisible = false;
    },
    openAndNavigate(menu, action) {
      this.isCollapsed = false; // Abrir el menú
      this.closeAllSubmenus(); // Cerrar todos los submenús
      this.navigateTo(`${menu}/${action}`); // Redirigir a la opción de creación
    },
    navigateTo(route) {
      this.$router.push(`/dashboard/${route}`);
      // No cerrar submenús aquí, simplemente mantener el estado del submenú abierto
    },
    logout() {
      localStorage.removeItem('token'); // Elimina el token
      this.$router.replace('/login'); // Usa replace para evitar que se pueda volver atrás
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
  transition: width 0.3s;
}

.sidebar-menu.collapsed {
  width: 60px; /* Ancho cuando está colapsado */
}

.logo-container {
  margin-bottom: 20px; /* Espacio entre el logo y los enlaces */
  display: flex;
  align-items: center;
}

.toggle-button {
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 24px; /* Tamaño del icono */
}

.hide-icon {
  width: 24px;
  height: 24px; /* Tamaño del icono para ocultar/mostrar */
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

/* Estilo para los íconos en el menú colapsado */
.collapsed-icons {
  display: flex;
  flex-direction: column;
  padding: 10px 0;
}

.collapsed-icons .nav-item {
  margin: 10px 0; /* Espaciado entre íconos */
  text-align: center; /* Centrar los íconos */
}
</style>
