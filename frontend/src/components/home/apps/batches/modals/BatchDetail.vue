<template>
  <modal-component id="batch-detail" title="Batch detail">
    <div class="row">
      <div class="col-sm-12">
        <ul>
          <li>
            <strong>Product:</strong>
            {{ batch.NombreProducto }}
          </li>
          <li>
            <strong>Quantity:</strong>
            {{ batch.quantity }}
          </li>
          <li>
            <strong>Manufacturing Date:</strong>
            {{ batch.manufacturing_date }}
          </li>
          <li>
            <strong>Expiration Date:</strong>
            {{ batch.expiration_date }}
          </li>
          <li>
            <strong>Status:</strong>
            {{ batch.is_active ? 'Active' : 'Inactive' }}
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
  name: 'batch-detail',
  computed: {
    ...mapState('batches', [
      'batch'
    ])
  }
}
</script>
