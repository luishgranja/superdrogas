<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Products
        </h1>
        <span class="badge bg-blue">{{numberProducts}} products</span>
      </div>
    </section>
    <section class="content">
      <div class="row">
        <div class="col-sm-12">
          <div class="box">
            <div class="box-body">
              <table
                id="table"
                class=" table-responsive table table-bordered table-striped"
              >
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Brand</th>
                    <th>Price</th>
                    <th>Image</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(product, index) in activeProductsCatalogue"
                    :key="index"
                  >
                    <td>{{ product.name }}</td>
                    <td>{{ product.brand }}</td>
                    <td>${{ product.price}}</td>
                    <td>
                      <img
                        class="image"
                        :src="product.image"
                        alt="Product image"
                        width="100%"
                        height="100%"
                      >
                    </td>
                    <td class="text-center">
                      <a
                        @click="getProduct(product.id)"
                        class="btn.btn-app btn-primary btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#product-detail"
                      >
                        <i class="fa fa-info-circle"></i>
                      </a>
                      <button
                        type="button"
                        @click='addToCart(product)'
                        class="btn btn-primary btn-flat"
                      >
                        <i class="fa fa-fw fa-plus"></i>
                        Add to cart
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>
    <product-detail />
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import template from '@/utilities/template'
import ProductDetail from '@/components/admin/board/apps/products/modals/ProductsDetail'

export default {
  name: 'product',
  components: {
    ProductDetail
  },
  computed: {
    ...mapGetters('products', [
      'activeProductsCatalogue',
      'numberProducts'
    ])
  },
  methods: {
    ...mapActions('ecommerce', [
      'addToCart'
    ]),
    ...mapActions('products', [
      'getProducts',
      'getProduct'
    ])
  },
  created () {
    this.getProducts()
  },
  updated () {
    template.reload()
  }
}
</script>

<style scoped>
.image {
  width: 100px !important;
  height: 100px !important;
}
</style>
