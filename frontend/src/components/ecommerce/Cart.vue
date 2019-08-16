<template>
  <div class="cart">
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Your Shopping Cart
        </h1>
      </div>
    </section>
    <div v-if='emptyCart'>
      <div class="box box-default">
        <div class="box-body">
          <img
            class="img-responsive"
            src="@/static/images/cart-empty.jpg"
            alt="Empty Cart"
            width="100%"
            height="100%"
          >
        </div>
      </div>
    </div>
    <div v-else>
      <section class="content">
        <div class="row">
          <div class="col-sm-12">
            <div class="box">
              <div class="box-body">
                <table
                  id="table"
                  class="table table-bordered table-striped"
                  v-show="itemsOnCart"
                >
                  <thead>
                    <tr>
                      <th>Name</th>
                      <th>Price</th>
                      <th>Quantity</th>
                      <th>Delete</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(p, index) in cartProducts"
                      :key="index"
                    >
                      <td>{{ p.name }}</td>
                      <td>${{ p.price }}</td>
                      <td>{{ p.quantity }}</td>
                      <td class="text-center">
                        <a
                          @click="getProduct(p.id)"
                          class="btn.btn-app btn-primary btn-sm action-btn"
                          data-toggle="modal"
                          data-target="#product-detail"
                        >
                          <i class="fa fa-info-circle"></i>
                        </a>
                        <a
                          @click="deleteFromCart(p)"
                          class="btn.btn-app btn-danger btn-sm action-btn"
                        >
                          <i class="fa fa-minus-square"></i>
                        </a>
                      </td>
                    </tr>
                    <tr>
                      <td><b>Total:</b></td>
                      <td></td>
                      <td><b>${{ total }}</b></td>
                    </tr>
                  </tbody>
                </table>
                <button
                  v-show="itemsOnCart"
                  type="submit"
                  @click='checkout($event)'
                  class="btn btn-primary btn-flat"
                >
                  <i class="fa fa-credit-card"></i>
                  Checkout
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
      <product-detail />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ProductDetail from '@/components/admin/board/apps/products/modals/ProductsDetail'

export default {
  name: 'cart',
  components: {
    ProductDetail
  },
  computed: {
    ...mapGetters('ecommerce', [
      'cartProducts',
      'itemsOnCart',
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
    ]),
    ...mapActions('products', [
      'getProduct'
    ])
  }
}
</script>
