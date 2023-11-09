<template>
  <div>
    <h2>학생 상세 정보 페이지입니다.</h2>
    <p>이름: {{ studentname }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute() // Route에 들어있는 객체를 들고오고 싶어요 (객체 정보 불러오기 = Route)
const studentname = ref(route.params.name) // Route가 들고있는 정보중에 params 정보 중에 name 값
</script>

<style scoped>

</style>