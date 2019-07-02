import HomeView from '@/views/home/Home'

import Home from '@/components/home/Home'
import Users from '@/components/users/Users'

export default {
  path: '/home',
  component: HomeView,
  children: [
    {
      path: '',
      name: 'home',
      component: Home
    },
    {
      path: 'users',
      name: 'users',
      component: Users
    }
  ]
}
