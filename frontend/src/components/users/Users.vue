<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Users
          <a class="btn btn-primary btn-raised" data-toggle="modal" data-target="#create">
            + New user
          </a>
        </h1>
      </div>
      <ol class="breadcrumb">
        <li><router-link :to="{ name: 'home' }">Home</router-link></li>
        <li class="active">Users</li>
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
                  <tr v-for="(user, index) in users" :key="index">
                    <td>{{ user.first_name }} {{ user.last_name }}</td>
                    <td>{{ user.username }}</td>
                    <td>{{ user.email }}</td>
                    <td class="text-center">
                      <p v-if="user.is_active" class="badge bg-green p-bg">Active</p>
                      <p v-else class="badge bg-red p-bg">Inactive</p>
                    </td>
                    <td class="text-center">
                      <a href="#delete" :class="[user.is_active ? 'btn-danger' : 'btn-success']" class="btn.btn-app btn-sm action-btn" data-toggle="modal" data-target="#delete">
                        <i v-if="user.is_active" class="fa fa-user-times"></i>
                        <i v-else class="fa fa-user-plus"></i>
                      </a>
                      <a href="#update" class="btn.btn-app btn-primary btn-sm action-btn" data-toggle="modal" data-target="#update">
                        <i class="fa fa-edit"></i>
                      </a>
                      <a href="#read" class="btn.btn-app btn-info btn-sm action-btn" data-toggle="modal" data-target="#read">
                        <i class="fa fa-info-circle"></i>
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
    <create />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import Create from './actions/Create'

export default {
  name: 'users',
  components: {
    Create
  },
  computed: {
    ...mapState('users', [
      'users',
      'isLoading'
    ])
  },
  methods: {
    ...mapActions('users', [
      'getUsers'
    ])
  },
  created () {
    this.getUsers()
  },
  updated () {
    // eslint-disable-next-line
    $(function () { $('#table').DataTable() })
  }
}
</script>
