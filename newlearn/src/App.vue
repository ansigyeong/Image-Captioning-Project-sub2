<template>
  <v-app>
    <Header />
      <!-- <v-spacer></v-spacer> -->
    <v-main>
      <!-- <Signin /> --> 
      <Myinfo />
    </v-main>
  </v-app>
</template>

<script scoped>
import Header from './components/Header.vue'
// import Signin from './views/accounts/Signin.vue'
import Myinfo from './views/accounts/Myinfo'

export default {
  name: 'App',

  components: {
    Header,
    // Signin,
    Myinfo,
},

  data: () => ({
    //
  }),
};
</script>
