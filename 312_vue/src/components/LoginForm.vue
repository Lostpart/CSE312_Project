<template>
  <form @submit.prevent ="handle"><img src="../assets/chat2.png" style ="float:right" alt="">
      <input type="text" required placeholder="name" v-model="showName"> 
      
      <input type="password" required placeholder="password" v-model ="showpassword">
     
      <button>Login </button>
  </form>
</template>

<script>
import { ref } from 'vue'
export default {
    setup()
    {
        const showName = ref('')
       const  showpassword = ref('')
        const handle=()=>{
            console.log(showName.value, showpassword.value)
        }
        return{showName, showpassword,handle}
    }
}
</script>

<style>
</style>