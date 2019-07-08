<template>
  <modal-component id="user-detail" title="User detail">
    <div class="row">
      <div class="col-sm-12">
        <ul>
          <li>
            <strong>Name:</strong>
            {{ currentUser.first_name }} {{ currentUser.last_name }}
          </li>
          <li>
            <strong>Username:</strong>
            {{ currentUser.username }}
          </li>
          <li>
            <strong>Email:</strong>
            {{ currentUser.email }}
          </li>
          <li>
            <strong>Status:</strong>
            {{ currentUser.is_active ? 'Active' : 'Inactive' }}
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
  name: 'user-detail',
  computed: {
    ...mapState('users', [
      'currentUser'
    ])
  }
}
</script>
