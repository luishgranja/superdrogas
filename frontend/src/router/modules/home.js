import HomeView from '@/components/home/HomeView'
import Home from '@/components/home/apps/home/Home'
import Users from '@/components/home/apps/users/Users'
import Batches from '@/components/home/apps/batches/Batches'
import Products from '@/components/home/apps/products/Products'

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
    },
    {
      path: 'products',
      name: 'products',
      component: Products
    }
  ]
}
