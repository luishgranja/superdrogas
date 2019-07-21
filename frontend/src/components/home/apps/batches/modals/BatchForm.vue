<template>
  <modal-component id="batch-form" :title="`${ isNewBatch ? 'Create' : 'Update' } batch`">
    <form>
      <div class="row">
        <select name="product" id="product">
          <option v-forvalue=""></option>

        </select>
        <input-component
          v-model="quantity"
          id="quantity"
          label="Quantity"
          :erros="errors.quantity"
        />
        <input-component
          v-model="manufacturing_date"
          id="manufacturingDate"
          label="Manufacturing Date"
          type="date"
          :erros="errors.manufacturing_date"
        />
        <input-component
          v-model="expiration_date"
          id="expirationDate"
          label="Expiration Date"
          type="date"
          :erros="errors.expiration_date"
        />

      </div>
      <div class="pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button v-if="isNewBatch" @click="createBatch($event)" type="submit" class="btn btn-success">Create</button>
        <button v-else @click="updateBatch($event)" type="submit" class="btn btn-primary">Update</button>
      </div>
    </form>
  </modal-component>
</template>

<script>
  /* eslint-disable eol-last */
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'batch-form',
  computed: {
    ...mapState('batches', [
      'batch',
      'errors'
    ]),
    ...mapGetters('batches', [
      'isNewBatch'
    ]),
    product: {
      get () {
        return this.batch.product
      },
      set (value) {
        this.$store.commit('users/SET_PRODUCT', value)
      }
    },
    quantity: {
      get () {
        return this.batch.quantity
      },
      set (value) {
        this.$store.commit('batches/SET_QUANTITY', value)
      }
    },
    manufacturing_date: {
      get () {
        return this.batch.manufacturing_date
      },
      set (value) {
        this.$store.commit('batches/SET_MANUFACTURING_DATE', value)
      }
    },
    expiration_date: {
      get () {
        return this.batch.expiration_date
      },
      set (value) {
        this.$store.commit('batches/SET_EXPIRATION_DATE', value)
      }
    }
  },
  methods: {
    ...mapActions('batches', [
      'createBatch',
      'updateBatch'
    ])
  }
}
</script>
