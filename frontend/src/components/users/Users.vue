<template>
  <div class="va-row">
    <div class="flex md12 xs12">
      <vuestic-widget headerText="Users">
        <vuestic-data-table
          :apiUrl="apiUrl"
          :tableFields="tableFields"
          :itemsPerPage="itemsPerPage"
          :defaultPerPage="defaultTablePerPage"
          :sortFunctions="sortFunctions"
          :apiMode="apiMode"
          :paginationPath="paginationPath"
          :queryParams="queryParams"
          :perPageSelectorShown="perPageSelectorShown"
        >
          <spring-spinner
            slot="loading"
            :animation-duration="2500"
            :size="70"
            color="#4ae387"
          />
        </vuestic-data-table>
      </vuestic-widget>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import BadgeColumn from '@/components/tables/BadgeColumn'
import { SpringSpinner } from 'epic-spinners'

Vue.component('badge-column', BadgeColumn)

export default {
  name: 'users',
  components: {
    SpringSpinner,
  },
  data () {
    return {
      apiUrl: 'https://vuetable.ratiw.net/api/users',
      apiMode: true,
      tableFields: [
        {
          name: '__component:badge-column',
          title: '',
          dataClass: 'text-center',
          width: '4%',
        },
        {
          name: 'name',
          sortField: 'name',
          width: '24%',
        },
        {
          name: 'email',
          sortField: 'email',
          width: '24%',
        },
        {
          name: 'address.line2',
          title: 'city',
          width: '24%',
        },
        {
          name: 'salary',
          title: 'score',
          width: '24%',
        },
      ],
      itemsPerPage: [
        { value: 5 },
        { value: 6 },
        { value: 10 },
      ],
      sortFunctions: {
        'name': function (item1, item2) {
          return item1 >= item2 ? 1 : -1
        },
        'email': function (item1, item2) {
          return item1 >= item2 ? 1 : -1
        },
      },
      paginationPath: '',
      defaultTablePerPage: 6,
      queryParams: {
        sort: 'sort',
        page: 'page',
        perPage: 'per_page'
      },
      perPageSelectorShown: true
    }
  }
}
</script>
