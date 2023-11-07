<template>
  <div>
    <input type="text" ref="ssafy">
  </div>
</template>

<script setup>
import { ref } from 'vue'

const ssafy = ref()

console.log(ssafy.value)
</script>

<style scoped>

</style>