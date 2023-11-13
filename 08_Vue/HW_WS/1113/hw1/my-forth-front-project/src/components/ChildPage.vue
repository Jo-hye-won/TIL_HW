<template>
    <div class="line">
      <h3> 자식 페이지 </h3>
      <p>{{ child.name }}</p>
    </div>
</template>

<script setup>
defineProps({
  child: Object
})
</script>

<style scoped>
.line {
  border: 1px solid lightgray;
  width: 80%;
  justify-items: center;  
}

</style>