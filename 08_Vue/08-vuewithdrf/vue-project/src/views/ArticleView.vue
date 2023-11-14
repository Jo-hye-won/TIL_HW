<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{name: 'CreateView'}">
      [CREATE]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

// django에 요청해서 게시글 목록 데이터받아서 sotre의 articles에 저장하는 것
onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>
