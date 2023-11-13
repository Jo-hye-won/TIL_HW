<template>
    <div>
      <h3>데이터 수정 페이지</h3>
      <p> 이름 : {{ getUserInfo.name }}</p>
      <p> 잔고 : {{ getUserInfo.balance }}</p>
      <button @click="updateBalance(getUserInfo.name)"> + </button>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const store = useBalanceStore()
const route = useRoute()
const name = route.params.username

const getUserInfo = store.getUserInfo(name)

const updateBalance = function(name) {
  store.updateBalance(name)
}

</script>

<style scoped>

</style>