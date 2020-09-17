<template>
    <div>
        <h1 style="text-align:center;">단어장</h1>
        <div style="text-align:center;">
            <v-btn @click="callToeicVocabulary" style="margin:1%;">
                토익 단어 가져오기
            </v-btn>
            <v-btn @click="callOpicVocabulary" style="margin:1%;">
                오픽 단어 가져오기
            </v-btn>
            <v-btn @click="callSATVocabulary" style="margin:1%;">
                수능 단어 가져오기
            </v-btn>
        </div>
        <br>
        <div v-if="words">
            <h3 style="text-align:center;">
                {{ $moment(today).format('YY년 MM월 DD일') }}의 단어
            </h3>
            <br>
            <li v-for="(word) in words" :key="word.pid" style="margin-left:20%;">
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