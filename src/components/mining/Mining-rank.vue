<template>
    <div class="rank-wrap">
        <h3>算力排行榜</h3>
        <div class="list-title clearFix">
            <span>名称</span>
            <span>账号</span>
            <span>算力值</span>
        </div>
        <ul class="mui-table-view">
            <li 
            v-for="(rank, index) in rankList"
            class="mui-table-view-cell"
            :key="rank.id"
            >
                <span>{{ index + 1 }}</span>
                <span>{{ rank.name }}</span>
                <span>{{ rank.force }}</span>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    data: () => {
        return {
            rankList: []
        }
    },
    created: function () {
        this.getRankList()
    },
    methods: {
        async getRankList () {
            const { data: { data } } = await this.$axios.get('/mining/rank/')
            this.rankList = data
        }
    }
   
    
}
</script>

<style lang="less" scoped>
.rank-wrap{
    margin-bottom: 98rem/100;
    width: 100%;
    color: #666;
    background: #fff;

    h3{
        margin: 0;
        width: 100%;
        height: 70rem/100;
        line-height: 70rem/100;
        font-size: 30rem/100;
        font-weight: normal;
        text-align: center;
        color: #3a6af2;
    }

    .list-title{
        padding: 0 54rem/100;
        width: 100%;
        height: 70rem/100;
        line-height: 70rem/100;
        text-align: center;
        font-size: 24rem/100;
        border-top: 1px solid #ccc;
        border-bottom: 1px solid #ccc;
        background: #f8f8f8;
        overflow: hidden;
        
        span{
            &:first-child{
                float: left;
            }
            &:last-child{
                float: right;
            }
        }
    }

    ul{
        padding: 0 54rem/100;
        width: 100%;
        &::after{
            height: 0;
        }

        li{
            padding-left: 15rem/100;
            padding-right: 15rem/100;
            width: 100%;
            text-align: center;
            font-size: 24rem/100;
            
            &::after{
                left: 0;
            }

            span{
                &:first-child{
                    float: left;
                }
                &:last-child{
                    float: right;
                }
            }
        }
    }
}
</style>


