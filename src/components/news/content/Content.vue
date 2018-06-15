<template>
    <div class="news-content-wrap">
        <div class="mask"></div>
        <div class="news-content">
            <TitleBar :title-obj="titleObj"></TitleBar>
            <div class="new">
                <h2>星子链，上交易所第一天暴涨100倍</h2>
                <div class="line"></div>
                <div class="content">
                    <p>
                        人的一生，关键的选择点可能只有几个。
                        这有限的几个节点组成了我们的一生。
                    </p>

                    <p>
                        20 13年，巴比特启动“光之锥”开放原创计划，
                        数以百计的专栏作者汇聚于此，大咖共襄、百家争鸣。
                        自此，国内最富有生命力的区块链思想平台逐渐成长、沉淀。
                    </p>

                    <p>
                        光锥之内，就是命运。光锥之外，未来穿越而来。
                        遇见比特币，遇见区块链，可能是巴比特专栏作者们人生中最大的转折点。
                        5年过去，他们有的淡出圈子，有的成长为一方诸侯。
                        更多的，仍在这个新兴领域里，探索前行。
                        喧嚣亦或沉静，争鸣亦或共识，是为行业生态。
                    </p>

                    <p>
                        一个月前，我们开始了这次“拾光之旅”，访问了过去5年间最具有代表性的专栏作者。并记录下他们的区块链时刻，追溯5年间被改变的人生。
                    </p> 

                    <p>
                        以此，向行业拓荒者致敬。
                    </p>

                    <p>
                        今天，让我们一起走进光之锥2.0人物访问系列一：2013年度作者龚鸣。
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import TitleBar from '../../Title-Bar.vue'

export default {
    data () {
        return {
            // 页面TitleBar中的属性
            titleObj: {
                // 标题 是否出题 返回按钮 详细按钮
                title: '新闻详情',
                bold: false,
                back: true,
                ditails: false
            }
        }
    },
    components: {
        TitleBar
    }
}
</script>

<style lang="less" scoped>
    .mask{
        position: fixed;
        z-index: 100;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background: #f5f5f5;
    }

    .news-content{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 101;

        .new{
            margin-top: 88rem/100;
            width: 100%;

            h2{
                width: 100%;
                height: 80rem/100;
                line-height: 80rem/100;
                text-align: center;
                font-size: 30rem/100;
                color: #333;
            }

            .line{
                width: 100%;
                height: 0;
                border-top: 1px dashed #ccc;
            }

            .content{
                padding: 25rem/100;
                width: 100%;
                
            }
        }
    }

    
</style>

