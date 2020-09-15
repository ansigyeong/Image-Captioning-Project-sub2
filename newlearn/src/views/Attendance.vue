<template>
    <div>
        <v-row justify="center">
            <v-date-picker v-model="picker"></v-date-picker>
        </v-row>
        <div v-if="dailyList.length >= 1">
            <p>{{ dailyList[0].date }}</p>
            <p>이미지 스피킹 : {{ dailyList[0].image_speak_count }}</p>
            <p>텍스트 스피킹 : {{ dailyList[0].text_speak_count }}</p>
            <p>리스닝 : {{ dailyList[0].listening_count }}</p>
        </div>
        <div v-else>
            <p>활동 내역이 없습니다</p>
        </div>
    </div>
</template>

<script>
import axios from "axios"

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    data () {
        return {
            dailyList: '',
            picker: new Date().toISOString().substr(0, 10),
        }
    },
    created() {
        this.getLists()
    },
    mounted() {
    },
    watch: {
        picker: function () {
            this.getLists()
        }
    },
    methods: {
        getLists() {
            // 테스트용으로 '2번' 유저에 대해 요청을 보냄.
            // 연동 완료 시 요청보내는 유저로 보낼 것
            axios.post(`${BACK_URL}/accounts/daily/2/`, this.picker)
            .then(res => {
                this.dailyList = res.data
                console.log(this.dailyList)
            })
        },
    }
}
</script>

<style>

</style>