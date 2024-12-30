<template>
  <div class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Login</h5>
        <!-- Emit 'close' event when the close button is clicked -->
        <button type="button" class="btn-close" @click="$emit('close')">
          &times;
        </button>
      </div>
      <div class="modal-body">
        <form @submit.prevent="submitLogin">
          <div class="mb-3">
            <label for="email" class="form-label">Email Address</label>
            <input
              type="email"
              id="email"
              v-model="email"
              class="form-control"
              placeholder="Enter your email"
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
              placeholder="Enter your password"
              required
            />
          </div>
          <div class="d-flex justify-content-between align-items-center">
            <button type="submit" class="btn btn-primary w-100">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
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
        // Emit 'close' event to hide the modal after successful login
        this.$emit("close");
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
  background: #fff;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  width: 400px;
  max-width: 90%;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #dee2e6;
  padding-bottom: 10px;
  margin-bottom: 20px;
}

.modal-title {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.modal-body {
  padding: 0;
}

.form-label {
  font-weight: 500;
  margin-bottom: 5px;
  display: inline-block;
}

.form-control {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ced4da;
  font-size: 1rem;
  width: 100%;
}

.btn-close {
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}

.btn-close:hover {
  color: red;
}

button.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  padding: 10px 15px;
  font-size: 1rem;
  border-radius: 5px;
}

button.btn-primary:hover {
  background-color: #0056b3;
}
</style>
