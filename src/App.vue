<template>
  <div id="app">
    <Navbar @open-login-modal="showModal = true" />
    <Home />
    <!-- LoginModal listens for the close event -->
    <LoginModal v-if="showModal" @close="showModal = false" />
  </div>
</template>

<script>
import Home from './views/Home.vue';
import Navbar from './components/Navbar.vue';
import LoginModal from './components/LoginModal.vue';

export default {
  name: 'App',
  components: {
    Home,
    Navbar,
    LoginModal,
  },
  data() {
    return {
      showModal: false, // Controls the visibility of LoginModal
    };
  },
};
</script>
