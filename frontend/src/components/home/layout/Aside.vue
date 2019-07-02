<template>
  <aside class="main-sidebar">
    <section class="sidebar">
      <ul class="sidebar-menu" data-widget="tree">
        <li class="active">
          <router-link :to="{ name: 'home' }">
            <i class="fa fa-home"></i>
            <span>Home</span>
          </router-link>
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
