<template>
  <modal-component id="batch-form" :title="`${ isNewBatch ? 'Create' : 'Update' } batch`">
    <form>
      <div class="row">
        <div class="form-group col-sm-6">
          <select v-model="product"  class="form-control select2" name="product" id="product"  style="width: 100%; height: 100%;">
            <option v-for="product in activeProducts":value="product.id" > {{ product.name }} </option>
          </select>
        </div>
        <input-component
          v-model="quantity"
          id="quantity"
          label="Quantity"
          :erros="errors.quantity"
        />
        <input-component
          v-model="manufacturing_date"
          id="manufacturing_date"
          label="Manufacturing Date"
          type="date"
          :erros="errors.manufacturing_date"
        />
        <input-component
          v-model="expiration_date"
          id="expiration_date"
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
    ]),
    updateProduct (value) {
        this.$store.commit('batches/SET_PRODUCT', value)
    }
  },
  created () {
    this.getProducts()
  },
}

$(document).ready(function() {
    $('.select2').select2();
});
</script>
