import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const usePostStore = defineStore('post', () => {
  // 백엔드 서버에 post 전체 목록 GET 요청
  // axios가 필요하다
  // axios.get(url)
  // const variable func()
  //  variable.method()
  // func().method()

  const postList = ref([])
  const getPostList = function (){
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/posts/'
    })
      .then((res) => {
        // console.log(res)
        // 객체의 value에 res.data를 넣는다. 
        postList.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    } 
  return { 
    getPostList, postList 
  }
})
