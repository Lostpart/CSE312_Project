<template>
  <v-row justify="space-around">
    <v-card elevation="2" width="500" style="padding: 30px; margin-top: 120px">
      <LoginForm></LoginForm>
    </v-card>
  </v-row>
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
