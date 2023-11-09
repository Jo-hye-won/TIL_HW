<template>
  <div>
    <h1>UserView</h1>
    <h2>{{ $route.params.id }}번 유저의 페이지입니다.</h2>
    <h2>{{ userId }}번 유저의 페이지입니다. </h2>
    <button @click="goHome"> 💒 홈으로! 💒</button>
    <button @click="goAnotherUser">100번 유저 페이지로!</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate} from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)

// 프로그래밍 방식 네비게이션
const router = useRouter()

const goHome = function() {
 	// router.push({ name: 'home' }) // 히스토리 남음
  router.replace({name: 'home'}) // 히스토리 남지 않음
 }


// In-component Guard
// 1. onBeforeRouteLeave
onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실건가요?')
  if (answer === false) { // 사용자가 취소를 눌렀다면
    return false // 취소!
  }

})


// 2. onBeforeUpdate
const goAnotherUser = function() {
    router.push({name:'user', params: {id: 100} })
}

onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id
})

</script>

<style scoped>

</style>