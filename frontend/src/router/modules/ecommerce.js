import ECommerce from '@/components/ecommerce/ECommerce'

import LandingPage from '@/components/ecommerce/views/LandingPage'
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
      path: 'cart',
      name: 'cart',
      component: ShoppingCart
    },
    {
      path: 'checkout',
      name: 'checkout',
      component: Checkout
    }
  ]
}
