<template>
   <nav class="nav has-shadow" style='box-shadow: 0 1px 0 rgba(219,219,219,.3);'>

      <!-- This "nav-menu" is hidden on mobile -->
      <!-- Add the modifier "is-active" to display it on mobile -->
      <div class="row">
        <div class="col-sm-6">
          <router-link :to="{ name: 'product' }" 
            class="btn btn-block btn-primary btn-lg"> Shop
          </router-link>
        </div>
        <div class="col-sm-6">
          <router-link :to="{ name: 'cart' }"                          
            class="btn btn-block btn-primary btn-lg">
            <span class="icon">
              <i class="fa fa-shopping-cart"></i>
            </span> Checkout ({{itemsOnCart}})
          </router-link>
        </div>          
      </div>                    
   </nav>
</template>

<style>
.nav {
    height: auto;
    margin-bottom: 2rem;
}
.nav-item img {
    max-height: 3.5rem;
}
.active-bottom-border {
    border-bottom: 3px solid #00d1b2;
    color: #00d1b2;
    padding-bottom: calc(.75rem - 8px);
}
</style>

<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters('ecommerce', [
      'itemsOnCart'
    ])
  }
}
</script>
