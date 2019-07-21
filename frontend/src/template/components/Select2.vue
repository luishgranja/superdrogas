<template>
  <select class="form-control select2" style="width: 100%;">
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
    }
  },
  mounted: function () {
    var vm = this
    // eslint-disable-next-line
    $('.select2')
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
      $('.select2')
        .val(value)
        .trigger('change')
    },
    options: function (options) {
      // eslint-disable-next-line
      $('.select2').empty().select2({ data: options })
    }
  },
  destroyed: function () {
    // eslint-disable-next-line
    $('.select2').off().select2('destroy')
  }
}
</script>
