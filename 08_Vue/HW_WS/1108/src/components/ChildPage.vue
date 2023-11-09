<template>
  <div>
    <h3>자식 페이지 입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
    <p>잔액 : {{ child.balance }}</p>
    <button @click="giveMeMoney">용돈 올려주세요</button>
  </div>
</template>

<script setup>

const props = defineProps({
  child: Object,
})

const emit = defineEmits(['giveMeMoneyEvent'])
const giveMeMoney = function() {
  // console.log(props.child.balance)
  // props.child.balance += 1000
  emit('giveMeMoneyEvent', props.child)
}

// script 영역에서 사용하고 싶다면, 
// const props = defineProps({
//   child: Object,  
// })
// console.log(props)

</script>

<style scoped>

</style>