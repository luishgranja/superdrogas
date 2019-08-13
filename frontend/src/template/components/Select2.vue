<template>
  <select :id="id" class="form-control" style="width: 100%;">
    <slot></slot>
  </select>
</template>

<script>
export default {
  name: 'select2',
  props: {
    options: {
      type: Array,
      default: () => []
    },
    value: {
      type: Number,
      default: 0
    },
    id: {
      type: String,
      default: 'select2'
    }
  },
  mounted: function () {
    var vm = this
    // eslint-disable-next-line
    $(`#${this.id}`)
      .select2({ data: this.options })
      .val(this.value)
      .trigger('change')
      .on('change', function () {
        vm.$emit('input', this.value)
      })
  },
  watch: {
    value: function (value) {
      // eslint-disable-next-line
      $(`#${this.id}`)
        .val(value)
        .trigger('change')
    },
    options: function (options) {
      // eslint-disable-next-line
      $(`#${this.id}`).empty().select2({ data: options })
    }
  },
  destroyed: function () {
    // eslint-disable-next-line
    $(`#${this.id}`).off().select2('destroy')
  }
}
</script>
