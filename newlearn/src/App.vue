<template>
  <div>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link> | 
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link>
      <router-link v-if="isLoggedIn" :to="{ name: 'Logout' }">Logout</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  componenets : [
  ],
  methods: {
  },
  
}
</script>

<style scoped>

</style>
