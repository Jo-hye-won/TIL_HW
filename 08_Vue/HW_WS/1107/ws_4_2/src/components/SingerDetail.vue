<template>
  <div class="container">
    <div class="item">
      <h1>가수 목록</h1>
    </div>  
  </div>
  <div class="container2">
    <div class="item">
        <h1>가수 이름</h1>
        <img class="imgsize" src="src/assets/singer.jpg" alt="">
        <p>가수 소개글</p>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.div_border {
  border-color: black;
}

.imgsize {
  width: 200px;
  border-radius: 50%;
}

.container {
  display: flex;
  justify-content: center;
  /* justify-items: center; */

}

.container2 {
  display: flex;
  justify-content: center;
  /* justify-items: center; */
  /* border: solid medium */
  border: solid thin;
}


.item {
  text-align: center;
}

</style>