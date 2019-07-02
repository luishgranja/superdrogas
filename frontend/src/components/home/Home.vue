<template>
  <div class="wrapper">
    <header-component />
    <aside-component />
    <div class="content-wrapper" style="min-height: 90vh;">
      <router-view/>
    </div>
    <footer-component />
  </div>
</template>

<script>
import HeaderComponent from '@/components/home/layout/Header'
import AsideComponent from '@/components/home/layout/Aside'
import FooterComponent from '@/components/home/layout/Footer'

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
