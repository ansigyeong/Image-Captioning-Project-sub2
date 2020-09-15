<template>
    <div>
        <div style="background:gray; height:50px;">
            <!-- 헤더 표시용 백그라운드 컬러임. 수정 가능 -->
            <div style="float:left; margin-left:10px; margin-top:8px;">
                <div @click.stop="drawer = !drawer" style="cursor:pointer;">
                    <i class="fas fa-bars fa-2x"></i>
                </div>
            </div>
            <div style="float:right; margin-right:10px; margin-top:8px;">
                <v-menu bottom transition="slide-y-transition">
                    <template v-slot:activator="{ on, attrs }">
                        <div v-bind="attrs" v-on="on">
                            <i class="fas fa-user fa-2x"></i>
                        </div>
                    </template>
                    <v-list>
                        <v-list-item @click.stop="dropDrawer = !dropDrawer">
                            <v-list-item-content>
                                <v-list-item-title>My Page</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                        <v-list v-if="dropDrawer">
                            <v-list-item @click="goAttendance" style="margin-left:20px;">
                                <v-list-item-content>
                                    <v-list-item-title>출석부</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item style="margin-left:20px;">
                                <v-list-item-content>
                                    <v-list-item-title>내 정보 수정</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item @click="goPointList" style="margin-left:20px;">
                                <v-list-item-content>
                                    <v-list-item-title>포인트 조회</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                            <v-list-item style="margin-left:20px;">
                                <v-list-item-content>
                                    <v-list-item-title>건의 & 불편 신고</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-list>
                        <v-divider></v-divider>
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title>Logout</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                    </v-list>
                    </v-menu>
            </div>
        </div>

        <!-- 사이드바 항목은 목업 내용 그대로 넣었음 -->
        <!-- 간격, 크기 등 조절해야 함 -->
        <v-navigation-drawer v-model="drawer" absolute temporary>
            <v-list-item style="margin-top:100px;">
                <v-list-item-icon>
                    <i class="fas fa-headphones-alt"></i>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>Listening</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-icon>
                    <i class="fas fa-volume-up"></i>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>Speaking</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-icon>
                    <i class="fas fa-atlas"></i>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>Wordbook</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-divider></v-divider>
            <v-list-item>
                <v-list-item-icon>
                    <i class="fas fa-bullhorn"></i>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>Notice</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-navigation-drawer>
    </div>
</template>

<script>
// import router from '../router';

export default {
    data () {
      return {
        drawer: null,
        dropDrawer: null,
      }
    },
    methods: {
        goPointList() {
            this.$router.push('/mypage/pointList')
        },
        goAttendance() {
            this.$router.push('/mypage/attendance')
        }
    }
}
</script>

<style>

</style>