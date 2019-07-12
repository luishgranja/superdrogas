<template>
  <modal-component
    id="user-status"
    :title="`${ user.is_active ? 'Deactivate' : 'Activate' } user`"
  >
    <div class="row">
      <div class="col-sm-12">
        <p>
          Are you sure to
          <strong>{{ user.is_active ? 'deactivate' : 'activate' }}</strong>
          the user
          <strong>{{ user.first_name }} {{ user.last_name }}</strong>?
        </p>
      </div>
    </div>
    <div class="pull-right">
      <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
      <button
        @click="deleteUser"
        :class="`${ user.is_active ? 'btn-danger' : 'btn-success' }`"
        class="btn"
        type="submit"
      >
        {{ user.is_active ? 'Deactivate' : 'Activate' }}
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
      'user'
    ])
  },
  methods: {
    ...mapActions('users', [
      'deleteUser'
    ])
  }
}
</script>
