import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
  ])

  const getUserInfo = computed(() => {
    return (name) => {
      return balances.value.find(info =>{
        return info.name === name
      })
    }
  })
  
  const updateBalance = function(name) {
    const info = balances.value.find(info =>{
      return info.name === name
    })
    info.balance += 1000
  }

  return { balances, getUserInfo, updateBalance }
})
