<template>
  <div class="max-w-4xl mx-auto sm:px-6 lg:px-8">
    <a class="flex justify-center pt-8 sm:pt-0 nd" href="/">
      <span class="text-3xl font-bold mb-2">OpsGen</span>
    </a>
    <div class="mt-4 bg-white overflow-hidden shadow sm:rounded-lg p-6">
      <form @submit.prevent="userLogin">
        <div class="mb-4">
          <input type="text"
                 placeholder="Username"
                 class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                 v-model="login.username" />
        </div>
        <div class="mb-4">
          <input type="password"
                 placeholder="Password"
                 class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                 v-model="login.password" />
        </div>
        <div class="text-center pt-1 pb-1">
          <button class="inline-block px-6 py-2.5 text-white font-medium text-xs leading-tight uppercase rounded shadow-md bg-blue-500 hover:bg-blue-700 hover:shadow-lg focus:shadow-lg focus:outline-none focus:ring-0 active:shadow-lg transition duration-150 ease-in-out w-full mb-3"
                  type="submit"
                  data-mdb-ripple="true"
                  data-mdb-ripple-color="light"
                  style="
                        background: linear-gradient(
                          to right,
                          #ee7724,
                          #d8363a,
                          #dd3675,
                          #b44593
                        );
                      ">
            Log in
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      login: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async userLogin() {
      try {
        const { username: email, password } = this.login;
        await this.$auth.loginWith('local', { data: { email, password } });
      } catch (err) {
        console.log(err)
      }
    }
  }
}
</script>

<style>
.nd {
  text-decoration: none;
}

.nd:hover {
  text-decoration: none;
  color: inherit;
}
</style>