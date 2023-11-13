<template>
    <div>
      <!-- {{ store.todos }} -->
     
      <TodoListItem 
      v-for="todo in store.todos"
      :key="todo.id"
      :todo-data="todo"  
    />
     <!-- :todo-data="todo" 에서 왼쪽에 있는거는 prop 이름이다 -->
    </div>
</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()


</script>

<style scoped>

</style>