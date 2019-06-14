<template>
  <div class="profile-dropdown flex-center">
    <h4 class="m-0">Iván Toro</h4>
    <vuestic-dropdown
      v-model="isShown"
      position="bottom"
    >
      <div
        v-for="option in options"
        :key="option.name"
        class="dropdown-item plain-link-item"
      >
        <router-link
          :to="{ name: option.redirectTo }"
          class="plain-link"
          href="#"
        >
          {{ $t(`user.${option.name}`) }}
        </router-link>
      </div>
    </vuestic-dropdown>
  </div>
</template>

<script>
export default {
  name: 'profile-section',
  data () {
    return {
      isShown: false,
    }
  },
  props: {
    options: {
      type: Array,
      default: () => [
        {
          name: 'profile',
          redirectTo: '',
        },
        {
          name: 'logout',
          redirectTo: '',
        },
      ],
    },
  },
}
</script>

<style lang="scss">
@import "~@/vuestic-theme/vuestic-sass/resources/resources";

.profile-dropdown {
  cursor: pointer;
  color: $vue-green;
}
</style>
