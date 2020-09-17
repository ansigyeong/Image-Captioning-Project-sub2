<template>
    <div style="text-align:center;">
        <h1>활동내역</h1>
        <br>
        <br>
        <h3>Total Points {{ totalPoint }}</h3>
        <v-row>
            <v-col cols="3">구분</v-col>
            <v-col cols="3">점수</v-col>
            <v-col cols="3">내용</v-col>
            <v-col cols="3">날짜</v-col>
        </v-row>
        <hr>
        <div v-for="(list) in pointList" :key="list.pid">
            <v-row>
                <v-col cols="3" v-if="list.use_type">적립</v-col>
                <v-col cols="3" v-else>사용</v-col>
                <v-col cols="3">{{ list.value }}</v-col>
                <v-col cols="3">{{ list.content }}</v-col>
                <v-col cols="3">{{ $moment(list.date).format('YYYY-MM-DD HH:mm') }}</v-col>
            </v-row>
        </div>
    </div>
</template>

<script>
import axios from "axios"

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    data () {
        return {
            totalPoint: 0,
            pointList: [],
        }
    },
    created() {
        this.getPoints()
    },
    methods: {
        getPoints() {
            // 테스트용으로 '2번' 유저에 대해 요청을 보냄.
            // 연동 완료 시 요청보내는 유저로 보낼 것
            axios.get(`${BACK_URL}/accounts/point/2/`)
            .then(res => {
                this.totalPoint = res.data.total_points
                this.pointList = res.data.point_list
            })
        }
    }
}
</script>

<style>

</style>