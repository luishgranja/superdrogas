<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Products
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Products
        </li>
      </ol>
    </section>
    <p>{{getNumberOfProducts}} products</p>
    <section class="content">
      <div class="row">
        <div class="col-sm-12">
          <div class="box">
            <div class="box-body">
              <table id="table" class="table table-bordered table-striped" >
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Brand</th>
                    <th>Price</th>            
                    <th>Image</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(product, index) in activeProducts" :key="index">
                    <td>{{product.name}}</td>
                    <td>{{product.brand}}</td>
                    <td>${{product.price}}</td>
                    <td class="text-center">
                      <a
                        @click="getProduct(product.id)"
                        class="btn.btn-app btn-info btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#product-detail"
                      >
                        <i class="fa fa-info-circle"></i>
                      </a>
                    <td><button @click='addToCart(product)' class='button is-info'>Add to cart</button></td>
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
import { mapState, mapGetters, mapActions } from 'vuex'
import ProductDetail from '@/components/admin/board/apps/products/modals/ProductsDetail'
export default {
  name: 'product',
  components: {
    ProductDetail    
  },
  computed: {
    //...mapState('products', [
    //  'products'
    //]),
    ...mapGetters('products', [
      'activeProducts',
      'numberProducts'
    ])
  },
  methods: {
    ...mapActions('ecommerce', [
      'addToCart'
    ])
  },
  created () {
    this.getProducts()
  },
}
</script>
