<template>
  <div class="login-page">
    <div class="login-box">
      <div class="login-box-body">
        <h1 class="text-center">
          Login
        </h1>
        <form>
          <div class="form-group has-feedback is-empty">
            <input type="username" class="form-control" placeholder="Username" required>
            <span class="glyphicon glyphicon-user form-control-feedback"></span>
          </div>
          <div class="form-group has-feedback is-empty">
            <input type="password" class="form-control" placeholder="Password" required>
            <span class="glyphicon glyphicon-lock form-control-feedback"></span>
          </div>
          <div class="row">
            <router-link :to="{}" class="col-md-6 fp">
              I forgot my password
            </router-link>
            <div class="col-md-6 pull-right">
              <button type="submit" class="btn bg-navy btn-block">
                Login
                <i class="fa fa-sign-in"></i>
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login'
}
</script>

<style scoped>
.login-page {
  background-image: url("~@/static/images/pharmacy.jpg");
  background-size: cover;
  display: flex;
  height: 100vh;
}
.fp {
  margin: 10px 0px;
}
</style>
