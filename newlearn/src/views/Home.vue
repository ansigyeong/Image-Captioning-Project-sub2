<template>
  <div class="home">
    <Header></Header>
    <h1>Home Page</h1>
  </div>
</template>

<script>
// @ is an alias to /src

import Header from '../components/Header.vue'

export default {
  name: 'Home',
  components: {
    Header,
  }
}
</script>
