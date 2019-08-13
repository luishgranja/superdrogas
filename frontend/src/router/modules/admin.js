import Admin from '@/components/admin/Admin'
import Login from '@/components/admin/login/Login'
import Board from '@/components/admin/board/Board'
import Home from '@/components/admin/board/apps/home/Home'
import Users from '@/components/admin/board/apps/users/Users'
import Batches from '@/components/admin/board/apps/batches/Batches'
import Brands from '@/components/admin/board/apps/brands/Brands'
import Categories from '@/components/admin/board/apps/categories/Categories'
import Tenants from '@/components/admin/board/apps/tenants/Tenants'
import Products from '@/components/admin/board/apps/products/Products'

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
          path: 'brands',
          name: 'brands',
          component: Brands
        },
        {
          path: 'products',
          name: 'products',
          component: Products
        },
        {
          path: 'categories',
          name: 'categories',
          component: Categories
        },
        {
          path: 'tenants',
          name: 'tenants',
          component: Tenants
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
