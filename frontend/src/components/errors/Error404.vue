<template>
  <div class="error-bg">
    <div class="error-page error-box">
      <h1 class="headline text-blue">404</h1>
      <div class="error-content">
        <h2>
          <i class="fa fa-warning text-blue"></i>
          Oops! Page not found.
        </h2>
        <p>
          We could not find the page you were looking for.
          Meanwhile, you may return to
          <router-link :to="{ name: 'landing' }">
            landing page.
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'error404'
}
</script>

<style>
.error-bg {
  display: flex;
  height: 100vh;
}
.error-box {
  margin: 10% auto;
}
.error-content {
  text-align: center;
}
</style>
