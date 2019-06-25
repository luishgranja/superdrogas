<template>
  <vuestic-navbar>
    <header-selector
      slot="selector"
      :isOpen.sync="valueProxy"
    />
    <vuestic-icon-vuestic slot="logo" />
    <notification-dropdown class="col nav-item" />
    <profile-dropdown class="col nav-item"></profile-dropdown>
  </vuestic-navbar>
</template>

<script>
import VuesticNavbar from '@/vuestic-theme/vuestic-components/vuestic-navbar/VuesticNavbar'
import VuesticIconVuestic from '@/vuestic-theme/vuestic-components/vuestic-icon/VuesticIconVuestic'

import HeaderSelector from './components/HeaderSelector'
import NotificationDropdown from './components/dropdowns/NotificationDropdown'
import ProfileDropdown from './components/dropdowns/ProfileDropdown'

export default {
  name: 'app-navbar',
  components: {
    VuesticNavbar,
    VuesticIconVuestic,
    HeaderSelector,
    NotificationDropdown,
    ProfileDropdown
  },
  props: {
    isOpen: {
      type: Boolean,
      required: true
    },
  },
  computed: {
    valueProxy: {
      get () {
        return this.isOpen
      },
      set (opened) {
        this.$emit('toggle-menu', opened)
      },
    },
  },
}
</script>
