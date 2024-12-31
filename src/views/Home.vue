<template>

<div>
    <ProductList />
    <Footer />
</div>
    
</template>
  
  <script>
  import ProductAPI from '@/api/products';
  import ProductList from '../components/ProductList.vue';
  import Footer from '../components/Footer.vue';
  
  export default {
    name:'Home',
    components: {
    Footer,
    ProductList, 
    
  }
    
  }
  </script>
  
  