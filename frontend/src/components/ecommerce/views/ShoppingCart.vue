<template>
  <div class="row">
    <div class="col-sm-12">
      <section class="content-header">
        <div class="list-inline">
          <h1>Shopping cart</h1>
        </div>
      </section>
      <section>
        <div class="row">
          <div class="col-sm-12">
            <div class="box">
              <div class="box-body">
                <div v-if="emptyCart" class="text-center">
                  <img class="cart-empty-img" src="@/static/images/shopping-cart.png" alt="Cart">
                  <p>Your shopping cart is empty!</p>
                </div>
                <div v-else>
                  <table id="table" class="table table-bordered table-striped">
                    <thead>
                      <tr>
                        <th>Name</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Image</th>
                        <th>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(product, index) in cartProducts" :key="index">
                        <td>{{ product.name }}</td>
                        <td>${{ product.price }}</td>
                        <td>{{ product.quantity }}</td>
                        <td class="text-center">
                          <img class="product-img" :src="product.image" alt="Product">
                        </td>
                        <td class="text-center">
                          <a @click="deleteFromCart(product)" class="btn.btn-app btn-danger btn-sm action-btn">
                            <i class="fa fa-minus-square"></i>
                          </a>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <div class="pull-right">
                    Total: <strong>${{ total }}</strong>
                    <button @click="checkout($event)" class="btn btn-primary btn-flat pull-rigth">
                      <i class="fa fa-credit-card"></i>
                      Checkout
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import template from '@/utilities/template'

export default {
  name: 'shopping-cart',
  computed: {
    ...mapGetters('ecommerce', [
      'cartProducts',
      'emptyCart'
    ]),
    total () {
      return this.cartProducts.reduce((total, p) => {
        return total + p.price * p.quantity
      }, 0)
    }
  },
  methods: {
    ...mapActions('ecommerce', [
      'deleteFromCart',
      'checkout'
    ])
  },
  mounted () {
    template.reload()
  },
  updated () {
    this.$nextTick(() => { template.reload() })
  }
}
</script>

<style scoped>
.cart-empty-img {
  height: 250px;
}
.product-img {
  height: 80px;
}
</style>
