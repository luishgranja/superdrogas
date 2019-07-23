<template>
  <div class="text-center">
    <h1>Insert here you are awesome Landing Page</h1>
    <router-link
      :to="{ name: 'home' }"
      class="btn btn-success"
    >
      Home
    </router-link>
    <router-link
      :to="{ name: 'login' }"
      class="btn btn-primary"
    >
      Login
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'landing-page'
}
</script>
