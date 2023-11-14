import axios from 'axios'
import { ref } from "vue";
import { defineStore } from "pinia";

export const useCategoryStore = defineStore('category', () => {
  const categoryList = ref([])

  const getCategoryList = () => {
    axios({
      method: 'GET',
      url: 'http://127.0.0.1:8000/api/v1/categories/'
    })
      .then(res => categoryList.value = res.data)
      // .then(res => console.log(res.data))
      .catch(err => console.log(err))
  }
  return {
    categoryList, getCategoryList
  }
})