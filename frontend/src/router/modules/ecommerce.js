import ECommerce from '@/components/ecommerce/ECommerce'
import Product from '@/components/ecommerce/Product'
import Cart from '@/components/ecommerce/Cart'

export default {
  path: '/ecommerce',
  component: ECommerce,
  children: [
    {
      path: '',
      name: 'product',
      component: Product
    },
    {
      path: '/cart',
      name: 'cart',
      component: Cart
    }
  ]
}
