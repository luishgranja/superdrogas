<template>
  <aside class="main-sidebar">
    <section class="sidebar">
      <ul class="sidebar-menu" data-widget="tree">
        <li class="header" style="font-size: 20px; padding: 15px 25px;">Navigation</li>
        <li>
          <router-link :to="{ name: 'home' }">
            <i class="fa fa-home"></i>
            <span>Home</span>
          </router-link>
        </li>
        <li class="treeview">
          <a>
            <i class="fa fa-users"></i>
            <span>Accounts</span>
            <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span>
          </a>
          <ul class="treeview-menu">
            <li>
              <router-link :to="{ name: 'users' }">
                <i class="fa fa-user"></i>
                <span>Users</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{}">
                <i class="fa fa-child"></i>
                <span>Customer</span>
              </router-link>
            </li>
          </ul>
        </li>
        <li class="treeview">
          <a>
            <i class="fa fa-cubes"></i>
            <span>Inventory</span>
            <span class="pull-right-container">
              <i class="fa fa-angle-left pull-right"></i>
            </span>
          </a>
          <ul class="treeview-menu">
            <li>
              <router-link :to="{ name: 'batches' }">
                <i class="fa fa-building"></i>
                <span>Batches</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{}">
                <i class="fa fa-trademark"></i>
                <span>Brands</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{}">
                <i class="fa fa-tag"></i>
                <span>Categories</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'products' }">
                <i class="fa fa-cube"></i>
                <span>Products</span>
              </router-link>
            </li>
          </ul>
        </li>
      </ul>
    </section>
  </aside>
</template>

<script>
export default {
  name: 'aside-component'
}
</script>
