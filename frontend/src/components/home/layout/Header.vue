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
            <a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
              <img src="https://i.imgur.com/VvO9nVO.png" class="user-image" alt="User image" />
              <span class="hidden-xs">Iván Toro</span>
              <div class="ripple-container"></div>
            </a>
            <ul class="dropdown-menu">
              <li class="user-header">
                <img src="https://i.imgur.com/VvO9nVO.png" class="img-circle" alt="User image" />
                <p>
                  Iván Toro - Administrator
                  <small>ivanmtoroc</small>
                  <small>ivanmtoroc@gmail.com</small>
                </p>
              </li>
              <li class="user-footer">
                <a class="btn btn-warning">
                  Logout
                  <i class="fa fa-sign-out"></i>
                </a>
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
