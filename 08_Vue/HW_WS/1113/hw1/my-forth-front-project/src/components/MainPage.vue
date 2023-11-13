<template>
    <div>
      <h1> pinia 연습하기</h1>
      <ParentPage 
      v-for="info in store.familyInfo"
      :key="info.familyName"
      :info="info"
      />
    </div>
</template>

<script setup>
import ParentPage from '@/components/ParentPage.vue'
import { useFamilyStore } from '@/stores/family.js'

const store = useFamilyStore()

// const { familyInfo } = store
// const familyInfo = store.getFamilyInfo

</script>

<style scoped>

</style>