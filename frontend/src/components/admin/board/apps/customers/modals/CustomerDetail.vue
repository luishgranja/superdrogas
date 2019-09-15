<template>
  <modal-component id="user-detail" title="Customer detail">
    <div class="row">
      <div class="col-sm-12">
        <ul>
          <li>
            <strong>Name:</strong>
            {{ user.first_name }} {{ user.last_name }}
          </li>
          <li>
            <strong>Username:</strong>
            {{ user.username }}
          </li>
          <li>
            <strong>Email:</strong>
            {{ user.email }}
          </li>
          <li>
            <strong>Status:</strong>
            {{ user.is_active ? 'Active' : 'Inactive' }}
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
  name: 'customer-detail',
  computed: {
    ...mapState('users', [
      'user'
    ])
  }
}
</script>
