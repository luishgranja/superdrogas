<template>
  <vuestic-layout v-layout>
    <app-navbar
      :isOpen="opened"
      @toggle-menu="toggleSidebar"
    />
    <app-sidebar
      :isOpen="opened"
      @toggle-menu="toggleSidebar"
    />
    <main
      slot="content"
      id="content"
      class="content va-layout gutter--lg fluid"
      role="main"
    >
      <app-breadcrumbs />
      <vuestic-pre-loader
        v-show="isLoading"
        class="pre-loader"
      />
      <router-view />
    </main>
    <span slot="footer">
      ©2019. Made by
      <router-link :to="{ name: 'dashboard' }">Superdrogas</router-link>
    </span>
  </vuestic-layout>
</template>

<script>
import { mapGetters } from 'vuex'

import Layout from '@/vuestic-theme/vuestic-directives/Layout'
import VuesticLayout from '@/vuestic-theme/vuestic-components/vuestic-layout/VuesticLayout'

import AppBreadcrumbs from './app-breadcrumbs/AppBreadcrumbs'
import AppNavbar from './app-navbar/AppNavbar'
import AppSidebar from './app-sidebar/AppSidebar'

export default {
  name: 'app-layout',
  components: {
    VuesticLayout,
    AppBreadcrumbs,
    AppNavbar,
    AppSidebar
  },
  directives: {
    layout: Layout
  },
  data () {
    return {
      opened: true
    }
  },
  methods: {
    toggleSidebar (opened) {
      this.opened = opened
    }
  },
  computed: {
    ...mapGetters(['isLoading'])
  }
}
</script>
