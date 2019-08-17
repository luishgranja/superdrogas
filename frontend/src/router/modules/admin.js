import Admin from '@/components/admin/Admin'
import Login from '@/components/admin/login/Login'
import Board from '@/components/admin/board/Board'
import Home from '@/components/admin/board/apps/home/Home'
import Batches from '@/components/admin/board/apps/batches/Batches'
import Brands from '@/components/admin/board/apps/brands/Brands'
import Categories from '@/components/admin/board/apps/categories/Categories'
import Configurations from '@/components/admin/board/apps/configurations/Configurations'
import Customers from '@/components/admin/board/apps/customers/Customers'
import Metrics from '@/components/admin/board/apps/metrics/Metrics'
import Products from '@/components/admin/board/apps/products/Products'
import Reports from '@/components/admin/board/apps/reports/Reports'
import Sales from '@/components/admin/board/apps/sales/Sales'
import Tenants from '@/components/admin/board/apps/tenants/Tenants'
import Users from '@/components/admin/board/apps/users/Users'

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
          path: 'categories',
          name: 'categories',
          component: Categories
        },
        {
          path: 'configurations',
          name: 'configurations',
          component: Configurations
        },
        {
          path: 'customers',
          name: 'customers',
          component: Customers
        },
        {
          path: 'metrics',
          name: 'metrics',
          component: Metrics
        },
        {
          path: 'products',
          name: 'products',
          component: Products
        },
        {
          path: 'reports',
          name: 'reports',
          component: Reports
        },
        {
          path: 'sales',
          name: 'sales',
          component: Sales
        },
        {
          path: 'tenants',
          name: 'tenants',
          component: Tenants
        },
        {
          path: 'users',
          name: 'users',
          component: Users
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
