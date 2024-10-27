<template>
    <li class="nav-subitem">
      <a class="nav-link" @click="clickHandler" style="display: flex; align-items: center;">
        <span>{{ title }}</span>
      </a>
    </li>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
    },
    methods: {
      clickHandler() {
        this.$emit('click');
      },
    },
  };
  </script>
  