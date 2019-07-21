<template>
  <modal-component
    id="batch-status"
    :title="`${ batch.is_active ? 'Deactivate' : 'Activate' } batch`"
  >
    <div class="row">
      <div class="col-sm-12">
        <p>
          Are you sure to
          <strong>{{ batch.is_active ? 'deactivate' : 'activate' }}</strong>
          the batch with
          <strong> {{ batch.quantity }} {{ batch.NombreProducto }} </strong>?
        </p>
      </div>
    </div>
    <div class="pull-right">
      <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
      <button
        @click="deleteBatch"
        :class="`${ batch.is_active ? 'btn-danger' : 'btn-success' }`"
        class="btn"
        type="submit"
      >
        {{ batch.is_active ? 'Deactivate' : 'Activate' }}
      </button>
    </div>
  </modal-component>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'batch-status',
  computed: {
    ...mapState('batches', [
      'batch'
    ])
  },
  methods: {
    ...mapActions('batches', [
      'deleteBatch'
    ])
  }
}
</script>