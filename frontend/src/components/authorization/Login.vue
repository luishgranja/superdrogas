<template>
  <div class="login-box">
    <div class="login-box-body">
      <h1 class="text-center">
        Login
      </h1>
      <form @submit.prevent="login()">
        <div
          v-if="errors.non_field_errors"
          class="alert alert-danger alert-dismissible"
        >
          <h4><i class="icon fa fa-ban"></i> Alert!</h4>
          {{ errors.non_field_errors[0] }}
        </div>
        <div :class="`${ errors.username ? 'has-error' : '' }`" class="form-group has-feedback is-empty">
          <input v-model="username" type="username" class="form-control" placeholder="Username" required>
          <span class="glyphicon glyphicon-user form-control-feedback"></span>
          <span v-for="(error, index) in errors.username" :key="index" class="help-block">
            {{ error }}
          </span>
        </div>
        <div :class="`${ errors.password ? 'has-error' : '' }`" class="form-group has-feedback is-empty">
          <input v-model="password" type="password" class="form-control" placeholder="Password" required>
          <span class="glyphicon glyphicon-lock form-control-feedback"></span>
          <span v-for="(error, index) in errors.password" :key="index" class="help-block">
            {{ error }}
          </span>
        </div>
        <div class="row">
          <a class="col-md-6 fp">
            <!-- I forgot my password -->
          </a>
          <div class="col-md-6 pull-right">
            <button type="submit" class="btn bg-navy btn-block">
              Login
              <i class="fa fa-sign-in"></i>
            </button>
          </div>
        </div>
      </form>
      <!-- <div class="text-center social-btns">
        <p>Or login with</p>
        <a class="btn btn-social-icon btn-google"><i class="fa fa-google"></i></a>
        <a class="btn btn-social-icon btn-facebook"><i class="fa fa-facebook"></i></a>
        <a class="btn btn-social-icon btn-twitter"><i class="fa fa-twitter"></i></a>
      </div> -->
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'login',
  computed: {
    ...mapState('authentication', [
      'user',
      'errors'
    ]),
    username: {
      get () {
        return this.user.username
      },
      set (value) {
        this.$store.commit('authentication/SET_USERNAME', value)
      }
    },
    password: {
      get () {
        return this.user.password
      },
      set (value) {
        this.$store.commit('authentication/SET_PASSWORD', value)
      }
    }
  },
  methods: {
    ...mapActions('authentication', [
      'login'
    ])
  }
}
</script>

<style>
body {
  background-image: url("~@/static/images/pharmacy.jpg");
  background-size: cover;
}
.fp {
  margin: 10px 0px;
}
.social-btns {
  margin-top: 20px;
}
.social-btns .btn {
  margin: 0px 5px;
}
</style>
