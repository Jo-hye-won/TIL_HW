<template>
  <div>
    <h1> 부모 페이지입니다. </h1>
    <ChildPage 
     v-for="child in children"
     :key="child.name"
     :child="child"
     @give-me-money-event="updateBalance"
    />
  </div>
</template>

<script setup>
   import { ref } from 'vue'
   import ChildPage from './ChildPage.vue';
   const children = ref([
    {
      name: '김하나',
      age:30,
      balance: 100000
    },
    {
      name: '김두리',
      age:20,
      balance: 10000
    },
    {
      name: '김서이',
      age:10,
      balance: 1000
    },
   ])

    const updateBalance = function(child) {
      child.balance += 1000
    }

</script>

<style scoped>
.div {
  border: 1px solid lightslategray;
  margin: 5px;
  padding: 10px;
}
</style>