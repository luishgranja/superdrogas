<template>
  <div :class="`${ erros ? 'has-error' : '' }`" class="form-group col-sm-6">
    <label :for="id">
      {{ label }}
    </label>
    <input
      :id="id"
      :value="value"
      @input="updateValue"
      :placeholder="label"
      :type="type"
      class="form-control"
      :required="required"
    >
    <slot></slot>
    <span v-for="(error, index) in erros" :key="index" class="help-block">
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
    label: {
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
    erros: {
      type: Array,
      default: () => null
    }
  },
  methods: {
    updateValue (event) {
      this.$emit('input', event.target.value)
    }
  }
}
</script>
