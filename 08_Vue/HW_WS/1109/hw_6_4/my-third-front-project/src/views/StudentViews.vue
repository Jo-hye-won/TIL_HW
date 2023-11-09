<template>
  <h2>학생 상세 정보 목록 입니다.</h2>
  <p v-for="student in students"
    :key="student.name"
    :student="student"
    @click="goStudentViews(student.name)"> 
    {{ student.name }} 학생 정보 보기</p>

</template>

<script setup>
import StudentDetailView from '@/views/StudentDetailView.vue';
import { ref } from 'vue'
import { useRouter } from 'vue-router';
const students = ref([
    { name: '김하나'},
    { name: '김두리'},
    { name: '김서이'},
])

const router = useRouter()
const goStudentViews = function(namevalue) {
  router.push({name:'studentsname', 
  params:{ 
    name: namevalue }
  })
} 
</script>

<style scoped>

</style>