import HomeView from '@/components/home/HomeView'
import Home from '@/components/home/apps/home/Home'
import Users from '@/components/home/apps/users/Users'
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
      path: 'products',
      name: 'products',
      component: Products
    }
  ]
}
