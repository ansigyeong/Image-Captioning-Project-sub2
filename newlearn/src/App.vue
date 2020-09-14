<template>
  <div>
    <Sign />
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link :to="{ name: 'Login' }">Login</router-link>
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link> | 
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link>
      <router-link v-if="isLoggedIn" :to="{ name: 'Logout' }">Logout</router-link>
    </div>
    <router-view /> -->
    
  </div>
</template>

<script>
// import { mapGetters } from 'vuex'
import Sign from './components/Sign.vue'

export default {
  name: 'App',
  computed: {
    // ...mapGetters(['isLoggedIn'])
  },
  componenets : [
    Sign
  ],
  methods: {
  },
  
}
</script>

<style scoped>

</style>
