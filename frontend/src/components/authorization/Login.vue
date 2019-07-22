<template>
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
          <a class="col-md-6 fp">
            I forgot my password
          </a>
          <div class="col-md-6 pull-right">
            <button type="submit" class="btn bg-navy btn-block">
              Login
              <i class="fa fa-sign-in"></i>
            </button>
          </div>
        </div>
      </form>
      <div class="text-center social-btns">
        <p>Or login with</p>
        <a class="btn btn-social-icon btn-google"><i class="fa fa-google"></i></a>
        <a class="btn btn-social-icon btn-facebook"><i class="fa fa-facebook"></i></a>
        <a class="btn btn-social-icon btn-twitter"><i class="fa fa-twitter"></i></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login'
}
</script>

<style>
body {
  background-image: url("~@/static/images/pharmacy.jpg");
  background-size: cover;
}
.fp {
  margin: 10px 0px;
}
.social-btns {
  margin-top: 20px;
}
.social-btns .btn {
  margin: 0px 5px;
}
</style>
