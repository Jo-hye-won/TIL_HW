<template>
  <div>
    <p> 이름 : {{ info.name }}</p>
    <p> 잔고 : {{ info.balance }}</p>
    <!-- <RouterLink :to="{name:'update', params:{username: info.name}}">updateBalance</RouterLink> -->
    <button @click="goToUpdate">updateBalance</button>
    <!-- <button @click="$router.push({name:'update', params:{username: info.name}})">updateBalance</button> -->
    <hr>
  </div>
</template>

<script setup>
// import { RouterLink } from 'vue-router';
import { useRouter } from 'vue-router';
const props = defineProps({
  info: Object
})

const router = useRouter()

const goToUpdate = function () {
  router.push({
    name: 'update',
    params: {
      username: props.info.name
    }
  })
}
</script>

<style scoped>

</style>