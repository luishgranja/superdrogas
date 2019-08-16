<template>
  <div class="container">
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from '@/components/ecommerce/NavBar.vue'

export default {
  name: 'shopping',
  components: {
    NavBar
  }
}
</script>
