<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <!-- { 키값 : 'value'} -->
        <RouterLink :to="{name: 'main'}"> | Main |</RouterLink>
        
        <RouterLink :to="{name: 'posts'}">| Posts |</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

.wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

nav {
  text-align: center;
  background-color: #B4BDFF;
  /* px보다 상대단위(rem)를 쓰는게 나음 */
  padding: 1rem; 
}

nav a {
  color: white;
  /* a태그에 들어가는 밑줄 없애기 */
  text-decoration: none;
  font-weight: bold;
}
</style>
