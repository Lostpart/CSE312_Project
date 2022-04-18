<template>
  <div class = "header">
      <p>Welcome to Chat App</p> 
      <div v-if = "displayLogin">
          <h2>login</h2>
          <login />
          <p>😭 no account?  <span @click="displayLogin = false">click me signup now</span> </p>

         
      </div>
      <div v-else>
          <h2>Sign up</h2>
            <signup />
            <p>😁   <span @click="displayLogin = true">click me if you already have account</span> </p>
      </div>
      
      
      
    
  </div>
</template>

<script>
import signup from '../components/signup.vue'
import login from '../components/LoginForm.vue'
import {ref} from 'vue'
export default {
    components:{ signup, login
    },
    setup()
    {
        const displayLogin = ref(true)
        return {displayLogin}
    }
   
  
}
</script>

<style>
.header{
    text-align: center;
    padding: 20px 0;
    
}
.header span{
   display: block;
   margin:20px 10px;
   cursor: pointer;
   text-decoration: underline;
}
.header form
{
    width: 320px;
    margin: 50px auto;
}
.header input{
    padding: 10px;
    outline: none;
    
}
</style>