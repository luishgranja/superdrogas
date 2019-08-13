.0<template>
  <modal-component id="category-detail" title="Category detail">
    <div class="row">
      <div class="col-sm-12">
        <ul>
          <li>
            <strong>Name:</strong>
            {{ category.name }}
          </li>
          <li>
            <strong>Description:</strong>
            {{ category.description }}
          </li>
          <li>
            <strong>Status:</strong>
            {{ category.is_active ? 'Active' : 'Inactive' }}
          </li>
        </ul>
      </div>
    </div>
    <div class="pull-right">
      <button type="button" class="btn btn-info" data-dismiss="modal">Close</button>
    </div>
  </modal-component>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'category-detail',
  computed: {
    ...mapState('categories', [
      'category'
    ])
  }
}
</script>
