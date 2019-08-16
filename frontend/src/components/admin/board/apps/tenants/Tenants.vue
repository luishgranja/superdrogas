<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Tenants
          <a
            @click="getTenant()"
            class="btn btn-primary btn-raised"
            data-toggle="modal"
            data-target="#tenant-form"
          >
            Create tenant
          </a>
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Tenants
        </li>
      </ol>
    </section>
    <section class="content">
      <div class="row">
        <div class="col-sm-12">
          <div class="box">
            <div class="box-body">
              <div v-if="isLoading" class="text-center">
                <spinner-component />
              </div>
              <table
                v-else
                id="table"
                class="table table-bordered table-striped"
              >
                <thead>
                  <tr>
                    <th>Schema name</th>
                    <th>Name</th>
                    <th>NIT</th>
                    <th>Email</th>
                    <th>Status</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(tenant, index) in tenants" :key="index">
                    <td>{{ tenant.schema_name }}</td>
                    <td>{{ tenant.name }}</td>
                    <td>{{ tenant.nit }}</td>
                    <td>{{ tenant.email }}</td>
                    <td class="text-center">
                      <p
                        :class="`${ tenant.is_active ? 'bg-green' : 'bg-red' }`"
                        class="badge p-bg"
                      >
                        {{ tenant.is_active ? 'Active' : 'Inactive' }}
                      </p>
                    </td>
                    <td class="text-center">
                      <a
                        @click="getTenant(tenant.id)"
                        class="btn.btn-app btn-primary btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#tenant-form"
                      >
                        <i class="fa fa-edit"></i>
                      </a>
                      <a
                        @click="getTenant(tenant.id)"
                        class="btn.btn-app btn-info btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#tenant-detail"
                      >
                        <i class="fa fa-info-circle"></i>
                      </a>
                      <a
                        @click="getTenant(tenant.id)"
                        :class="`${ tenant.is_active ? 'btn-danger' : 'btn-success' }`"
                        class="btn.btn-app btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#tenant-status"
                      >
                        <i :class="`${ tenant.is_active ? 'fa fa-times-circle' : 'fa fa-plus-circle' }`"></i>
                      </a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>
    <tenant-detail />
    <tenant-form />
    <tenant-status />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import template from '@/utilities/template'
import TenantDetail from './modals/TenantDetail'
import TenantForm from './modals/TenantForm'
import TenantStatus from './modals/TenantStatus'

export default {
  name: 'tenants',
  components: {
    TenantDetail,
    TenantForm,
    TenantStatus
  },
  computed: {
    ...mapState('tenants', [
      'tenants',
      'isLoading'
    ])
  },
  methods: {
    ...mapActions('tenants', [
      'getTenants',
      'getTenant'
    ])
  },
  created () {
    this.getTenants()
  },
  updated () {
    template.reload()
  }
}
</script>
