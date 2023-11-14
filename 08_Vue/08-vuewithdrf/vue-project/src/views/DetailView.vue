<template>
  <div>
    <h1>Datail</h1>
    <div v-if="article">
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성일 : {{ article.created_at }}</p>
    <p>수정일 : {{ article.updated_at }}</p>
  </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
// const article = ref(null)로 하면 오류가 날 수 있음
// const article = ref('') 이렇게 해도 되고 
const article = ref(null) // <div v-if="article">하면 null로 둬도 됨

onMounted(() => {
  axios({
    method: 'get',
    url:`${store.API_URL}/api/v1/articles/${route.params.id}`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})
// 장고측에 1번 게시글 줘 



</script>

<style>

</style>
