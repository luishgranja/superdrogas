<template>
  <modal-component id="user-form" title="Create user">
    <form>
      <div class="row">
        <div class="form-group col-sm-6">
          <input
            placeholder="Username"
            type="text"
            class="form-control"
            required
          />
        </div>
        <div class="form-group col-sm-6">
          <input
            placeholder="Email address"
            type="email"
            class="form-control"
            required
          />
        </div>
        <div class="form-group col-sm-6">
          <input
            placeholder="First name"
            type="text"
            class="form-control"
            required
          />
        </div>
        <div class="form-group col-sm-6">
          <input
            placeholder="Last name"
            type="text"
            class="form-control"
            required
          />
        </div>
        <div class="form-group col-sm-6">
          <input
            placeholder="Password"
            type="password"
            class="form-control"
            required
          />
        </div>
        <div class="form-group col-sm-6">
          <input
            placeholder="Password confirmation"
            type="password"
            class="form-control"
            required
          />
        </div>
      </div>
      <div class="pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button type="submit" class="btn btn-success">Create</button>
      </div>
    </form>
  </modal-component>
</template>

<script>
export default {
  name: 'create-user'
}
</script>
