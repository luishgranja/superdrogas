<template>
  <div class="wrapper">
    <header-component />
    <aside-component />
    <div class="content-wrapper" style="min-height: 90vh;">
      <router-view />
    </div>
    <footer-component />
  </div>
</template>

<script>
import HeaderComponent from '@/views/home/layout/Header'
import AsideComponent from '@/views/home/layout/Aside'
import FooterComponent from '@/views/home/layout/Footer'

export default {
  name: 'home',
  components: {
    HeaderComponent,
    AsideComponent,
    FooterComponent
  }
}
</script>

<style>
.action-btn {
  margin: 0px 3px;
}
</style>
