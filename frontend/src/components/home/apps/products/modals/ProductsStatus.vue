<template>
  <modal-component
    id="product-status"
    :title="`${ product.is_active ? 'Deactivate' : 'Activate' } product`"
  >
    <div class="row">
      <div class="col-sm-12">
        <p>
          Are you sure to
          <strong>{{ product.is_active ? 'deactivate' : 'activate' }}</strong>
          the product
          <strong>{{ product.name }} </strong>?
        </p>
      </div>
    </div>
    <div class="pull-right">
      <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
      <button
        @click="deleteProduct"
        :class="`${ product.is_active ? 'btn-danger' : 'btn-success' }`"
        class="btn"
        type="submit"
      >
        {{ product.is_active ? 'Deactivate' : 'Activate' }}
      </button>
    </div>
  </modal-component>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'product-status',
  computed: {
    ...mapState('products', [
      'product'
    ])
  },
  methods: {
    ...mapActions('products', [
      'deleteProduct'
    ])
  }
}
</script>
