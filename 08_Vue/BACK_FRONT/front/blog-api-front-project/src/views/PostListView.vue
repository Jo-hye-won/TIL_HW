<template>
    <div>
      <button>
        <RouterLink :to="{name: 'postCreate'}"> 게시글 생성하기</RouterLink> 
      </button>
      <h1> 📃_게시글 목록 페이지 </h1>
      <div
      v-for="post in store.postList"
      :key="post.pk"
      @click="goToDetail(post.pk)"
      class="post-link"
      >
        <h3> {{ post.pk }} 번 글 🖋 | {{ post.title }} </h3>
        <hr>
    </div>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { usePostStore} from '@/stores/post'
import { useRouter } from 'vue-router'
const router = useRouter()

// sotre에 정의한 actions 가져와서 실행하기
const store = usePostStore()

// 현재 컴포넌트가 마운트 되고난 후에, axios 요청 보낼 것
onMounted(() => {
  store.getPostList()
})

const goToDetail = function(pk) {
  router.push({name: 'detail', params: {pk: pk}})
}


</script>

<style scoped>
.post-link {
  cursor: pointer;
}

.post-link:hover {
  background-color: goldenrod;
  transition: 2s;
  height: 100px;
}

</style>