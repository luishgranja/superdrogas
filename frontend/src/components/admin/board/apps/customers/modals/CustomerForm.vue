<template>
  <modal-component id="user-form" :title="`${ isNewUser ? 'Create' : 'Update' } customer`">
    <form>
      <div class="row">
        <input-component
          id="username"
          class="col-md-6"
          v-model="username"
          placeholder="Username"
          :inputErrors="errors.username"
        />
        <input-component
          id="identification_number"
          class="col-md-6"
          v-model="identification_number"
          placeholder="Identification number"
          :inputErrors="errors.identification_number"
        />
        <input-component
          id="email"
          class="col-md-12"
          v-model="email"
          placeholder="Email"
          type="email"
          :inputErrors="errors.email"
        />
        <input-component
          id="first_name"
          class="col-md-6"
          v-model="firstName"
          placeholder="First name"
          :inputErrors="errors.first_name"
        />
        <input-component
          id="last_name"
          class="col-md-6"
          v-model="lastName"
          placeholder="Last name"
          :inputErrors="errors.last_name"
        />
        <input-component
          id="phone"
          class="col-md-6"
          v-model="phone"
          placeholder="Phone"
          :inputErrors="errors.phone"
        />
        <input-component
          id="address"
          class="col-md-6"
          v-model="address"
          placeholder="Address"
          :inputErrors="errors.address"
        />
        <input-component
          id="password"
          class="col-md-6"
          v-if="isNewUser"
          v-model="password"
          placeholder="Password"
          type="password"
          :inputErrors="errors.password"
        />
        <input-component
          id="password_confirmation"
          class="col-md-6"
          v-if="isNewUser"
          v-model="passwordConfirmation"
          placeholder="Password confirmation"
          type="password"
          :inputErrors="errors.password_confirmation"
        />
      </div>
      <div class="pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button v-if="isNewUser" @click="createCustomer($event)" type="submit" class="btn btn-success">Create</button>
        <button v-else @click="updateCustomer($event)" type="submit" class="btn btn-primary">Update</button>
      </div>
    </form>
  </modal-component>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'customer-form',
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
    ...mapActions('users', [
      'createUser',
      'updateUser'
    ]),
    createCustomer (event) {
      this.$store.commit('users/SET_ROL', 'CM')
      this.createUser(event)
    },
    updateCustomer (event) {
      this.$store.commit('users/SET_ROL', 'CM')
      this.updateUser(event)
    }
  }
}
</script>
