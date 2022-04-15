<template>

<label style="padding-left:430px">😎</label>
 <label style="padding-right:10px"></label>
   <select v-model="role">
     <option value="option1">选项1</option>
     <option value="option2">选项2</option>
   </select>

  <form @submit.prevent="handle"> 
    <label>UserName:</label>
   <input type="UserName" required  placeholder="name" v-model="UserName">
   <label>Password:</label>
   <input type="Password" required placeholder = "Password" v-model="Password">


   <br>
   <div class ="submit">
     <button>Login</button>
   </div>

  
  </form> 
  
  <!-- testing -->
  <!-- <p>UserName:{{UserName}}</p>
  <p>Password:{{Password}}</p> -->
</template> 

<script>
import {ref} from 'vue'
export default {
  setup()
  {
      const UserName = ref('')
      const Password = ref('')
      const handle =() =>{
        console.log(UserName.value,Password.value)
      }
      return{UserName, Password,handle}

  },
  data()
  {
    return{
      // PasswordError: '',
      // UserName:'', 
      // Password:'',
      role: ''
    }
  },
  // methods:
  // {
  //   handle()
  //   {
  //     // console.log('submitting')
  //     this.PasswordError = this.Password.length>3 ? '':' password must be at least 4 char long'

  //   }
  // }

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

