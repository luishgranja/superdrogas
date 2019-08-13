<template>
  <modal-component id="batch-form" :title="`${ isNewBatch ? 'Create' : 'Update' } batch`">
    <form>
      <div class="row">
        <div class="form-group col-sm-6">
          <label>Product</label>
          <select2
            :options="activeProducts"
            v-model="product"
          >
          </select2>
        </div>
        <input-component
          class="col-sm-6"
          v-model="quantity"
          id="quantity"
          placeholder="Quantity"
          :inputErrors="errors.quantity"
        />
        <input-component
          class="col-sm-6"
          v-model="manufacturing_date"
          id="manufacturing_date"
          placeholder="Manufacturing Date"
          type="date"
          :inputErrors="errors.manufacturing_date"
        />
        <input-component
          class="col-sm-6"
          v-model="expiration_date"
          id="expiration_date"
          placeholder="Expiration Date"
          type="date"
          :inputErrors="errors.expiration_date"
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
    ...mapGetters('products', [
      'activeProducts'
    ]),
    product: {
      get () {
        return this.batch.product
      },
      set (value) {
        this.$store.commit('batches/SET_PRODUCT', value)
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
    ]),
    ...mapActions('products', [
      'getProducts'
    ])
  },
  created () {
    this.getProducts()
  }
}
</script>
