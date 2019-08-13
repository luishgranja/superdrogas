<template>
  <modal-component id="brand-form" :title="`${ isNewBrand ? 'Create' : 'Update' } brand`">
    <form>
      <div class="row">
        <input-component
          class="col-md-6"
          id="name"
          v-model="name"
          placeholder="Name"
          :inputErrors="errors.name"
        />
        <input-component
          class="col-md-6"
          id="phone"
          v-model="phone"
          placeholder="Phone"
          :inputErrors="errors.phone"
        />
        <input-component
          class="col-md-12"
          id="email"
          v-model="email"
          placeholder="Email"
          type="email"
          :inputErrors="errors.email"
        />
      </div>
      <div class="pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button v-if="isNewBrand" @click="createBrand($event)" type="submit" class="btn btn-success">Create</button>
        <button v-else @click="updateBrand($event)" type="submit" class="btn btn-primary">Update</button>
      </div>
    </form>
  </modal-component>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'brand-form',
  computed: {
    ...mapState('brands', [
      'brand',
      'errors'
    ]),
    ...mapGetters('brands', [
      'isNewBrand'
    ]),
    name: {
      get () {
        return this.brand.name
      },
      set (value) {
        this.$store.commit('brands/SET_NAME', value)
      }
    },
    email: {
      get () {
        return this.brand.email
      },
      set (value) {
        this.$store.commit('brands/SET_EMAIL', value)
      }
    },
    phone: {
      get () {
        return this.brand.phone
      },
      set (value) {
        this.$store.commit('brands/SET_PHONE', value)
      }
    }
  },
  methods: {
    ...mapActions('brands', [
      'createBrand',
      'updateBrand'
    ])
  }
}
</script>
