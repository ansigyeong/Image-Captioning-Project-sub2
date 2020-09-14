<template>
  <v-app>
    <Header />
      <v-spacer></v-spacer>
    <v-main>
      <Signin />
    </v-main>
  </v-app>
</template>

<script scoped>
import Header from './components/Header.vue';
import Signin from './views/Signin.vue'

export default {
  name: 'App',

  components: {
    Header,
    Signin,
},

  data: () => ({
    //
  }),
};
</script>
