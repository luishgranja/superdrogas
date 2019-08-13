<template>
  <modal-component id="sale-form" :title="`Cantidad de ${ product.name }`" >
    <div class="row">
      <input-component
          v-model="name"
          id="name"
          label="Name:"
          :erros="errors.name"
        />
          <div class="pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button v-if="isNewProduct" @click="createProduct($event)" type="submit" class="btn btn-success">Create</button>
        <button v-else @click="updateProduct($event)" type="submit" class="btn btn-primary">Update</button>
      </div>
      </div>
    </modal-component>
</template>

<script>

  import { mapState, mapGetters, mapActions } from 'vuex'

 export default {
  name: 'ProductQuantity',
  computed: {
    ...mapState('products', [
      'product',
      'errors'
    ])}
  }
</script>

<style scoped>

</style>