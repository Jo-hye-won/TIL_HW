<template>
    <div>
      <h1> 게시글 상세 조회 페이지</h1>
      <div>
        <p>게시글 번호 : {{ post.id }}</p>
        <p>제목 : {{ post.title }}</p>
        <p>내용 : {{ post.content }}</p>
        <p>작성일 : {{ post.created_at }}</p>
        <p>수정일 : {{ post.updated_at }}</p>
      </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const pk = route.params.pk

const post = ref({})
axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`
})
// .then(res => console.log(res))
.then(res => post.value = res.data)
.catch(err=> console.log(err))
</script>

<style scoped>

</style>