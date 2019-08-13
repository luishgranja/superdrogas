<template>
  <modal-component id="category-form" :title="`${ isNewCategory ? 'Create' : 'Update' } category`">
    <form>
      <div class="row">
        <input-component
          class="col-md-12"
          id="name"
          v-model="name"
          placeholder="Name"
          :inputErrors="errors.name"
        />
        <input-component
          class="col-md-12"
          id="description"
          v-model="description"
          placeholder="Description"
          :inputErrors="errors.description"
        />
      </div>
      <div class="pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button v-if="isNewCategory" @click="createCategory($event)" type="submit" class="btn btn-success">Create</button>
        <button v-else @click="updateCategory($event)" type="submit" class="btn btn-primary">Update</button>
      </div>
    </form>
  </modal-component>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'category-form',
  computed: {
    ...mapState('categories', [
      'category',
      'errors'
    ]),
    ...mapGetters('categories', [
      'isNewCategory'
    ]),
    name: {
      get () {
        return this.category.name
      },
      set (value) {
        this.$store.commit('categories/SET_NAME', value)
      }
    },
    description: {
      get () {
        return this.category.description
      },
      set (value) {
        this.$store.commit('categories/SET_DESCRIPTION', value)
      }
    }
  },
  methods: {
    ...mapActions('categories', [
      'createCategory',
      'updateCategory'
    ])
  }
}
</script>
