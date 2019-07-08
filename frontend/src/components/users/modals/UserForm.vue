<template>
  <modal-component
    id="user-form"
    :title="`${ newUser ? 'Create' : 'Update' } user`"
  >
    <form>
      <div class="row">
        <input-component
          v-model="username"
          id="username"
          label="Username"
          :erros="errorList.username"
        />
        <input-component
          v-model="email"
          id="email"
          label="Email"
          type="email"
          :erros="errorList.email"
        />
        <input-component
          v-model="firstName"
          id="firstName"
          label="First name"
          :erros="errorList.first_name"
        />
        <input-component
          v-model="lastName"
          id="lastName"
          label="Last name"
          :erros="errorList.last_name"
        />
        <input-component
          v-model="password"
          id="password"
          label="Password"
          type="password"
          :erros="errorList.password"
        />
        <input-component
          v-model="passwordConfirmation"
          id="passwordConfirmation"
          label="Password confirmation"
          type="password"
          :erros="errorList.password_confirmation"
        />
      </div>
      <div class="pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button v-if="newUser" @click="createUser($event)" type="submit" class="btn btn-success">Create</button>
        <button v-else @click="updateUser($event)" type="submit" class="btn btn-primary">Update</button>
      </div>
    </form>
  </modal-component>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'create-user',
  computed: {
    ...mapState('users', [
      'errorList'
    ]),
    ...mapGetters('users', [
      'newUser'
    ]),
    username: {
      get () {
        return this.$store.state.users.currentUser.username
      },
      set (value) {
        this.$store.commit('users/SET_USERNAME', value)
      }
    },
    firstName: {
      get () {
        return this.$store.state.users.first_name
      },
      set (value) {
        this.$store.commit('users/SET_FIRST_NAME', value)
      }
    },
    lastName: {
      get () {
        return this.$store.state.users.currentUser.last_name
      },
      set (value) {
        this.$store.commit('users/SET_LAST_NAME', value)
      }
    },
    email: {
      get () {
        return this.$store.state.users.email
      },
      set (value) {
        this.$store.commit('users/SET_EMAIL', value)
      }
    },
    password: {
      get () {
        return this.$store.state.users.password
      },
      set (value) {
        this.$store.commit('users/SET_PASSWORD', value)
      }
    },
    passwordConfirmation: {
      get () {
        return this.$store.state.users.password_confirmation
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
