<template>
  <modal-component
    id="brand-status"
    :title="`${ brand.is_active ? 'Deactivate' : 'Activate' } brand`"
  >
    <div class="row">
      <div class="col-sm-12">
        <p>
          Are you sure to
          <strong>{{ brand.is_active ? 'deactivate' : 'activate' }}</strong>
          the brand <strong>{{ brand.name }}</strong>?
        </p>
      </div>
    </div>
    <div class="pull-right">
      <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
      <button
        @click="deleteBrand"
        :class="`${ brand.is_active ? 'btn-danger' : 'btn-success' }`"
        class="btn"
        type="submit"
      >
        {{ brand.is_active ? 'Deactivate' : 'Activate' }}
      </button>
    </div>
  </modal-component>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'brand-status',
  computed: {
    ...mapState('brands', [
      'brand'
    ])
  },
  methods: {
    ...mapActions('brands', [
      'deleteBrand'
    ])
  }
}
</script>
