<template>
  <v-app>
    <Header> </Header>
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link v-if="!isLoggedIn" :to="{ name: 'Login' }">Login</router-link> | 
      <router-link v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup</router-link>
      <router-link v-if="isLoggedIn" :to="{ name: 'Logout' }">Logout</router-link>
    </div> -->
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <!-- <router-link :to="{ name: 'Login' }">Login</router-link> |  -->
      <!-- <router-link :to="{ name: 'Signup' }">Signup</router-link> | -->
      <!-- <router-link :to="{ name: 'Logout' }">Logout</router-link> -->
      <router-link :to="{ name: 'Myinfo' }">My Information</router-link> |
      <router-link :to="{ name: 'Pointlist' }">Point List</router-link> |
      <router-link :to="{ name: 'Attendance' }">Attendace</router-link>

    </div>
    <router-view />
    <!-- <v-spacer></v-spacer>
    <v-main>
    </v-main> -->
  </v-app>
</template>

<script scoped>
import Header from './components/Header.vue'

import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  componenets : {
    Header,
  },
  methods: {
  },
  
}
</script>

<style scoped>

</style>
