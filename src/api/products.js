import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api/products';

export default {
  async fetchProducts() {
    try {
      const response = await axios.get(`${API_BASE_URL}/list/`);
      return response.data;
    } catch (error) {
      console.error('Error fetching products:', error);
      throw error;
    }
  },
};
