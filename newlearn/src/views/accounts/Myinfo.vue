<template>
  <v-app>

    <div class="container">
      <!-- 1. 프로필 카드 -->
      <v-card
        class="mx-auto"
        max-width="434"
        tile
      >
        <v-img
          height="100%"
          src="@/assets/profile_back_sample.jpg"
        >
          <v-row
            align="end"
            class="fill-height"
          >
            <v-col
              align-self="start"
              class="pa-0"
              cols="12"
            >
              <v-avatar
                class="profile"
                color="grey"
                size="164"
                tile
              >
                <v-img src="@/assets/profile_sample.jpg"></v-img>
              </v-avatar>
            </v-col>
            <v-col class="py-0">
              <v-list-item
                color="rgba(0, 0, 0, .4)"
                dark
              >
                <v-list-item-content>
                  <v-list-item-title class="title"><h1>Ko younghee</h1></v-list-item-title>
                  <v-list-item-subtitle><h2>Network Engineer</h2></v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-col>
          </v-row>
        </v-img>
      </v-card>

      <br>
      <br>

      <!-- 2. 회원 정보 수정(닉네임, 비밀번호, 비밀번호 확인) & 회원탈퇴  -->
      <form class="user_info">
        <v-text-field
          v-model="name"
          :error-messages="nameErrors"
          :counter="10"
          label="Goyounghee@gmail.com"
          required
          @input="$v.name.$touch()"
          @blur="$v.name.$touch()"
        ></v-text-field>
        <div>
          <div class="form-group" :class="{ 'form-group--error': $v.password.$error }">
            <!-- <label class="form__label">Password</label> -->
            <v-text-field label="●●●●●●●●" class="form__input" v-model.trim="$v.password.$model"/>
          </div>
          <!-- <div class="error" v-if="!$v.password.required" style="font-style: italic; color: red;"><small>Password is required.</small></div>
          <div class="error" v-if="!$v.password.minLength" style="font-style: italic; color: red;"><small>Password must have at least {{ $v.password.$params.minLength.min }} letters.</small></div> -->
          <div class="form-group" :class="{ 'form-group--error': $v.repeatPassword.$error }">
            <!-- <label class="form__label">Repeat password</label> -->
            <v-text-field label="●●●●●●●●" class="form__input" v-model.trim="$v.repeatPassword.$model"/>
          </div>
          <!-- <div class="error" v-if="!$v.repeatPassword.sameAsPassword" style="font-style: italic; color: red;"><small>Passwords must be identical.</small></div> -->
          <tree-view :data="$v" :options="{rootObjectKey: '$v', maxDepth: 2}"></tree-view>
        </div>
        <br>
        <br>
        <div class="button">
          <v-btn class="mr-4" @click="submit">Save Profile</v-btn>
          <v-btn @click="clear">Delete Account</v-btn>
        </div>
      </form>
    </div>
  </v-app>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import { required, maxLength, sameAs, minLength } from 'vuelidate/lib/validators'

  export default {
    name: 'Myinfo',
    components: {
    },
    mixins: [validationMixin],
    validations: {
      name: { required, maxLength: maxLength(10) },
      password: {
        required,
        minLength: minLength(6)
      },
      repeatPassword: {
        sameAsPassword: sameAs('password')
      },
    },

    data: () => ({
      name: '',
      password: '',
      repeatPassword: '',
    }),

    computed: {
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
        !this.$v.name.required && errors.push('Name is required.')
        return errors
      },
    },

    methods: {
      submit () {
        this.$v.$touch()
      },
      clear () {
        this.$v.$reset()
        this.name = ''
        this.password = ''
        this.select = null
        this.checkbox = false
      },
    },
  }
</script>

<style scoped>
  /* form {
    max-width: 50%;
  } */
  .user_info {
    max-width: 50%;
    margin: auto;
  }
  .v-application .error {
    background-color: white !important;
    border-color: white !important;
  }
  .button {
    text-align: center !important;
    justify-content: center !important;
  }  
</style>