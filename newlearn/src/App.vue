<template>
  <v-app id="app">
    <Header/>
    <main>
    </main>
  </v-app>
</template>

<script scoped>

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
