<template>
  <div class="home">
    <LoginView v-if="!isLoggedIn" />
  </div>
</template>

<script>
// @ is an alias to /src

import LoginView from '../views/accounts/LoginView.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'Home',
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  components: {
    LoginView,
  }
}
</script>

<style socped>
  body {
    background-image: url('../assets/Newyork.jpg');
    background-size: 100%;
  }
</style>