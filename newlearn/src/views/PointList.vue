<template>
    <div>
        <Header />
        <h1>Total Points {{ totalPoint }}</h1>
        <div v-for="(list) in pointList" :key="list.pid">
            <span>{{ list.id }} </span>
            <span v-if="list.use_type">{{ list.value }} </span>
            <span v-else>-{{ list.value }} </span>
            <span>{{ list.content }}</span>
            <p>{{ list.date }}</p>
        </div>
    </div>
</template>

<script>
import axios from "axios"
import Header from "../components/Header.vue"

const BACK_URL = 'http://127.0.0.1:8000'

export default {
    components: {
        Header,
    },
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