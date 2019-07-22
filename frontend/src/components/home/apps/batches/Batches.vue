<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Batches
          <a
            @click="getBatch()"
            class="btn btn-primary btn-raised"
            data-toggle="modal"
            data-target="#batch-form"
          >
            Create batch
          </a>
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Batches
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
                    <th>Product</th>
                    <th>Quantity</th>
                    <th>Manufacturing Date</th>
                    <th>Expiration Date</th>
                    <th>Status</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(batch, index) in batches" :key="index">
                    <td>{{ batch.product_name }} </td>
                    <td>{{ batch.quantity }}</td>
                    <td>{{ batch.manufacturing_date }}</td>
                    <td>{{ batch.expiration_date }}</td>
                    <td class="text-center">
                      <p
                        :class="`${ batch.is_active ? 'bg-green' : 'bg-red' }`"
                        class="badge p-bg"
                      >
                        {{ batch.is_active ? 'Active' : 'Inactive' }}
                      </p>
                    </td>
                    <td class="text-center">
                      <a
                        @click="getBatch(batch.id)"
                        class="btn.btn-app btn-primary btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#batch-form"
                      >
                        <i class="fa fa-edit"></i>
                      </a>
                      <a
                        @click="getBatch(batch.id)"
                        class="btn.btn-app btn-info btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#batch-detail"
                      >
                        <i class="fa fa-info-circle"></i>
                      </a>
                      <a
                        @click="getBatch(batch.id)"
                        :class="`${ batch.is_active ? 'btn-danger' : 'btn-success' }`"
                        class="btn.btn-app btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#batch-status"
                      >
                        <i :class="`${ batch.is_active ? 'fa fa-user-times' : 'fa fa-user-plus' }`"></i>
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
    <batch-detail />
    <batch-form />
    <batch-status />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import template from '@/utilities/template'
import BatchDetail from './modals/BatchDetail'
import BatchForm from './modals/BatchForm'
import BatchStatus from './modals/BatchStatus'

export default {
  name: 'batches',
  components: {
    BatchDetail,
    BatchForm,
    BatchStatus
  },
  computed: {
    ...mapState('batches', [
      'batches',
      'isLoading'
    ])
  },
  methods: {
    ...mapActions('batches', [
      'getBatches',
      'getBatch'
    ])
  },
  created () {
    this.getBatches()
  },
  updated () {
    template.refresh()
  }
}
</script>
