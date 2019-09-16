import ECommerce from '@/components/ecommerce/ECommerce'
import LandingPage from '@/components/ecommerce/views/LandingPage'
import Login from '@/components/ecommerce/views/Login'
import ShoppingCart from '@/components/ecommerce/views/ShoppingCart'
import Checkout from '@/components/ecommerce/views/Checkout'

export default {
  path: '',
  component: ECommerce,
  children: [
    {
      path: '',
      name: 'landing',
      component: LandingPage
    },
    {
      path: 'login',
      name: 'login-ecommerce',
      component: Login
    },
    {
      path: 'shopping-cart',
      name: 'shopping-cart',
      component: ShoppingCart
    },
    {
      path: 'checkout',
      name: 'checkout',
      component: Checkout
    }
  ]
}
