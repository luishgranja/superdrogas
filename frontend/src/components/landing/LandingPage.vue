<template>
  <body class="hold-transition skin-black-light layout-top-nav fixed">
    <div class="wrapper">
      <header class="main-header">
        <nav class="navbar navbar-static-top">
          <div class="container">
            <div class="navbar-header">
              <a href="" class="navbar-brand">
                <strong>Super Drogas</strong>
              </a>
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse">
                <i class="fa fa-bars"></i>
              </button>
            </div>
            <div class="collapse navbar-collapse pull-left" id="navbar-collapse">
              <ul class="nav navbar-nav nav-item">
                <li><a href="#funcionalidad">Functionality</a></li>
                <li><a href="#pricing">Pricing</a></li>
              </ul>
            </div>
            <div class="navbar-custom-menu">
              <router-link :to="{ name: 'home' }">
                <ul class="nav navbar-nav nav-item">
                  <li>
                    <button class="btn btn-success btn-raised">
                      ADMIN
                    </button>
                  </li>
                </ul>
              </router-link>
            </div>
          </div>
        </nav>
      </header>
      <div
        id="seccion1"
        class="content-wrapper"
        style="background-color: #ffffff !important;"
      >
        <div class="container">
          <section class="content">
            <div class="row">
              <div class="col-md-6">
                <h1>
                  <b>
                    The management and administration tool for your drugstore
                    within the reach of your needs
                  </b>
                </h1>
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Quae modi, exercitationem magnam nemo beatae nostrum at expedita
                  qui maiores! Accusamus reprehenderit modi alias ipsam ratione eligendi
                  repellendus inventore voluptatum harum.
                </p>
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Quae modi, exercitationem magnam nemo beatae nostrum at expedita
                  qui maiores! Accusamus reprehenderit modi alias ipsam ratione eligendi
                  repellendus inventore voluptatum harum.
                </p>
              </div>
              <div class="col-md-6">
                <img src="@/static/images/farmacia.svg" alt="Pharmacy" style="width:100%; height: 100%;">
              </div>
            </div>
          </section>
          <section class="content" id="funcionalidad">
            <div class="row">
              <h2 class="text-center">
                See how we are redesigning SUPERDROGAS Cloud Software
              </h2>
              <div class="col-md-6">
                <img src="@/static/images/bg.png" alt="" height="100%" width="100%">
              </div>
              <div class="col-md-6">
                <h1>
                  <b>
                    Better investment and better administration
                  </b>
                </h1>
                <p>
                  Lorem ipsum dolor sit amet consectetur adipisicing elit.
                  Ipsum velit beatae aliquid odit, asperiores dolorem veritatis
                  in provident eligendi fugit cum saepe repellat non commodi quam
                  repellendus eveniet voluptatem excepturi.
                </p>
              </div>
            </div>
          </section>
          <section class="content" id="pricing">
            <h2 class="text-center">Pricing</h2>
            <div class="planContainer">
              <div class="plan">
                <div class="titleContainer">
                  <div class="title">Starter</div>
                </div>
                <div class="infoContainer">
                  <div class="price">
                    <p>$6 </p><span>/mo</span>
                  </div>
                  <div class="p desc"><em>Great for beginners and hobbyists.</em></div>
                  <ul class="features">
                    <li><strong>2</strong> Users</li>
                    <li><strong>5</strong> Projects</li>
                    <li><strong>10GB</strong> Storage</li>
                    <li><strong>100GB</strong> Bandwidth</li>
                    <li><strong>0</strong> Free Domain</li>
                  </ul>
                  <button class="btn btn-raised btn-success">Select Plan</button>
                </div>
              </div>
              <div class="plan">
                <div class="titleContainer">
                  <div class="title">Standard</div>
                </div>
                <div class="infoContainer">
                  <div class="price">
                    <p>$12 </p><span>/mo</span>
                  </div>
                  <div class="p desc"><em>Recommended for developers and experienced hobbyists.</em></div>
                  <ul class="features">
                    <li><strong>5</strong> Users</li>
                    <li><strong>15</strong> Projects</li>
                    <li><strong>50GB</strong> Storage</li>
                    <li><strong>500GB</strong> Bandwidth</li>
                    <li><strong>1</strong> Free Domain</li>
                  </ul>
                  <button class="btn btn-raised btn-success">Select Plan</button>
                </div>
              </div>
              <div class="plan">
                <div class="titleContainer">
                  <div class="title">Premium</div>
                </div>
                <div class="infoContainer">
                  <div class="price">
                    <p>$20</p><span>/mo</span>
                  </div>
                  <div class="p desc"><em>Ideal for small businesses and experienced developers.</em></div>
                  <ul class="features">
                    <li><strong>20</strong> Users</li>
                    <li><strong>Unlimited</strong> Projects</li>
                    <li><strong>150GB</strong> Storage</li>
                    <li><strong>1TB</strong> Bandwidth</li>
                    <li><strong>2</strong> Free Domains</li>
                  </ul>
                  <button class="btn btn-raised btn-success">Select Plan</button>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
      <footer class="main-footer">
        <div class="container">
          <strong>Copyright &copy; 2019 | <a>Super Drogas</a></strong>.
          All rights reserved.
          <div class="pull-right hidden-xs">
            Universidad del Valle
          </div>
        </div>
      </footer>
    </div>
  </body>
</template>

<script>
export default {
  name: 'landing'
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800");
.nav-item {
  margin-bottom: 0px !important;
}
.planContainer {
  display: flex;
  flex-wrap: wrap;
  margin: 1em;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
}
.plan {
  background: white;
  width: 20em;
  box-sizing: border-box;
  text-align: center;
  margin: 1em;
  margin-bottom: 1em;
}
.plan .titleContainer {
  background-color: #f3f3f3;
  padding: 1em;
}
.plan .titleContainer .title {
  font-size: 1.45em;
  text-transform: uppercase;
  color: #1abc9c;
  font-weight: 700;
}
.plan .infoContainer {
  padding: 1em;
  color: #2d3b48;
  box-sizing: border-box;
}
.plan .infoContainer .price {
  font-size: 1.35em;
  padding: 1em 0;
  font-weight: 600;
  margin-top: 0;
  display: inline-block;
  width: 80%;
}
.plan .infoContainer .price p {
  font-size: 1.35em;
  display: inline-block;
  margin: 0;
}
.plan .infoContainer .price span {
  font-size: 1.0125em;
  display: inline-block;
}
.plan .infoContainer .desc {
  padding-bottom: 1em;
  border-bottom: 2px solid #f3f3f3;
  margin: 0 auto;
  width: 90%;
}
.plan .infoContainer .desc em {
  font-size: 1em;
  font-weight: 500;
}
.plan .infoContainer .features {
  font-size: 1em;
  list-style: none;
  padding-left: 0;
}
.plan .infoContainer .features li {
  padding: 0.5em;
}
.plan .infoContainer .selectPlan {
  border: 2px solid #1abc9c;
  padding: 0.75em 1em;
  border-radius: 2.5em;
  cursor: pointer;
  transition: all 0.25s;
  margin: 1em auto;
  box-sizing: border-box;
  max-width: 70%;
  display: block;
  font-weight: 700;
}
.plan .infoContainer .selectPlan:hover {
  background-color: #1abc9c;
  color: white;
}
@media screen and (max-width: 25em) {
  .planContainer {
    margin: 0;
  }
  .planContainer .plan {
    width: 100%;
    margin: 1em 0;
  }
}
</style>
