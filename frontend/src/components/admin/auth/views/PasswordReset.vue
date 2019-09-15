<template>
  <div>
    <h1 class="text-center">
      Enter your email
    </h1>
    <form @submit.prevent="formHandler()">
      <input-component
        id="username"
        v-model="user.username"
        placeholder="Email"
        :label="false"
        :inputErrors="errors.username"
      >
        <span class="glyphicon glyphicon-envelope form-control-feedback"></span>
      </input-component>
      <div class="row footer">
        <div class="col-md-6 pull-right">
          <router-link
            :to="{ name: 'password-reset-new-password', params: { uid: '1', token: '2' } }"
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
  name: 'password-reset',
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
