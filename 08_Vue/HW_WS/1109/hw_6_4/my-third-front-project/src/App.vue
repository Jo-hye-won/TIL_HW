<template>
  <div>
    <MainPage />
  </div>
  <main>
    <div>
      <RouterLink :to="{ name: 'some'}"> Some</RouterLink> | 
      <RouterLink :to="{ name: 'other'}"> Other</RouterLink> |
      <RouterLink :to="{ name:'students' }">Students</RouterLink>
    </div>
  </main>

  <RouterView />
  
</template>

<script setup>
import MainPage from '@/components/MainPage.vue'
import { RouterLink, RouterView } from 'vue-router';

</script>

<style scoped>

</style>