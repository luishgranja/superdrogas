.0<template>
  <modal-component id="brand-detail" title="Brand detail">
    <div class="row">
      <div class="col-sm-12">
        <ul>
          <li>
            <strong>Name:</strong>
            {{ brand.name }}
          </li>
          <li>
            <strong>Email:</strong>
            {{ brand.email }}
          </li>
          <li>
            <strong>Phone:</strong>
            {{ brand.phone }}
          </li>
          <li>
            <strong>Status:</strong>
            {{ brand.is_active ? 'Active' : 'Inactive' }}
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
  name: 'brand-detail',
  computed: {
    ...mapState('brands', [
      'brand'
    ])
  }
}
</script>
