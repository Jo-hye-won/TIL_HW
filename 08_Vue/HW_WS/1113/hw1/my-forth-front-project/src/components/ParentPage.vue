<template>
    <div>
      <div class="div-b">
      <h2> 부모 컴포넌트 </h2>
      <!-- <p> 가문명: {{ info.familyName }}</p> -->
      <p> {{ info.father }} </p>
      <p> {{ info.mother }} </p>
      
      <ChildPage 
      v-for="child in info.children"
      :key="child.name"
      :child="child"/>
    </div>
    </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue'

defineProps({
  info:Object
})

</script>

<style scoped>
.div-b {
  border: 1px solid gray;
  margin: auto;
  text-align: center;
}

</style>