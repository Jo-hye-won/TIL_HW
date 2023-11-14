<template>
  <div>
    <h5> {{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <RouterLink :to="{name: 'DetailView', params: {id: article.id}}">[Detail]</RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

// article이라는 prop데이터를 정의하고 써야함
defineProps({
  article: Object // article을 객체로 받아옴
})

</script>
