<template>           

  <div id="app">
    <div class="container mt-4">
      <h1 class="text-center">Our Products</h1>
      <div class="row">
        <div v-for="product in products" :key="product.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <div class="card">
            <img :src="product.image" class="card-img-top product-image" alt="Product Image">
            <div class="card-body">
              <h5 class="card-title">{{ product.item_name }}</h5>
              <p class="card-text">Price: ${{ product.new_price }}</p>
              <p class="card-text">Discount: {{ product.discount }}%</p>
              <p>Seller: {{ product.seller }}</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Pagination Controls -->
      <div class="pagination-container text-center mt-4">
        <button 
          class="btn btn-primary mx-1"
          :disabled="currentPage === 1"
          @click="fetchProducts(currentPage - 1)"
        >
          Previous
        </button>
        
        <span v-for="page in totalPages" :key="page">
          <button 
            class="btn btn-secondary mx-1"
            :class="{ 'btn-primary': page === currentPage }"
            @click="fetchProducts(page)"
          >
            {{ page }}
          </button>
        </span>
        
        <button 
          class="btn btn-primary mx-1"
          :disabled="currentPage === totalPages"
          @click="fetchProducts(currentPage + 1)"
        >
          Next
        </button>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      products: [],
      currentPage: 1,
      pageSize: 8,
      totalPages: 0,
    };
  },
  created() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts(page=1) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/products?page=${page}`);
        this.products = response.data.results || [];
        this.totalPages = Math.ceil(response.data.count / this.pageSize);
        this.currentPage = page;
      } catch (error) {
        console.error("There was an error fetching the products!", error);
      }
    }
  }
}
</script>

<style scoped>
.card {
  transition: box-shadow 0.3s ease;
}
.card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-img-top.product-image {
  max-width: 100%;
  height: 200px; /* Fixed height for images */
  object-fit: cover; /* Ensures proper image cropping */
}

/* Adjust column size for each product card */
.col-lg-3 {
  width: calc(100% / 4); /* Ensures 4 cards per row on large screens */
}

.row {
  display: flex;
  flex-wrap: wrap;
}
</style>
