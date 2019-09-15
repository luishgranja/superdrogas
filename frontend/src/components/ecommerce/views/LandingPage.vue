<template>
  <div class="container-fluid mt">
    <carousel></carousel>
    <div class="row">
      <h2 class="text-center section-title">
        Top products
      </h2>
      <div v-for="i in 6" :key="i" class="col-sm-2">
        <product></product>
      </div>
    </div>
  </div>
</template>

<script>
import Carousel from '@/components/ecommerce/components/Carousel'
import Product from '@/components/ecommerce/components/Product'

export default {
  name: 'shopping',
  components: {
    Carousel,
    Product
  }
}
</script>

<style scoped>
.mt {
  margin-top: 70px;
}
.section-title {
  margin: 40px 0px;
  font-size: 40px;
}
</style>
