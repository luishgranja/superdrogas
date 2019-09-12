<template>
  <div class="login-page">
    <div class="login-box">
      <div class="login-box-body">
        <h1 class="text-center">
          Enter your email
        </h1>
        <p>
            Your password is update! Go to
            <router-link :to="{ name: 'login' }">
                Login
            </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'login',
  data () {
    return {
      user: {
        username: '',
        password: ''
      },
      errors: {}
    }
  },
  methods: {
    ...mapActions('authentication', [
      'login'
    ]),
    async formHandler () {
      this.errors = await this.login(this.user)
    }
  }
}
</script>

<style scoped>
.login-page {
  background-image: url("~@/static/images/pharmacy.jpg");
  background-size: cover;
  display: flex;
  height: 100vh;
}
.fp {
  margin: 10px 0px;
}
.footer {
  padding-top: 10px;
}
</style>
