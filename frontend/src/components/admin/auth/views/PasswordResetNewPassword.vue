<template>
  <div>
    <h1 class="text-center">
      New password
    </h1>
    <form @submit.prevent="formHandler()">
      <input-component
        id="username"
        v-model="user.username"
        placeholder="New password"
        :label="false"
        :inputErrors="errors.username"
      >
        <span class="glyphicon glyphicon-lock form-control-feedback"></span>
      </input-component>
      <input-component
        id="username"
        v-model="user.username"
        placeholder="Confirm new password"
        :label="false"
        :inputErrors="errors.username"
      >
        <span class="glyphicon glyphicon-lock form-control-feedback"></span>
      </input-component>
      <div class="row footer">
        <div class="col-md-6 pull-right">
          <router-link
            :to="{ name: 'password-reset-done' }"
            class="btn bg-navy btn-block"
          >
            Send
          </router-link>
        </div>
      </div>
    </form>
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
.fp {
  margin: 10px 0px;
}
.footer {
  padding-top: 10px;
}
</style>
