<template>
  <header class="main-header">
    <a class="logo">
      <span class="logo-mini">
        <strong>SD</strong>
      </span>
      <span class="logo-lg">Super Drogas</span>
    </a>
    <nav class="navbar navbar-static-top" role="navigation">
      <a class="sidebar-toggle" data-toggle="push-menu" role="button"></a>
      <div class="navbar-custom-menu">
        <ul class="nav navbar-nav">
          <li class="dropdown user user-menu">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
              <img src="@/static/images/user.png" class="user-image" alt="User">
              <span class="hidden-xs">Iván Toro</span>
            </a>
            <ul class="dropdown-menu">
              <li class="user-header">
                <img src="@/static/images/user.png" class="img-circle" alt="User">
                <p>
                  Iván Toro
                  <small>ivanmtoroc</small>
                  <small>ivanmtoroc@gmail.com</small>
                </p>
              </li>
              <li class="user-footer">
                <div>
                  <a class="btn btn-default btn-block btn-flat">
                    Logout
                    <i class="fa fa-sign-out"></i>
                  </a>
                </div>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'header-component'
}
</script>
