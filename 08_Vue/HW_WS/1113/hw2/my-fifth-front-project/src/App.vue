<template>
  <h1> pinia + router 연습하기</h1>
  <nav>
    <RouterLink to="/">Home</RouterLink>
  </nav>

  <RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>
