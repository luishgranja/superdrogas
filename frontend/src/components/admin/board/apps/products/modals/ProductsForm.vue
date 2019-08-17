<template>
  <modal-component id="product-form" :title="`${ isNewProduct ? 'Create' : 'Update' } product`">
    <form>
      <div class="row">
        <input-component
          class="col-sm-6"
          id="name"
          v-model="name"
          placeholder="Name"
          :inputErrors="errors.name"
        />
        <input-component
          class="col-sm-6"
          v-model="description"
          id="description"
          placeholder="Description"
          :inputErrors="errors.description"
        />
      </div>
      <div class="row">
        <input-component
          class="col-sm-6"
          v-model="price"
          id="price"
          type="number"
          placeholder="Price"
          :inputErrors="errors.price"
        />
        <div class="col-sm-6 file">
          <label for="image">Image</label>
          <input
            class="form-control"
            @change="handleFileUpload()"
            id="image"
            type="file"
            ref="file"
          >
          <span v-if="errors.image" class="help-block error-block">
            This field is required.
          </span>
        </div>
      </div>
      <div class="row">
        <div class="form-group col-sm-6">
          <label>Category</label>
          <select2
            id="category"
            :options="activeCategories"
            v-model="category"
          >
          </select2>
          <span v-if="errors.category" class="help-block error-block">
            This field is required.
          </span>
        </div>
        <div class="form-group col-sm-6">
          <label>Brand</label>
          <select2
            id="brand"
            :options="activeBrands"
            v-model="brand"
          >
          </select2>
          <span v-if="errors.brand" class="help-block error-block">
            This field is required.
          </span>
        </div>
      </div>
      <div class="mt-10 pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button v-if="isNewProduct" @click="createProduct($event)" type="submit" class="btn btn-success">Create</button>
        <button v-else @click="updateProduct($event)" type="submit" class="btn btn-primary">Update</button>
      </div>
    </form>
  </modal-component>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'product-form',
  computed: {
    ...mapState('products', [
      'product',
      'errors'
    ]),
    ...mapGetters('products', [
      'isNewProduct'
    ]),
    ...mapGetters('categories', [
      'activeCategories'
    ]),
    ...mapGetters('brands', [
      'activeBrands'
    ]),
    name: {
      get () {
        return this.product.name
      },
      set (value) {
        this.$store.commit('products/SET_NAME', value)
      }
    },
    description: {
      get () {
        return this.product.description
      },
      set (value) {
        this.$store.commit('products/SET_DESCRIPTION', value)
      }
    },
    price: {
      get () {
        return this.product.price
      },
      set (value) {
        this.$store.commit('products/SET_PRICE', value)
      }
    },
    image: {
      get () {
        return this.product.image
      },
      set (value) {
        this.$store.commit('products/SET_IMAGE', value)
      }
    },
    category: {
      get () {
        return this.product.category
      },
      set (value) {
        this.$store.commit('products/SET_CATEGORY', value)
      }
    },
    brand: {
      get () {
        return this.product.brand
      },
      set (value) {
        this.$store.commit('products/SET_BRAND', value)
      }
    }
  },
  methods: {
    ...mapActions('products', [
      'createProduct',
      'updateProduct'
    ]),
    ...mapActions('categories', [
      'getCategories'
    ]),
    ...mapActions('brands', [
      'getBrands'
    ]),
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
      this.$store.commit('products/SET_IMAGE', this.file)
    }
  },
  created () {
    this.getCategories()
    this.getBrands()
  }
}
</script>

<style scoped>
.file {
  padding-bottom: 7px;
  margin: 28px 0 0 0;
}
</style>
