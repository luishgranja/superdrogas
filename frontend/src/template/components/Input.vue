<template>
  <div :class="`${ inputErrors ? 'has-error is-focused' : '' }`" class="form-group">
    <input
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
    placeholder: {
      type: String,
      required: true
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
