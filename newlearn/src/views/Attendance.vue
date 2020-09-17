<template>
    <div>
        <v-row>
            <v-col cols="12" md="4" offset-md="2" style="text-align:center;">
                <v-date-picker v-model="picker"
                :event-color="date => date[9] % 2 ? 'red' : 'yellow'"
                :events="functionEvents"></v-date-picker>
            </v-col>
            <v-col cols="12" md="4" v-if="daily.length >= 1" style="text-align:center;">
                <p>{{ daily[0].date }}</p>
                <p>이미지 스피킹 : {{ daily[0].image_speak_count }}</p>
                <p>텍스트 스피킹 : {{ daily[0].text_speak_count }}</p>
                <p>리스닝 : {{ daily[0].listening_count }}</p>
            </v-col>
            <v-col cols="12" md="4" v-else style="text-align:center;">
                <p>활동 내역이 없습니다</p>
            </v-col>
        </v-row>
    </div>
</template>

<script>
import axios from "axios"

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    data () {
        return {
            daily: '',
            month: '',
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
                this.daily = res.data.day
                this.month = res.data.month
            })
        },
        functionEvents (date) {
            const [,, day] = date.split('-')
            if (this.month.includes(parseInt(day, 10))) return ['green']
            return false
        },
    }
}
</script>

<style>

</style>