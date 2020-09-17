<template>
  <div class="container">
    <h1>건의 & 불편 신고</h1>
    <v-form>
      <v-autocomplete
        v-model="selected"
        :items="['Trevor Handsen', 'Alex Nelson']"
        chips
        label="Category"
        full-width
        hide-details
        hide-no-data
        hide-selected
        multiple
        single-line
      ></v-autocomplete>
      <v-divider></v-divider>
      <v-text-field
        label="Subject"
        value="Title"
        single-line
        full-width
        hide-details
      ></v-text-field>
      <v-divider></v-divider>
      <v-textarea
        v-model="title"
        label="Message"
        counter
        maxlength="120"
        full-width
        single-line
      ></v-textarea>
    </v-form>
    <div class="button">
      <input type="submit" style="text-align: right;" value="Submit">
    </div>
  </div>
</template>

<script>
  // const BACK_URL = 'http://127.0.0.1:8000'

  export default {
    name: 'QandA',
    data () {
      return {
        selected: [],
        items: [],
        title: '',
      }
    },
    // methods: {
    //   originInfo() {
    //     axios.post(`${BACK_URL}`/)
    //   }
    // }
  }
</script>

<style scoped>
  input[type='submit'] {
    background-color: #3d8fc5;
    color: #eee;
    font-weight: 700;
    text-transform: uppercase;
  }

  input[type='submit']:focus,
  input[type='submit']:hover {
    background-color: #073a5c;
  }

  .button {
    margin-top: 30px;
    text-align: right;
  }
</style>