<template>
  <div class="text-center">
    <h1>Landing Page</h1>
    <a
      :href="$router.resolve({ name: 'home' }).href"
      class="btn btn-lg btn-success"
    >
      Home
    </a>
    <router-link
      :to="{ name: 'login' }"
      class="btn btn-lg btn-primary"
    >
      Login
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'ecommerce'
}
</script>
