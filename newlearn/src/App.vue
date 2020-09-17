<template>
  <v-app id="app">
    <Header/>
    <main>
      <div id="nav">
        <router-link to="/">Home</router-link> |
        <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link> | 
        <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link>
        <router-link v-if="isLoggedIn" :to="{ name: 'Logout' }">Logout</router-link>
      </div>
      <router-view />
    </main>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'
import Header from './components/Header.vue'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  components : {
    Header,
  },
  methods: {
  },
  
}
</script>

<style scoped>

</style>
