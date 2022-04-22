<template>
    <v-card elevation="2" width="500" style="padding:30px">
      <SignupForm></SignupForm>
    </v-card>
</template>

<script>
import SignupForm from "@/components/RegisterForm.vue";

export default {
  name: "HomeView",
  components: {
    SignupForm,
  },
};
</script>
