<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Products
          <a
            @click="getProduct()"
            class="btn btn-primary btn-raised"
            data-toggle="modal"
            data-target="#product-form"
          >
            Create Product
          </a>
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Products
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
                    <th>Name</th>
                    <th>Price</th>
                    <th>Category</th>
                    <th>Brand</th>
                    <th>Status</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(product, index) in products" :key="index">
                    <td>{{ product.name }}</td>
                    <td>{{ product.price }}</td>
                    <td>{{ product.category_name }}</td>
                    <td>{{ product.brand_name }}</td>
                    <td class="text-center">
                      <p
                        :class="`${ product.is_active ? 'bg-green' : 'bg-red' }`"
                        class="badge p-bg"
                      >
                        {{ product.is_active ? 'Active' : 'Inactive' }}
                      </p>
                    </td>
                    <td class="text-center">
                      <a
                        @click="getProduct(product.id)"
                        class="btn.btn-app btn-primary btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#product-form"
                      >
                        <i class="fa fa-edit"></i>
                      </a>
                      <a
                        @click="getProduct(product.id)"
                        class="btn.btn-app btn-info btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#product-detail"
                      >
                        <i class="fa fa-info-circle"></i>
                      </a>
                      <a
                        @click="getProduct(product.id)"
                        :class="`${ product.is_active ? 'btn-danger' : 'btn-success' }`"
                        class="btn.btn-app btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#product-status"
                      >
                        <i :class="`${ product.is_active ? 'fa fa-times-circle' : 'fa fa-plus-circle' }`"></i>
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
    <product-detail />
    <product-form />
    <product-status />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import template from '@/utilities/template'
import ProductDetail from './modals/ProductsDetail'
import ProductForm from './modals/ProductsForm'
import ProductStatus from './modals/ProductsStatus'

export default {
  name: 'products',
  components: {
    ProductDetail,
    ProductForm,
    ProductStatus
  },
  computed: {
    ...mapState('products', [
      'products',
      'isLoading'
    ])
  },
  methods: {
    ...mapActions('products', [
      'getProducts',
      'getProduct'
    ])
  },
  created () {
    this.getProducts()
  },
  updated () {
    template.reload()
  }
}
</script>
