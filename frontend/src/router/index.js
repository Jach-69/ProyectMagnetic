import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import DashboardPage from '@/views/DashboardPage.vue';
import CreateCampus from '@/views/campus/CreateCampus.vue';
import ListCampus from '@/views/campus/ListCampus.vue';
import EditCampus from '@/views/campus/EditCampus.vue';
import ListBloque from '@/views/bloques/ListBloque.vue';
import EditBloque from '@/views/bloques/EditBloque.vue';
import ListRol from '@/views/roles/ListRol.vue';
import CreateRol from '@/views/roles/CreateRol.vue';
import EditRol from '@/views/roles/EditRol.vue';
import ListAula from '@/views/aulas/ListAula.vue';
import CreateAula from '@/views/aulas/CreateAula.vue';
import EditAula from '@/views/aulas/EditAula.vue';
import CreateUsuario from '@/views/usuarios/CreateUsuario.vue';
import ListUsuario from '@/views/usuarios/ListUsuario.vue';
import EditUsuario from '@/views/usuarios/EditUsuario.vue';
import CreatePermiso from '@/views/permisos/CreatePermiso.vue';
import ListPermiso from '@/views/permisos/ListPermiso.vue';
import EditPermiso from '@/views/permisos/EditPermiso.vue';
import ListAcceso from '@/views/accesos/ListAcceso.vue';
import ListHistorial from '@/views/historial/ListHistorial.vue';

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginPage },
  { 
    path: '/dashboard', 
    component: DashboardPage,
    children: [
      { path: 'campus/create', component: CreateCampus },
      { path: 'campus/list', component: ListCampus },
      { path: 'ambientes/create', component: () => import('@/views/ambientes/CreateAmbiente.vue') },
      { path: 'ambientes/list', component: () => import('@/views/ambientes/ListAmbientes.vue') },
      { path: 'personas/create', component: () => import('@/views/personas/CreatePersona.vue') },
      { path: 'permisos/create', component: CreatePermiso },
      { path: 'accesos/list', component: ListAcceso },


      { path: 'campus/edit/:id', component: EditCampus, props: true },
      { path: 'personas/create', component: () => import('@/views/personas/CreatePersona.vue') },
      { path: 'personas/list', component: () => import('@/views/personas/ListPersona.vue') },
      { path: 'personas/edit/:id', component: () => import('@/views/personas/EditPersona.vue'), props: true },
      { path: 'bloques/create', component: () => import('@/views/bloques/CreateBloque.vue') },
      { path: 'bloques/list', component: ListBloque },
      { path: 'bloques/edit/:id', component: EditBloque, props: true },
      { path: 'roles/list', component: ListRol },
      { path: 'roles/create', component: CreateRol },
      { path: 'roles/edit/:id', component: EditRol, props: true },
      { path: 'aulas/create', component: CreateAula },
      { path: 'aulas/list', component: ListAula },
      { path: 'aulas/edit/:id', component: EditAula, props: true },
      { path: 'usuarios/create', component: CreateUsuario },
      { path: 'usuarios/list', component: ListUsuario },
      { path: 'usuarios/edit/:id', component: EditUsuario, props: true },
      { path: 'permisos/create', component: CreatePermiso },
      { path: 'permisos/list', component: ListPermiso },
      { path: 'permisos/edit/:id', component: EditPermiso },
      { path: 'accesos/list', component: ListAcceso },
      { path: 'historial/list', component: ListHistorial },
    ]
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
