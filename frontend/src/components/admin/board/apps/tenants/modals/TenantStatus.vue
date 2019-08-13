<template>
  <modal-component
    id="tenant-status"
    :title="`${ tenant.is_active ? 'Deactivate' : 'Activate' } tenant`"
  >
    <div class="row">
      <div class="col-sm-12">
        <p>
          Are you sure to
          <strong>{{ tenant.is_active ? 'deactivate' : 'activate' }}</strong>
          the tenant <strong>{{ tenant.name }}</strong>?
        </p>
      </div>
    </div>
    <div class="pull-right">
      <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
      <button
        @click="deleteTenant"
        :class="`${ tenant.is_active ? 'btn-danger' : 'btn-success' }`"
        class="btn"
        type="submit"
      >
        {{ tenant.is_active ? 'Deactivate' : 'Activate' }}
      </button>
    </div>
  </modal-component>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'tenant-status',
  computed: {
    ...mapState('tenants', [
      'tenant'
    ])
  },
  methods: {
    ...mapActions('tenants', [
      'deleteTenant'
    ])
  }
}
</script>
