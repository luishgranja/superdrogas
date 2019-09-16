<template>
  <div class="thumbnail">
    <img :src="product.image" :alt="product.name">
    <div class="caption">
      <h3>{{ product.name }}</h3>
      <h5 class="text-aqua">${{ product.price }}</h5>
      <p class="description">
        {{ product.description }}
      </p>
      <div class="text-center">
        <a href="" class="btn btn-primary">
          <i class="fa fa-cart-plus"></i>
          Add
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'product',
  props: {
    product: {
      type: Object,
      default: () => {}
    }
  }
}
</script>

<style scoped>
img {
  max-height: 200px;
  overflow: hidden;
}
.description {
  height: 30px;
}
</style>
