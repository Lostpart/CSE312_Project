<template>
  <form @submit.prevent ="handle"><img src="../assets/chat2.png" style ="float:right" alt="">
      <input type="text" required placeholder="name" v-model="showName">
      <input type="password" required placeholder="password" v-model ="showpassword">
      <button>sign up</button>
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
form{ 
  max-width:435px;
  margin:10px auto;
  background: rgb(251, 255, 255);
  text-align:left;
  padding:40px;
  border-radius: 10px;
}
label{
  color: black;
  display:inline-block;
  margin:25px 0 10px;
  font-size: 0.9em;
  text-transform: 1px;
  font-weight:bold;
}
input{
  display:block;
  padding:5px 6px;
  width:40%;
  box-sizing:border-box;
  border: none;
  border-bottom:1px solid rgb(0, 0, 0);
  color: rgb(4, 0, 0);

}
button
{
  background: rgb(243, 243, 244);
  
  padding: 10px 20px;
  margin-top:20px;
  border-radius: 20px;
}

</style>