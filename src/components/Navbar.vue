<template>
    <nav class="navbar">
      <div class="navbar-left">
        <a href="#" class="nav-link">Home</a>
        <a href="#" class="nav-link">Product List</a>
      </div>
      <div class="navbar-right">
        <span class="nav-link" @click="openLoginModal">Login</span>
      </div>
    </nav>
  </template>


  
  <script>
  import LoginModal from "./LoginModal.vue";  

  export default {

    components: {
        LoginModal,
    },

    methods: {
        
      openLoginModal() {
        // Emit an event to open the modal
        this.$emit("open-login-modal");
      },
    },
  };
  </script>
  
  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #1180ac;
    padding: 10px 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .navbar-left {
    display: flex;
    gap: 15px;
  }
  
  .navbar-right {
    display: flex;
    align-items: center;
  }
  
  .nav-link {
    cursor: pointer;
    color: #00ffff;
    text-decoration: none;
    font-size: 1rem;
    font-weight: 500;
  }
  
  .nav-link:hover {
    text-decoration: underline;
  }
  </style>
  