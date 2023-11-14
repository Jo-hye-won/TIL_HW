import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios' // axios 설치 해뒀기 때문에 쓰고하 하는곳에서 이케 import 해주면 됨

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
    // 실제 data는 장고에 요청해서 받아와야 한다. 
    // 그래서 여기 나중엔 빈 배열로 만들어둘거임!! 
    // axios를 동작하게 하는 액션을 해야함 중앙저장소에서 작성해야 함
  
  const API_URL = 'http://127.0.0.1:8000'

  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
    .then((res) => {
      // console.log(res)

      articles.value = res.data  
      // response(res)에서 받아서 articles의 빈 배열에 장고의 데이터가 저장됨
    })
    .catch((err) => {
      console.log(err)
    })
  }
  
  return { articles, API_URL, getArticles }  //articleList 컴포넌트 참조해야함
}, { persist: true }) // persist: true = plugin추가 
