<template>
  <div class="row">
    <div class="col-sm-offset-1 col-sm-4">
      <h1 class="text-center section-title">Login</h1>
      <form @submit.prevent="formHandler()">
        <div class="row">
          <input-component
            id="username_login"
            v-model="user.username"
            placeholder="Username"
            :label="false"
            :inputErrors="errors.username"
          >
            <span class="glyphicon glyphicon-user form-control-feedback"></span>
          </input-component>
          <input-component
            id="password_login"
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
        </div>
      </form>
    </div>
    <div class="col-sm-offset-2 col-sm-4">
      <h1 class="text-center section-title">Sign Up</h1>
      <form @submit.prevent="formHandler()">
        <div class="row">
          <input-component
            id="username"
            class="col-md-6"
            v-model="username"
            placeholder="Username"
            :label="false"
            :inputErrors="errors.username"
          >
            <span class="glyphicon glyphicon-user form-control-feedback"></span>
          </input-component>
          <input-component
            id="identification_number"
            class="col-md-6"
            v-model="identification_number"
            placeholder="Identification number"
            :label="false"
            :inputErrors="errors.identification_number"
          >
            <span class="glyphicon glyphicon-th-large form-control-feedback"></span>
          </input-component>
          <input-component
            id="email"
            class="col-md-12"
            v-model="email"
            placeholder="Email"
            type="email"
            :label="false"
            :inputErrors="errors.email"
          >
            <span class="glyphicon glyphicon-envelope form-control-feedback"></span>
          </input-component>
          <input-component
            id="first_name"
            class="col-md-6"
            v-model="firstName"
            placeholder="First name"
            :label="false"
            :inputErrors="errors.first_name"
          >
            <span class="glyphicon glyphicon-edit form-control-feedback"></span>
          </input-component>
          <input-component
            id="last_name"
            class="col-md-6"
            v-model="lastName"
            placeholder="Last name"
            :label="false"
            :inputErrors="errors.last_name"
          >
            <span class="glyphicon glyphicon-edit form-control-feedback"></span>
          </input-component>
          <input-component
            id="phone"
            class="col-md-6"
            v-model="phone"
            placeholder="Phone"
            :label="false"
            :inputErrors="errors.phone"
          >
            <span class="glyphicon glyphicon-earphone form-control-feedback"></span>
          </input-component>
          <input-component
            id="address"
            class="col-md-6"
            v-model="address"
            placeholder="Address"
            :label="false"
            :inputErrors="errors.address"
          >
            <span class="glyphicon glyphicon-send form-control-feedback"></span>
          </input-component>
          <input-component
            id="password"
            class="col-md-6"
            v-model="password"
            placeholder="Password"
            type="password"
            :label="false"
            :inputErrors="errors.password"
          >
            <span class="glyphicon glyphicon-lock form-control-feedback"></span>
          </input-component>
          <input-component
            id="password_confirmation"
            class="col-md-6"
            v-model="passwordConfirmation"
            placeholder="Password confirmation"
            type="password"
            :label="false"
            :inputErrors="errors.password_confirmation"
          >
            <span class="glyphicon glyphicon-lock form-control-feedback"></span>
          </input-component>
        </div>
        <div class="pull-right">
          <button type="submit" class="btn bg-navy btn-block">
            Sign Up
            <i class="fa fa-user-plus"></i>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'login-signup-ecommerce',
  data () {
    return {
      user_login: {
        username: '',
        password: ''
      },
      errors_login: {}
    }
  },
  computed: {
    ...mapState('users', [
      'user',
      'errors'
    ]),
    username: {
      get () {
        return this.user.username
      },
      set (value) {
        this.$store.commit('users/SET_USERNAME', value)
      }
    },
    firstName: {
      get () {
        return this.user.first_name
      },
      set (value) {
        this.$store.commit('users/SET_FIRST_NAME', value)
      }
    },
    lastName: {
      get () {
        return this.user.last_name
      },
      set (value) {
        this.$store.commit('users/SET_LAST_NAME', value)
      }
    },
    email: {
      get () {
        return this.user.email
      },
      set (value) {
        this.$store.commit('users/SET_EMAIL', value)
      }
    },
    phone: {
      get () {
        return this.user.phone
      },
      set (value) {
        this.$store.commit('users/SET_PHONE', value)
      }
    },
    address: {
      get () {
        return this.user.address
      },
      set (value) {
        this.$store.commit('users/SET_ADDRESS', value)
      }
    },
    identification_number: {
      get () {
        return this.user.identification_number
      },
      set (value) {
        this.$store.commit('users/SET_IDENTIFICATION_NUMBER', value)
      }
    },
    password: {
      get () {
        return this.user.password
      },
      set (value) {
        this.$store.commit('users/SET_PASSWORD', value)
      }
    },
    passwordConfirmation: {
      get () {
        return this.user.password_confirmation
      },
      set (value) {
        this.$store.commit('users/SET_PASSWORD_CONFIRMATION', value)
      }
    }
  },
  methods: {
    ...mapActions('authentication', [
      'login'
    ]),
    async formHandler () {
      this.errors_login = await this.login(this.user_login)
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
