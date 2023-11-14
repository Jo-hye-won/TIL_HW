<template>
    <div>
      <h1> 게시글 생성 페이지</h1>
      <!-- form 태그 -->
      <form @submit.prevent="createPost">
        <!-- 선택할 카테고리 목록 -->
        <label for="category">카테고리</label>
        <select id="category" v-model="category">
          <option 
            v-for="category in store.categoryList"
            :key="category.id"
            :value="category.id"
            >
            {{ category.name }}
          </option>
          <!-- <option value="2">두번째</option>
          <option value="3">세번째</option>
          <option value="4">네번째</option> -->
        </select>
        <!-- 제목 -->
        <label for="title"> 제목 </label>
        <input type="text" id="title" v-model="title">
        <!-- 내용 -->
        <label for="content"> 내용 </label>
        <input type="text" id="content" v-model="content">
        <!-- 버튼 : 게시글 생성 -->
        <button>게시글 생성</button>
      </form>
      <p>{{ store.CategoryList }}</p>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { onMounted } from 'vue';
import { useCategoryStore } from '@/stores/category'
import { useRouter } from 'vue-router'

const store = useCategoryStore()
const router = useRouter()

onMounted(() => {
  store.getCategoryList()
})

const title = ref('')
const content = ref('')
const category = ref(1)
const createPost = function(){
  axios({
    method: 'POST',
    url:'http://127.0.0.1:8000/api/v1/posts/',
    data: {
      title: title.value,
      content: content.value,
      category: category.value,
    }
  })
  .then(res => {
      router.push({name: 'detail', params:{pk: res.data.id}})
    })
  .catch(err => {
      console.log(err)
    })
}

// input 태그에 입력한 내용 담을 수 있는 객체
  // 카테고리는 -> db에 있는 목록을 보여줘야 한다. 
    // store에서 category  전체 목록 axios 요청 보내서 응답 받은 데이터
  // submit 이벤트 발생시에는
    // 담고 있는 데이터를 모아서 back POST 요청 보내야 한다. 


</script>

<style scoped>

</style>