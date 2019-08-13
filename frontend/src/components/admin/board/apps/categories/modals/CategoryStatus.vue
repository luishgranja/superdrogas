<template>
  <modal-component
    id="category-status"
    :title="`${ category.is_active ? 'Deactivate' : 'Activate' } category`"
  >
    <div class="row">
      <div class="col-sm-12">
        <p>
          Are you sure to
          <strong>{{ category.is_active ? 'deactivate' : 'activate' }}</strong>
          the category <strong>{{ category.name }}</strong>?
        </p>
      </div>
    </div>
    <div class="pull-right">
      <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
      <button
        @click="deleteCategory"
        :class="`${ category.is_active ? 'btn-danger' : 'btn-success' }`"
        class="btn"
        type="submit"
      >
        {{ category.is_active ? 'Deactivate' : 'Activate' }}
      </button>
    </div>
  </modal-component>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'category-status',
  computed: {
    ...mapState('categories', [
      'category'
    ])
  },
  methods: {
    ...mapActions('categories', [
      'deleteCategory'
    ])
  }
}
</script>
