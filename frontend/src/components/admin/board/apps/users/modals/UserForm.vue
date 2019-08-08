<template>
  <modal-component id="user-form" :title="`${ isNewUser ? 'Create' : 'Update' } user`">
    <form>
      <div class="row">
        <input-component
          v-model="username"
          id="username"
          label="Username"
          :erros="errors.username"
        />
        <input-component
          v-model="email"
          id="email"
          label="Email"
          type="email"
          :erros="errors.email"
        />
        <input-component
          v-model="firstName"
          id="firstName"
          label="First name"
          :erros="errors.first_name"
        />
        <input-component
          v-model="lastName"
          id="lastName"
          label="Last name"
          :erros="errors.last_name"
        />
        <input-component
          v-if="isNewUser"
          v-model="password"
          id="password"
          label="Password"
          type="password"
          :erros="errors.password"
        />
        <input-component
          v-if="isNewUser"
          v-model="passwordConfirmation"
          id="passwordConfirmation"
          label="Password confirmation"
          type="password"
          :erros="errors.password_confirmation"
        />
      </div>
      <div class="pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button v-if="isNewUser" @click="createUser($event)" type="submit" class="btn btn-success">Create</button>
        <button v-else @click="updateUser($event)" type="submit" class="btn btn-primary">Update</button>
      </div>
    </form>
  </modal-component>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'user-form',
  computed: {
    ...mapState('users', [
      'user',
      'errors'
    ]),
    ...mapGetters('users', [
      'isNewUser'
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
    ...mapActions('users', [
      'createUser',
      'updateUser'
    ])
  }
}
</script>
