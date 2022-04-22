<template>
    <v-card elevation="2" width="500" style="padding:30px">
      <LoginForm></LoginForm>
    </v-card>
</template>

<script>
import LoginForm from "@/components/LoginForm.vue";

export default {
  name: "LoginView",
  components: {
    LoginForm,
  },
};
</script>
