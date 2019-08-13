<template>
<section class="invoice">
      <!-- title row -->
      <div class="row">
        <div class="col-xs-12">
          <h2 class="page-header">
            <i class="fa fa-globe"></i> Superdrogas, Inc.
            <small class="pull-right">Date: {{ sale_invoice.date }}</small>
          </h2>
        </div>
        <!-- /.col -->
      </div>
      <!-- info row -->
      <div class="row invoice-info">
        <div class="col-sm-4 invoice-col">
          From
          <address>
            <strong>Admin, Inc.</strong><br>
            795 Folsom Ave, Suite 600<br>
            San Francisco, CA 94107<br>
            Phone: (804) 123-5432<br>
            Email: info@almasaeedstudio.com
          </address>
        </div>
        <!-- /.col -->
        <div class="col-sm-4 invoice-col">
          To
          <address>
            <strong>John Doe</strong><br>
            795 Folsom Ave, Suite 600<br>
            San Francisco, CA 94107<br>
            Phone: (555) 539-1037<br>
            Email: john.doe@example.com
          </address>
        </div>
        <!-- /.col -->
        <div class="col-sm-4 invoice-col">
          <b>Invoice #{{ sale_invoice.id }}</b><br>
          <br>          
          <b>Account:</b> 968-34567
        </div>
        <!-- /.col -->
      </div>
      <!-- /.row -->

      <!-- Table row -->
      <div class="row">
        <div class="col-xs-12 table-responsive">
          <table class="table table-striped">
            <thead>
            <tr>
              <th>Qty</th>
              <th>Product</th>
              <th>Description</th>
              <th>Unit Price</th>
              <th>Subtotal</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(product, index) in products_invoice" :key="index">
              <td>{{ product.quantity }}</td>
              <td>{{ product.product_name }}</td>
              <td>{{ product.product_description }}</td>
              <td>{{ product.total_price }}</td>
              <td>{{ product.product_subtotal }}</td>
            </tr>            
            </tbody>
          </table>
        </div>
        <!-- /.col -->
      </div>
      <!-- /.row -->

      <div class="row">
        <!-- accepted payments column -->
        <div class="col-xs-6">          
          <p class="text-muted well well-sm no-shadow" style="margin-top: 10px;">
            Etsy doostang zoodles disqus groupon greplin oooj voxy zoodles, weebly ning heekya handango imeem plugg
            dopplr jibjab, movity jajah plickers sifteo edmodo ifttt zimbra.
          </p>
        </div>
        <!-- /.col -->
        <div class="col-xs-6">
          <p class="lead">Amount Due {{ sale_invoice.date }}</p>

          <div class="table-responsive">
            <table class="table">
              <tbody>
              <tr>
                <th style="width:50%">Subtotal:</th>
                <td>${{ noIva }}</td>
              </tr>
              <tr>
                <th>Tax (19%)</th>
                <td>${{ iva }}</td>
              </tr>
              <tr>
                <th>Total:</th>
                <td>${{ sale_invoice.total_amount }}</td>
              </tr>
            </tbody></table>
          </div>
        </div>
        <!-- /.col -->
      </div>
      <!-- /.row -->

      <!-- this row will not appear when printing -->
      <div class="row no-print">
        <div class="col-xs-12">
          <a href="invoice-print.html" target="_blank" class="btn btn-default"><i class="fa fa-print"></i> Print</a>
          <button type="button" class="btn btn-success pull-right"><i class="fa fa-credit-card"></i> Submit Payment
          </button>
          <button type="button" class="btn btn-primary pull-right" style="margin-right: 5px;">
            <i class="fa fa-download"></i> Generate PDF
          </button>
        </div>
      </div>
    </section>
  </template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'
import template from '@/utilities/template'
export default {
  name: 'checkout',  
  computed: {
      ...mapState('ecommerce', [
      'sale_invoice',
      'products_invoice'
    ]),
    ...mapGetters('ecommerce', [
      'noIva',
      'iva'      
    ]),
    total () {
      return this.cartProducts.reduce((total, p) => {
        return total + p.price * p.quantity
      }, 0)
    }
  },
  methods: {
    ...mapActions('ecommerce', [
      'deleteFromCart'
    ]),
    ...mapActions('products', [      
      'getProduct'
    ]),
    checkout () {
      alert('Pay us $' + this.total)
    }
  }
}
</script>