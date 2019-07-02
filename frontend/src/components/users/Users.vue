<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Users
          <a href="#create" class="btn btn-primary btn-raised" data-toggle="modal" data-target="#create">Add new user</a>
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
              <table id="table" class="table table-bordered table-striped">
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Username</th>
                    <th>Identification</th>
                    <th>Status</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(user, index) in users" :key="index" class="odd">
                    <td>{{ user.name }}</td>
                    <td>{{ user.username }}</td>
                    <td>{{ user.identification }}</td>
                    <td class="text-center">
                      <p v-if="user.status" class="badge bg-green p-bg">Active</p>
                      <p v-else class="badge bg-red p-bg">Inactive</p>
                    </td>
                    <td class="text-center">
                      <a href="#delete" :class="[user.status ? 'btn-danger' : 'btn-success']" class="btn.btn-app btn-sm action-btn" data-toggle="modal" data-target="#delete">
                        <i v-if="user.status" class="fa fa-user-times"></i>
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
  </div>
</template>

<script>
// eslint-disable-next-line
$(function () { $('#table').DataTable() })

export default {
  name: 'users',
  data () {
    return {
      users: [
        {
          name: 'Iván Toro',
          username: 'ivanmtoroc',
          identification: '123467890',
          status: false
        },
        {
          name: 'Luis Granja',
          username: 'luisgranja',
          identification: '0987654321',
          status: true
        },
        {
          name: 'Sebastián Villegas',
          username: 'sebastianvillegas',
          identification: '0987612345',
          status: true
        },
        {
          name: 'Jhon Hadder',
          username: 'jhonhadder',
          identification: '1234657809',
          status: false
        }
      ]
    }
  }
}
</script>
