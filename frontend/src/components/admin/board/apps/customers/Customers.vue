<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Customers
          <a
            @click="getUser()"
            class="btn btn-primary btn-raised"
            data-toggle="modal"
            data-target="#user-form"
          >
            Create customer
          </a>
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Customers
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
              <table v-else id="table" class="table table-bordered table-striped">
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Username</th>
                    <th>Email</th>
                    <th>Status</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(customer, index) in customers" :key="index">
                    <td>{{ customer.first_name }} {{ customer.last_name }}</td>
                    <td>{{ customer.username }}</td>
                    <td>{{ customer.email }}</td>
                    <td class="text-center">
                      <p
                        :class="`${ customer.is_active ? 'bg-green' : 'bg-red' }`"
                        class="badge p-bg"
                      >
                        {{ customer.is_active ? 'Active' : 'Inactive' }}
                      </p>
                    </td>
                    <td class="text-center">
                      <a
                        @click="getUser(customer.id)"
                        class="btn.btn-app btn-primary btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#user-form"
                      >
                        <i class="fa fa-edit"></i>
                      </a>
                      <a
                        @click="getUser(customer.id)"
                        class="btn.btn-app btn-info btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#user-detail"
                      >
                        <i class="fa fa-info-circle"></i>
                      </a>
                      <a
                        @click="getUser(customer.id)"
                        :class="`${ customer.is_active ? 'btn-danger' : 'btn-success' }`"
                        class="btn.btn-app btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#user-status"
                      >
                        <i :class="`${ customer.is_active ? 'fa fa-user-times' : 'fa fa-user-plus' }`"></i>
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
    <customer-detail />
    <customer-form />
    <customer-status />
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import template from '@/utilities/template'
import CustomerDetail from './modals/CustomerDetail'
import CustomerForm from './modals/CustomerForm'
import CustomerStatus from './modals/CustomerStatus'

export default {
  name: 'customers',
  components: {
    CustomerDetail,
    CustomerForm,
    CustomerStatus
  },
  computed: {
    ...mapState('users', [
      'isLoading'
    ]),
    ...mapGetters('users', [
      'customers'
    ])
  },
  methods: {
    ...mapActions('users', [
      'getUsers',
      'getUser'
    ])
  },
  created () {
    this.getUsers()
  },
  updated () {
    this.$nextTick(() => { template.reload() })
  }
}
</script>
