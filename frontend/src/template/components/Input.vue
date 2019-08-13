<template>
  <div :class="`${ inputErrors ? 'has-error is-focused' : '' }`" class="form-group">
    <label v-if="label" :for="id">
      {{ placeholder }}
    </label>
    <input
      :id="id"
      :value="value"
      @input="$emit('input', $event.target.value)"
      :placeholder="placeholder"
      :type="type"
      class="form-control"
      :required="required"
    >
    <slot></slot>
    <span v-for="(error, index) in inputErrors" :key="index" class="help-block">
      {{ error }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'input-component',
  props: {
    id: {
      type: String,
      required: true
    },
    placeholder: {
      type: String,
      required: true
    },
    label: {
      type: Boolean,
      default: true
    },
    value: {
      type: [String, Number],
      default: ''
    },
    type: {
      type: String,
      default: 'text'
    },
    required: {
      type: Boolean,
      default: true
    },
    inputErrors: {
      type: Array,
      default: () => null
    }
  }
}
</script>
