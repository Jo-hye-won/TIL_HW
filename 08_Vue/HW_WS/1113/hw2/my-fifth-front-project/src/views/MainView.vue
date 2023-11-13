<template>
    <h1> 메인 페이지 </h1>
    <MainPage 
    v-for="info in balances"
    :key="info.name"
    :info="info"
    />
    
</template>

<script setup>
import MainPage from '@/components/MainPage.vue'
import { useBalanceStore } from '../stores/balance'
const store = useBalanceStore()
const { balances } = store
// console.log(balances)

</script>

<style scoped>

</style>
