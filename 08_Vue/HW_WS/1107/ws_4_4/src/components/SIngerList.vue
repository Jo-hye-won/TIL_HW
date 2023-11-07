<template>
  <div>
    <h1>가수 목록</h1>
    <ul>
      <p> {{ singers }}</p>
      <SingerDetail 
        v-for="singer in singers"
        :key="singer.name"
      />
    </ul>
  </div>
</template>

<script setup>
import SingerDetail from '@components/singer'

const singers = [
  {
    name: '아이유'
  },
  {
    name: 'adele'
  },
  {
    name: 'muse'
  },
]
</script>

<style scoped>

</style>