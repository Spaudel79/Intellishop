<template>
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-section">
          <p>&copy; 2024 Your Company Name. All Rights Reserved.</p>
        </div>
        <div class="footer-section">
          <ul class="footer-links">
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/product-list">Products</router-link></li>
            <li><router-link to="/contact">Contact Us</router-link></li>
          </ul>
        </div>
        <div class="footer-section">
          <p>Follow us:</p>
          <div class="social-icons">
            <a href="https://facebook.com" target="_blank" aria-label="Facebook">
              <i class="fab fa-facebook"></i>
            </a>
            <a href="https://twitter.com" target="_blank" aria-label="Twitter">
              <i class="fab fa-twitter"></i>
            </a>
            <a href="https://instagram.com" target="_blank" aria-label="Instagram">
              <i class="fab fa-instagram"></i>
            </a>
          </div>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: "Footer",
  };
  </script>
  
  <style scoped>
  .footer {
    background-color: #f8f9fa;
    padding: 20px 0;
    text-align: center;
    border-top: 1px solid #e7e7e7;
  }
  
  .footer-content {
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
  }
  
  .footer-section {
    margin: 10px;
  }
  
  .footer-links {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .footer-links li {
    display: inline;
    margin: 0 10px;
  }
  
  .footer-links a {
    text-decoration: none;
    color: #007bff;
    transition: color 0.3s;
  }
  
  .footer-links a:hover {
    color: #0056b3;
  }
  
  .social-icons {
    display: flex;
    gap: 10px;
    justify-content: center;
  }
  
  .social-icons a {
    text-decoration: none;
    color: #495057;
    font-size: 20px;
  }
  
  .social-icons a:hover {
    color: #007bff;
  }
  </style>
  