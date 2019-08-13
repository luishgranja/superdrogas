import ECommerce from '@/components/ecommerce/ECommerce'
import Product from '@/components/ecommerce/Product'
import Cart from '@/components/ecommerce/Cart'
import Checkout from '@/components/ecommerce/Checkout'
import Shopping from '@/components/ecommerce/Shopping'

export default {
  path: '/ecommerce',
  component: ECommerce,
  children: [
    {
      path: '',      
      component: Shopping,
      children: [
        {
          path: '',
          name: 'product',
          component: Product
        },
        {
          path: 'cart',
          name: 'cart',
          component: Cart,
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
