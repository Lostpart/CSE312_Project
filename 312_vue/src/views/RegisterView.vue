<template>
  <v-row justify="space-around">
    <v-card elevation="2" width="500" style="padding: 30px; margin-top: 120px">
      <RegisterForm></RegisterForm>
    </v-card>
  </v-row>
</template>

<script>
import RegisterForm from "@/components/RegisterForm.vue";

export default {
  name: "RegisterView",
  components: {
    RegisterForm,
  },
};
</script>
