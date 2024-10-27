<template>
    <li class="nav-item">
      <a @click="toggle" class="nav-link menu-title" style="display: flex; align-items: center;">
        <img :src="require(`@/assets/${icon}.png`)" alt="Icon" class="icon" />
        <span v-if="!$parent.isCollapsed">{{ title }}</span>
      </a>
      <ul v-if="submenu" class="submenu">
        <slot></slot>
      </ul>
    </li>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      icon: String,
      submenu: Boolean,
    },
    methods: {
      toggle() {
        this.$emit('toggle');
      },
    },
  };
  </script>
  