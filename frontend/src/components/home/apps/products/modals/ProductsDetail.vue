<template>
  <modal-component id="product-detail" title="Product detail">
    <div class="row">
      <div class="col-sm-12">
        <ul>
          <li>
            <img :src="product.image" alt="Product image" width="100%" height="100%">
          </li>
          <li>
            <strong>Name:</strong>
            {{ product.name }}
          </li>
          <li>
            <strong>Description:</strong>
            {{ product.description }}
          </li>
          <li>
            <strong>Price:</strong>
            {{ product.price }}
          </li>
          <li>
            <strong>Category:</strong>
            {{ product.category }}
          </li>
          <li>
            <strong>Sku:</strong>
            {{ product.sku }}
          </li>
          <li>
            <strong>Weight:</strong>
            {{ product.weight }}
          </li>
          <li>
            <strong>Brand:</strong>
            {{ product.brand }}
          </li>
          <li>
            <strong>Status:</strong>
            {{ product.is_active ? 'Active' : 'Inactive' }}
          </li>
        </ul>
      </div>
    </div>
    <div class="pull-right">
      <button type="button" class="btn btn-info" data-dismiss="modal">Close</button>
    </div>
  </modal-component>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'product-detail',
  computed: {
    ...mapState('products', [
      'product'
    ])
  }
}
</script>
