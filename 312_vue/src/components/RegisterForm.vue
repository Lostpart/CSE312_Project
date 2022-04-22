<template>
<div @keyup.enter="register">
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="displayName"
      :rules="nameRules"
      label="Display Name"
      required
    ></v-text-field>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

    <v-text-field
      v-model="password"
      label="Password"
      required
    ></v-text-field>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="register"
    >
      REGISTER
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Reset Form
    </v-btn>

  </v-form>
  </div>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      displayName: '',
      nameRules: [
        v => !!v || 'Display name is required',
        v => (v && v.length <= 20) || 'Display name must be less than 20 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      password: '',

    }),

    methods: {
      register () {
        console.log(this.email)
        console.log(this.password)
        console.log(this.displayName)
      },
      reset () {
        this.$refs.form.reset()
      },
    },
  }
</script>