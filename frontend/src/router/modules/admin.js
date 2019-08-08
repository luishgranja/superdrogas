import Admin from '@/components/admin/Admin'
import Board from '@/components/admin/board/Board'
import Home from '@/components/admin/board/apps/home/Home'
import Users from '@/components/admin/board/apps/users/Users'
import Batches from '@/components/admin/board/apps/batches/Batches'
import Products from '@/components/admin/board/apps/products/Products'
import Login from '@/components/admin/login/Login'

export default {
  path: '/admin',
  component: Admin,
  children: [
    {
      path: '',
      component: Board,
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
    },
    {
      path: 'login',
      name: 'login',
      component: Login
    }
  ]
}
