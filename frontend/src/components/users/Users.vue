<template>
  <div class="va-row">
    <div class="flex md12 xs12">
      <vuestic-widget headerText="Users">
        <vuestic-data-table
          :apiUrl="apiUrl"
          :tableFields="tableFields"
          :itemsPerPage="itemsPerPage"
          :sortFunctions="sortFunctions"
          :apiMode="apiMode"
          :paginationPath="paginationPath"
        ></vuestic-data-table>
      </vuestic-widget>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import BadgeColumn from '@/components/tables/BadgeColumn'

Vue.component('badge-column', BadgeColumn)

export default {
  data () {
    return {
      apiUrl: 'https://vuetable.ratiw.net/api/users',
      apiMode: true,
      tableFields: [
        {
          name: '__component:badge-column',
          title: '',
          dataClass: 'text-center'
        },
        {
          name: 'name',
          sortField: 'name'
        },
        {
          name: 'email',
          sortField: 'email'
        },
        {
          name: 'address.line2',
          title: 'city'
        },
        {
          name: 'salary',
          title: 'score'
        }
      ],
      itemsPerPage: [
        {
          value: 5
        },
        {
          value: 6
        },
        {
          value: 10
        }
      ],
      sortFunctions: {
        name: function (item1, item2) {
          return item1 >= item2 ? 1 : -1
        },
        email: function (item1, item2) {
          return item1 >= item2 ? 1 : -1
        }
      },
      paginationPath: ''
    }
  }
}
</script>
