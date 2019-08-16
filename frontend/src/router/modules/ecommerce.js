import ECommerce from '@/components/ecommerce/ECommerce'
import Product from '@/components/ecommerce/Product'
import Cart from '@/components/ecommerce/Cart'
import Checkout from '@/components/ecommerce/Checkout'
import Shopping from '@/components/ecommerce/Shopping'

export default {
  path: '',
  component: ECommerce,
  children: [
    {
      path: '',
      component: Shopping,
      children: [
        {
          path: '',
          name: 'landing',
          component: Product
        },
        {
          path: 'cart',
          name: 'cart',
          component: Cart
        }
      ]
    },
    {
      path: 'checkout',
      name: 'checkout',
      component: Checkout
    }
  ]
}
