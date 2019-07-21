<template>
  <modal-component id="product-form" :title="`${ isNewProduct ? 'Create' : 'Update' } product`">
    <form>
      <div class="row">
      <input-component
          v-model="name"
          id="name"
          label="Name:"
          :erros="errors.name"
        />
        <input-component
          v-model="description"
          id="description"
          label="Description:"
          :erros="errors.description"
        />
        <input-component
          v-model="price"
          id="price"
          label="Price:"
          :erros="errors.price"
        />
        <input-component
          v-model="image"
          id="image"
          label="Image:"
          :erros="errors.image"
        />
        <input-component
          v-model="category"
          id="category"
          label="Category:"
          :erros="errors.category"
        />
        <input-component
          v-model="sku"
          id="Sku"
          label="Sku:"
          :erros="errors.sku"
        />
          <input-component
          v-model="weight"
          id="weight"
          label="Weight:"
          :erros="errors.weight"
        />
          <input-component
          v-model="brand"
          id="brand"
          label="Brand:"
          :erros="errors.brand"
        />
      </div>
      <div class="pull-right">
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
    sku: {
      get () {
        return this.product.sku
      },
      set (value) {
        this.$store.commit('products/SET_SKU', value)
      }
    },
    weight: {
      get () {
        return this.product.weight
      },
      set (value) {
        this.$store.commit('products/SET_WEIGHT', value)
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
    ])
  }
}
</script>
