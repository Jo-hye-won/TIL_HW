<template>
  <div class="container">
    <div>
      <div>
        <h1>가수 목록</h1>
      </div>  
    </div>
        <div class="item">
          <h1>가수 이름</h1>
          <img src="@/assets/singer.jpg" alt="singer">
          <img class="imgsize" src="@/assets/singer.jpg" alt="">
          <p>가수 소개글</p>
          <SingerAlbum />
          <SingerAlbum />
      </div>
    
  </div>
</template>

<script setup>
import SingerAlbum from "@/components/singers/SingerAlbum.vue'"

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
  margin:auto;
  flex-direction: column;
  align-items: center;
  /* justify-items: center; */

}

.container2 {
  display: flex;
  justify-content: center;
  margin: auto;
  justify-items: center;
  /* border: solcid medium */
  border: solid thin;
  /* border-width: 200px; */
  box-sizing: border-box;
  /* width: 700px;  */
 
}

.item {
  text-align: center;
  width:700px;
  border: solid thin;
}


</style>