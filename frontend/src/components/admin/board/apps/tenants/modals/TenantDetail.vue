<template>
  <modal-component id="tenant-detail" title="Tenant detail">
    <div class="row">
      <div class="col-sm-12">
        <ul>
          <li>
            <strong>Schema name:</strong>
            {{ tenant.schema_name }}
          </li>
          <li>
            <strong>Name:</strong>
            {{ tenant.name }}
          </li>
          <li>
            <strong>Prefix:</strong>
            {{ tenant.prefix }}
          </li>
          <li>
            <strong>NIT:</strong>
            {{ tenant.nit }}
          </li>
          <li>
            <strong>Phone:</strong>
            {{ tenant.phone }}
          </li>
          <li>
            <strong>Email:</strong>
            {{ tenant.email }}
          </li>
          <li>
            <strong>Address:</strong>
            {{ tenant.address }}
          </li>
          <li>
            <strong>Description:</strong>
            {{ tenant.description }}
          </li>
          <li>
            <strong>Status:</strong>
            {{ tenant.is_active ? 'Active' : 'Inactive' }}
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
  name: 'tenant-detail',
  computed: {
    ...mapState('tenants', [
      'tenant'
    ])
  }
}
</script>
