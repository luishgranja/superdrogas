<template>
  <div class="row">
    <div class="col-sm-offset-4 col-sm-4">
      <h1 class="text-center section-title">Login</h1>
      <form @submit.prevent="formHandler()">
        <input-component
          id="username"
          v-model="user.username"
          placeholder="Username"
          :label="false"
          :inputErrors="errors.username"
        >
          <span class="glyphicon glyphicon-user form-control-feedback"></span>
        </input-component>
        <input-component
          id="password"
          v-model="user.password"
          placeholder="Password"
          :label="false"
          type="password"
          :inputErrors="errors.password"
        >
          <span class="glyphicon glyphicon-lock form-control-feedback"></span>
        </input-component>
        <div class="row footer">
          <router-link
            :to="{ name: 'password-reset' }"
            class="col-md-6 fp"
          >
            I forgot my password
          </router-link>
          <div class="col-md-6 pull-right">
            <button type="submit" class="btn bg-navy btn-block">
              Login
              <i class="fa fa-sign-in"></i>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'login-ecommerce',
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
.section-title {
  margin: 40px 0px;
  font-size: 40px;
}
</style>
