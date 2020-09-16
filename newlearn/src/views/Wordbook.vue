<template>
    <div>
        <h1>워드북</h1>
        <v-btn @click="callToeicVocabulary">
            토익 단어 가져오기
        </v-btn>
        <v-btn @click="callOpicVocabulary">
            오픽 단어 가져오기
        </v-btn>
        <v-btn @click="callSATVocabulary">
            수능 단어 가져오기
        </v-btn>
        <div v-if="words">
            {{ $moment(today).format('YY년 MM월 DD일') }}의 단어
            <li v-for="(word) in words" :key="word.pid">
                {{ word.word }} : {{ word.mean }}
            </li>
        </div>
    </div>
</template>

<script>
import axios from "axios"

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    data () {
      return {
        words: JSON.parse(localStorage.getItem("words")),
        today: localStorage.getItem("today"),
        choice: '',
      }
    },
    created() {
        // console.log(localStorage.words)
    }
    ,
    methods: {
        callVocabulary(choice) {
            axios.post(`${BACK_URL}/english/vocabulary/`, choice)
            .then(res => {
                this.words = res.data.vocabulary
                localStorage.setItem("words", JSON.stringify(this.words))
                this.today = res.data.today
                localStorage.today = this.today
            })
        },
        callToeicVocabulary() {
            this.choice = {'Toeic': true}
            this.callVocabulary(this.choice)
        },
        callOpicVocabulary() {
            this.choice = {'Opic': true}
            this.callVocabulary(this.choice)
        },
        callSATVocabulary() {
            this.choice = {'korean_SAT': true}
            this.callVocabulary(this.choice)
        },
    }
}
</script>

<style>

</style>