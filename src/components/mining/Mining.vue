<template>
    <div class="mining">
        <TitleBar v-bind:title-obj="titleObj"></TitleBar>
        <MiningCore></MiningCore>
        <MiningRank></MiningRank>
    </div>
</template>

<script>
import TitleBar from '../Title-Bar.vue'
import MiningCore from './Mining-Core.vue'
import MiningRank from './Mining-rank.vue'

export default {
    data () {
        return{
            // 页面TitleBar中的属性
            titleObj: {
                // 标题 是否出题 返回按钮 详细按钮
                title: '挖矿中心',
                bold: true,
                back: false,
                ditails: false
            }
        }
    },
    components: {
        TitleBar,
        MiningCore,
        MiningRank
    }
}
</script>


<style>

</style>
