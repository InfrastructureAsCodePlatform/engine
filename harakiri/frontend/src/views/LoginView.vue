<template>
  <div class="login">
    <a class="head-block" href="/">
      <span class="text-3xl font-bold mb-2">OpsGen</span>
    </a>
    <div class="login-form">
      <form @submit.prevent="login">
        <div class="form-input">
          <input placeholder="Email" type="text" v-model="credentials.email" />
        </div>
        <div class="form-input">
          <input placeholder="Password" type="password" v-model="credentials.password" />
        </div>
        <div class="form-button">
          <button>Log in</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { useUserStore } from '@/stores/user';

const credentials = ref({
  email: '',
  password: ''
});

const user = useUserStore();
const router = useRouter();

async function login() {
  const { email, password } = credentials.value;
  await user.login(email, password);
  await router.push('/');
}
</script>

<style>
.login {
  min-height: 100vh;
  max-width: 56rem;
  display: grid;
  align-items: center;
  align-content: center;
}

.login-form {
  margin-top: 1rem;
  background-color: white;
  overflow: hidden;
  border-radius: 0.5rem;
  --tw-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1),0 1px 2px 0 rgba(0, 0, 0, 0.06);
  padding: 1.5rem;
  --tw-bg-opacity: 1;
  box-shadow: 0 0.5rem 1rem rgb(0 0 0 / 15%);
}

.form-button {
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
  text-align: center;
}

.form-button button {
  cursor: pointer;
  transition-duration: 150ms;
  transition-timing-function: cubic-bezier(0.4,0,0.2,1);
  transition-property: background-color,border-color,color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter,-webkit-backdrop-filter;
  width: 100%;
  text-transform: uppercase;
  --tw-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),0 2px 4px -1px rgba(0, 0, 0, 0.06);
  box-shadow: var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow);
  padding: 0.625rem 1.5rem;
  line-height: 1.25;
  font-size: .75rem;
  font-weight: 800;
  display: inline-block;
  --tw-bg-opacity: 1;
  background-color: rgba(59,130,246,var(--tw-bg-opacity));
  -webkit-appearance: button;
  color: #fff;
  margin-bottom: 1rem;
  border-radius: 0.25rem;
  border: none;
}

.form-input {
  margin-bottom: 1.5rem;
}

.form-input input {
  border: 1px solid #dee2e6;
  margin: 0;
  background-clip: padding-box;
  display: block;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.5rem;
  padding: 0.375rem 1rem;
  --tw-text-opacity: 1;
  color: rgba(55,65,81,var(--tw-text-opacity));
  width: 100%;
  transition-duration: 150ms;
  transition-timing-function: cubic-bezier(0.4,0,0.2,1);
  border-radius: 0.25rem;
}

.head-block {
  display: flex;
  justify-content: center;
  text-decoration-color: #0a0e14;
}

.head-block span {
  font-size: 1.875rem;
  line-height: 2.25rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

@media (max-width: 1023px) {
  .login {
    min-height: 80vh;
    justify-content: center;
  }
}

.login a {
  color: lightgrey;
}

@media (hover: hover) {
  .login a:hover {
    background-color: transparent;
  }
}
</style>
