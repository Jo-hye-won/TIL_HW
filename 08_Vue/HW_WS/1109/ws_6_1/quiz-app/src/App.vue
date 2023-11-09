<template>

<div class="container" style="background-color: lightgray; width: 31rem; display: flex; flex-direction: column;  justify-content: center;">
  <div class="card" style="width: 30rem;" >
    <div class="card-header text-white fw-bold fs-3" style="background-color: orange;">
      Quiz 퀴즈
    </div>
        <div class="card-body">
          <blockquote class="blockquote mb-0 fs-6">
            <p> 여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
          </blockquote>
        </div>
    </div>
</div>
  <div>
    <div>
      <h1 class="quiz"></h1>
      <p class="detail"></p>
   </div>
   <nav class="navbar navbar-dark bg-dark text-white text-align text-center mx-auto"><RouterLink to="/">Home     |   </RouterLink></nav>
  </div>


<RouterView />

</template>

<script setup>
import 'bootstrap/dist/css/bootstrap.css'
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>

*{
  text-align: center;
}

</style>