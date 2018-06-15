<template>
    <div class="case">
        <TitleBar :title-obj="titleObj"></TitleBar>
        <CaseList></CaseList>
        <CaseApply></CaseApply>
    </div>
</template>

<script>
import TitleBar from '../Title-Bar.vue'
import CaseList from './Case-list.vue'
import CaseApply from './Case-apply.vue'

export default {
    data () {
        return{
            titleObj: {
                title: '应用中心',
                bold: true,
                back: false,
                ditails: false
            }
        }
    },
    components: {
        TitleBar,
        CaseList,
        CaseApply
    }
}
</script>

<style lang="less" scoped>

</style>

