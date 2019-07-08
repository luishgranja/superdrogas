<template>
  <modal-component
    id="user-status"
    :title="`${ currentUser.is_active ? 'Deactivate' : 'Activate' } user`"
  >
    <div class="row">
      <div class="col-sm-12">
        <p>
          Are you sure to
          <strong>{{ currentUser.is_active ? 'deactivate' : 'activate' }}</strong>
          the user
          <strong>{{ currentUser.first_name }} {{ currentUser.last_name }}</strong>?
        </p>
      </div>
    </div>
    <div class="pull-right">
      <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
      <button
        @click="deleteUser"
        :class="`${ currentUser.is_active ? 'btn-danger' : 'btn-success' }`"
        class="btn"
        type="submit"
      >
        {{ currentUser.is_active ? 'Deactivate' : 'Activate' }}
      </button>
    </div>
  </modal-component>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'user-status',
  computed: {
    ...mapState('users', [
      'currentUser'
    ])
  },
  methods: {
    ...mapActions('users', [
      'deleteUser'
    ])
  }
}
</script>
