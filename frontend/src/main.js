import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import 'bootstrap/dist/css/bootstrap.min.css'; // Estilos de Bootstrap
import 'bootstrap'; // JavaScript de Bootstrap

createApp(App)
  .use(router)
  .mount('#app');
