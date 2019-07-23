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
import AsideComponent from './layout/Aside'
import FooterComponent from './layout/Footer'
import HeaderComponent from './layout/Header'

export default {
  name: 'home-view',
  components: {
    AsideComponent,
    FooterComponent,
    HeaderComponent
  }
}
</script>

<style>
.action-btn {
  margin: 0px 3px;
}
</style>
