<template>
    <div>
        <Header />
        <v-row justify="center">
            <v-date-picker v-model="picker"
            :event-color="date => date[9] % 2 ? 'red' : 'yellow'"
            :events="functionEvents"></v-date-picker>
        </v-row>
        <div v-if="daily.length >= 1">
            <p>{{ daily[0].date }}</p>
            <p>이미지 스피킹 : {{ daily[0].image_speak_count }}</p>
            <p>텍스트 스피킹 : {{ daily[0].text_speak_count }}</p>
            <p>리스닝 : {{ daily[0].listening_count }}</p>
        </div>
        <div v-else>
            <p>활동 내역이 없습니다</p>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import Header from '../components/Header.vue'

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    name: 'Attendance',
    components: {
        Header,
    },
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