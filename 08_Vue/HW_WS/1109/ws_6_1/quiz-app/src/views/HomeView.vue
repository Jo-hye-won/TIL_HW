<!-- HomeVue -->
<template>
  <div class="container my-5">
    <h2 class="fw-bold text-center m-3">퀴즈 앱 사용 방법</h2>
    <div class="d-flex flex-wrap justify-content-center">
      <div class="my-3">
        <h3>1. 퀴즈 목록 확인하기</h3>
        <p>퀴즈 목록 페이지에서 다양한 퀴즈를 확인하세요</p>
        <img src="@/assets/quizList.png" alt="quizList">
      </div>

      <div class="my-3">
        <h3>2. 퀴즈 생성하기</h3>
        <p>퀴즈는 직접 생성 할 수도 있어요</p>
        <img src="@/assets/quizCreate.png" alt="quizCreate">
      </div>

      <div class="my-3">
        <h3>3. 정답 페이지</h3>
        <p>작성한 답안이 정답인지 확인하세요</p>
        <img src="@/assets/quizAnswer.png" alt="quizAnswer">
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
  img {
    width: 500px;
  }
</style>