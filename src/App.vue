<template>
<div class = "header">
<p>Welcome</p>
<div v-if="show">
  <h2>Login</h2>
  <login />
  <p>no account yet<span @click="show = false" >Signup</span>instead</p>
</div>
<div v-else>
  <h2>Signup</h2>
 <signup />
</div>
 </div> 
  
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import signup from './components/signup.vue'
import login from './components/login.vue'


export default {
  name: 'App',
  components: {signup,login},

  methods()
     {
      const show = ref(true)
       return {show}
     }
  }

</script> 

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0b0300;
  margin-top: 100px;
}
body{
  margin:0;
  background: rgb(241, 244, 244);
}
</style>

 
<!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->