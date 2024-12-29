<template>
  <div>
    <!-- Login Button -->
    <button type="button" class="btn btn-primary" @click="showModal = true">
      Login
    </button>

    <!-- Login Modal -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Login</h5>
          <button type="button" class="btn-close" @click="showModal = false">&times;</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitLogin">
            <div class="mb-3">
              <label for="email" class="form-label">Email address</label>
              <input
                type="email"
                id="email"
                v-model="email"
                class="form-control"
                required
              />
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input
                type="password"
                id="password"
                v-model="password"
                class="form-control"
                required
              />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"; // Ensure axios is imported

export default {
  data() {
    return {
      showModal: false,
      email: "",
      password: "",
    };
  },
  methods: {
    async submitLogin() {
      try {
        const response = await axios.post("http://127.0.0.1:8000/api/login", {
          email: this.email,
          password: this.password,
        });
        console.log("Login Successful:", response.data);
        this.showModal = false;
      } catch (error) {
        console.error("Login Failed:", error.response.data);
      }
    },
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 5px;
  width: 400px;
  max-width: 90%;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.btn-close {
  background: transparent;
  border: none;
  font-size: 1.2rem;
}
</style>
