<template>
  <div class="login-page">
    <div class="login-box">
      <div class="login-box-body">
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
              <!-- <button type="submit" class="btn bg-navy btn-block">
                Send
                <i class="fa fa-sign-in"></i>
              </button> -->
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
