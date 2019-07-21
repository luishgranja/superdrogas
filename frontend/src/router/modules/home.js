import HomeView from '@/components/home/HomeView'
import Home from '@/components/home/apps/home/Home'
import Users from '@/components/home/apps/users/Users'
import Batches from '@/components/home/apps/batches/Batches'

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
    },
    {
      path: 'batches',
      name: 'batches',
      component: Batches
    }
  ]
}
