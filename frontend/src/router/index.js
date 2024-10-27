import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import DashboardPage from '@/views/DashboardPage.vue';

// Importar tus vistas
import CreatePermiso from '@/views/permisos/CreatePermiso.vue';
import ListPermiso from '@/views/permisos/ListPermiso.vue';
import EditPermiso from '@/views/permisos/EditPermiso.vue';
import ListAcceso from '@/views/accesos/ListAcceso.vue';
import ListHistorial from '@/views/historial/ListHistorial.vue';

// Función para verificar si el usuario está autenticado
const isAuthenticated = () => {
  return !!localStorage.getItem('token'); // Retorna true si hay un token
};

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginPage },
  { 
    path: '/dashboard', 
    component: DashboardPage,
    beforeEnter: (to, from, next) => {
      if (!isAuthenticated()) {
        next('/login'); // Redirige a login si no está autenticado
      } else {
        next(); // Permite el acceso
      }
    },
    children: [
      { path: 'ambientes/create', component: () => import('@/views/ambientes/CreateAmbiente.vue') },
      { path: 'ambientes/list', component: () => import('@/views/ambientes/ListAmbientes.vue') },
      { path: 'personas/create', component: () => import('@/views/personas/CreatePersona.vue') },
      { path: 'permisos/create', component: CreatePermiso },
      { path: 'accesos/list', component: ListAcceso },
      { path: 'personas/list', component: () => import('@/views/personas/ListPersona.vue') },
      { path: 'personas/edit/:id', component: () => import('@/views/personas/EditPersona.vue'), props: true },
      { path: 'permisos/list', component: ListPermiso },
      { path: 'permisos/edit/:id', component: EditPermiso },
      { path: 'historial/list', component: ListHistorial },
    ]
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
