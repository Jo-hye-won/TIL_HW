<template>
  <div class="main-page">
    <h1>😛 Hyewon's 블로그 😛</h1>
    <h5>Welcome to my personal blog_! 🙋‍♀️</h5>
  </div>
</template>

<script setup>

</script>

<style scoped>
.main-page {
  display: flex;
  /* 메인축을 수직으로 바꿔주기 */
  /* 수직으로 축을 두고 정렬시키기 위해서 */
  flex-direction: column;

  /* 메인축 기준으로 중앙 정렬 */
  justify-content: center;
  height: 100vh;

  /* 교차축 기준 중앙 정렬 */
  align-items: center;

  background-color: rgb(240, 225, 253);
  
}

</style>