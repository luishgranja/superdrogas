<template>
  <aside class="main-sidebar">
    <section class="sidebar">
      <ul class="sidebar-menu" data-widget="tree">
        <li class="header" style="font-size: 20px; padding: 15px 25px;">Navigation</li>
        <li
          @click="updateApp('home')"
          :class="`${ app === 'home' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'home' }">
            <i class="fa fa-home"></i>
            <span>Home</span>
          </router-link>
        </li>
        <li
          :class="`${ module === 'accounts' ? 'active' : '' }`"
          class="treeview"
        >
          <a>
            <i class="fa fa-users"></i>
            <span>Accounts</span>
            <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span>
          </a>
          <ul class="treeview-menu">
            <li
              @click="updateApp('users')"
              :class="`${ app === 'users' ? 'active' : '' }`"
            >
              <router-link :to="{ name: 'users' }">
                <i class="fa fa-user"></i>
                <span>Users</span>
              </router-link>
            </li>
            <li
              @click="updateApp('customers')"
              :class="`${ app === 'customers' ? 'active' : '' }`"
            >
              <router-link :to="{ name: 'customers' }">
                <i class="fa fa-child"></i>
                <span>Customers</span>
              </router-link>
            </li>
          </ul>
        </li>
        <li
          v-if="isAdmin"
          @click="updateApp('tenants')"
          :class="`${ app === 'tenants' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'tenants' }">
            <i class="fa fa-medkit"></i>
            <span>Tenants</span>
          </router-link>
        </li>
        <li
          v-if="isAdmin"
          @click="updateApp('metrics')"
          :class="`${ app === 'metrics' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'metrics' }">
            <i class="fa fa-area-chart"></i>
            <span>Metrics</span>
          </router-link>
        </li>
        <li
          v-if="!isAdmin"
          :class="`${ module === 'inventory' ? 'active' : '' }`"
          class="treeview"
        >
          <a>
            <i class="fa fa-cubes"></i>
            <span>Inventory</span>
            <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span>
          </a>
          <ul class="treeview-menu">
            <li
              @click="updateApp('batches')"
              :class="`${ app === 'batches' ? 'active' : '' }`"
            >
              <router-link :to="{ name: 'batches' }">
                <i class="fa fa-building"></i>
                <span>Batches</span>
              </router-link>
            </li>
            <li
              @click="updateApp('brands')"
              :class="`${ app === 'brands' ? 'active' : '' }`"
            >
              <router-link :to="{ name: 'brands' }">
                <i class="fa fa-trademark"></i>
                <span>Brands</span>
              </router-link>
            </li>
            <li
              @click="updateApp('categories')"
              :class="`${ app === 'categories' ? 'active' : '' }`"
            >
              <router-link :to="{ name: 'categories' }">
                <i class="fa fa-tag"></i>
                <span>Categories</span>
              </router-link>
            </li>
            <li
              @click="updateApp('products')"
              :class="`${ app === 'products' ? 'active' : '' }`"
            >
              <router-link :to="{ name: 'products' }">
                <i class="fa fa-cube"></i>
                <span>Products</span>
              </router-link>
            </li>
          </ul>
        </li>
        <li
          v-if="!isAdmin"
          @click="updateApp('reports')"
          :class="`${ app === 'reports' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'reports' }">
            <i class="fa fa-bar-chart"></i>
            <span>Reports</span>
          </router-link>
        </li>
        <li
          v-if="!isAdmin"
          @click="updateApp('sales')"
          :class="`${ app === 'sales' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'sales' }">
            <i class="fa fa-money"></i>
            <span>Sales</span>
          </router-link>
        </li>
        <li
          v-if="!isAdmin"
          @click="updateApp('configurations')"
          :class="`${ app === 'configurations' ? 'active' : '' }`"
        >
          <router-link :to="{ name: 'configurations' }">
            <i class="fa fa-cog"></i>
            <span>Configurations</span>
          </router-link>
        </li>
      </ul>
    </section>
  </aside>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'aside-component',
  computed: {
    ...mapState('app', [
      'isAdmin',
      'app'
    ]),
    ...mapGetters('app', [
      'module'
    ])
  },
  methods: {
    ...mapActions('app', [
      'updateApp'
    ])
  },
  mounted () {
    this.updateApp(this.$route.matched[2].name)
  }
}
</script>
