<template>
  <aside class="main-sidebar">
    <section class="sidebar">
      <ul class="sidebar-menu" data-widget="tree">
        <li
          @click="setApp('home')"
          :class="`${ app === 'home' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'home' }">
            <i class="fa fa-home"></i>
            <span>Home</span>
          </router-link>
        </li>
        <li
          @click="setApp('clients')"
          :class="`${ app === 'clients' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'users' }">
            <i class="fa fa-users"></i>
            <span>Users</span>
          </router-link>
        </li>
        <li
          @click="setApp('batches')"
          :class="`${ app === 'batches' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'batches' }">
            <i class="fa fa-cubes"></i>
            <span>Batches</span>
          </router-link>
        </li>
        <li
          @click="setApp('products')"
          :class="`${ app === 'products' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'products' }">
            <i class="fa fa-cube"></i>
            <span>Products</span>
          </router-link>
        </li>
      </ul>
    </section>
  </aside>
</template>

<script>
export default {
  name: 'aside-component',
  data () {
    return {
      app: ''
    }
  },
  methods: {
    setApp (newApp) {
      this.app = newApp
    }
  },
  mounted () {
    this.setApp(this.$route.matched[1].name)
  }
}
</script>
