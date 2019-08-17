<template>
  <section class="content">
    <h1>Home</h1>
    <div class="row">
      <div class="col-md-4 col-sm-6">
        <div class="box box-widget widget-user">
          <div class="widget-user-header bg-aqua-active module-header">
            <h2 class="widget-user-username text-center">
              <strong>
                <i class="fa fa-users"></i>
                Accounts
              </strong>
            </h2>
          </div>
          <div class="box-footer module-footer">
            <div class="row">
              <div class="col-xs-6 border-right">
                <div class="description-block">
                  <h5 class="description-header module-item">
                    <router-link :to="{ name: 'users' }">
                      <i class="fa fa-user"></i>
                      Users
                    </router-link>
                  </h5>
                </div>
              </div>
              <div class="col-xs-6 border-right">
                <div class="description-block">
                  <h5 class="description-header module-item">
                    <router-link :to="{ name: 'customers' }">
                      <i class="fa fa-child"></i>
                      Customers
                    </router-link>
                  </h5>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="isAdmin" class="col-md-4 col-sm-6">
        <div class="box box-widget widget-user">
          <div class="widget-user-header bg-red-active module-header">
            <h2 class="widget-user-username text-center">
              <router-link :to="{ name: 'tenants' }">
                <strong>
                  <i class="fa fa-medkit"></i>
                  Tenants
                </strong>
              </router-link>
            </h2>
          </div>
        </div>
      </div>
      <div v-if="isAdmin" class="col-md-4 col-sm-6">
        <div class="box box-widget widget-user">
          <div class="widget-user-header bg-yellow-active module-header">
            <h2 class="widget-user-username text-center">
              <router-link :to="{ name: 'metrics' }">
                <strong>
                  <i class="fa fa-area-chart"></i>
                  Metrics
                </strong>
              </router-link>
            </h2>
          </div>
        </div>
      </div>
      <div v-if="!isAdmin" class="col-md-4 col-sm-6">
        <div class="box box-widget widget-user">
          <div class="widget-user-header bg-yellow-active module-header">
            <h2 class="widget-user-username text-center">
              <strong>
                <i class="fa fa-cubes"></i>
                Inventory
              </strong>
            </h2>
          </div>
          <div class="box-footer module-footer">
            <div class="row">
              <div class="col-xs-6 border-right">
                <div class="description-block">
                  <h5 class="description-header module-item">
                    <router-link :to="{ name: 'batches' }">
                      <i class="fa fa-building"></i>
                      Batches
                    </router-link>
                  </h5>
                </div>
              </div>
              <div class="col-xs-6 border-right">
                <div class="description-block">
                  <h5 class="description-header module-item">
                    <router-link :to="{ name: 'brands' }">
                      <i class="fa fa-trademark"></i>
                      Brands
                    </router-link>
                  </h5>
                </div>
              </div>
              <div class="col-xs-6 border-right">
                <div class="description-block">
                  <h5 class="description-header module-item">
                    <router-link :to="{ name: 'categories' }">
                      <i class="fa fa-tag"></i>
                      Categories
                    </router-link>
                  </h5>
                </div>
              </div>
              <div class="col-xs-6 border-right">
                <div class="description-block">
                  <h5 class="description-header module-item">
                    <router-link :to="{ name: 'products' }">
                      <i class="fa fa-cube"></i>
                      Products
                    </router-link>
                  </h5>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="!isAdmin" class="col-md-4 col-sm-6">
        <div class="box box-widget widget-user">
          <div class="widget-user-header bg-red-active module-header">
            <h2 class="widget-user-username text-center">
              <router-link :to="{ name: 'reports' }">
                <strong>
                  <i class="fa fa-bar-chart"></i>
                  Reports
                </strong>
              </router-link>
            </h2>
          </div>
        </div>
      </div>
      <div v-if="!isAdmin" class="col-md-4 col-sm-6">
        <div class="box box-widget widget-user">
          <div class="widget-user-header bg-green-active module-header">
            <h2 class="widget-user-username text-center">
              <router-link :to="{ name: 'sales' }">
                <strong>
                  <i class="fa fa-money"></i>
                  Sales
                </strong>
              </router-link>
            </h2>
          </div>
        </div>
      </div>
      <div v-if="!isAdmin" class="col-md-4 col-sm-6">
        <div class="box box-widget widget-user">
          <div class="widget-user-header bg-orange-active module-header">
            <h2 class="widget-user-username text-center">
              <router-link :to="{ name: 'configurations' }">
                <strong>
                  <i class="fa fa-cog"></i>
                  Configurations
                </strong>
              </router-link>
            </h2>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'home',
  computed: {
    ...mapState('app', [
      'isAdmin'
    ])
  }
}
</script>

<style scoped>
a {
  color: #333 !important;
}
strong {
  color: white;
}
.module-header {
  height: auto;
}
.module-footer {
  padding-top: 20px;
}
.module-item {
  transition: 0.3s ease;
}
.module-item:hover {
  transform: scale(1.2, 1.2);
}
</style>
