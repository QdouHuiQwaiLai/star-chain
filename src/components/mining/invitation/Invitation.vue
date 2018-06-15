<template>
    <div class="invitation-wrap">
        <div class="mask"></div>
        <div class="invitation">
            <TitleBar v-bind:title-obj="titleObj"></TitleBar>
            <div class="box-wrap">
                <div class="box">
                    <h3>邀请好友送算力</h3>
                    <div class="erweima"></div>
                    <div class="line">
                        <s></s>
                        <s></s>
                    </div>
                    <button @tap="copyLink" type="button" class="mui-btn">
                        复制链接邀请朋友加入星子链
                    </button>
                    <!-- 隐藏复制文本框 -->
                    <textarea>
                        127.0.0.1:8080/#/register
                    </textarea>
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
                title: '邀请好友',
                bold: false,
                back: true,
                ditails: false
            }
        }
    },
    methods: {
        // 复制邀请好友注册链接
        copyLink() {
            document.querySelector('textarea').select()
            document.execCommand('copy');
            mui.toast('复制成功')
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

    .invitation{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 101;

        .box-wrap{
            margin-top: 88rem/100;
            padding: 20rem/100 25rem/100;
            width: 100%;

            .box{
                padding: 35rem/100 0;
                width: 100%;
                text-align: center;
                border-radius: 10px;
                background: #fff;
                box-shadow: 0px 4px 8px #ddd;

                h3{
                    margin: 0;
                    width: 100%;
                    text-align: center;
                    font-size: 34rem/100;
                    font-weight: normal;
                    color: #3a6af2;
                }

                .erweima{
                    display: inline-block;
                    margin: 20rem/100 0;
                    width: 200rem/100;
                    height: 200rem/100;
                    background: url(../../../image/erweima.png) no-repeat center;
                    background-size: 200rem/100 200rem/100;
                }

                .line{
                    position: relative;
                    width: 100%;
                    border-top: 1px dashed #3a6af2;

                    s{  
                        position: absolute;     
                        display: block;
                        width: 45rem/100;
                        height: 45rem/100;
                        border-radius: 50%;
                        background: #f5f5f5;

                        &:first-child{
                            left: 0;
                            top: 0;
                            transform: translateX(-50%) translateY(-50%);
                        }

                        &:last-child{
                            right: 0;
                            top: 0;
                            transform: translateX(50%) translateY(-50%);
                        }
                    }
                }

                button{
                    margin-top: 30rem/100;
                    padding: 15rem/100 80rem/100;
                    color: #fff;
                    border-radius: 5px;
                    background: #3a6af2;
                }

                textarea{
                    position: absolute;
                    width: 0;
                    height: 0;
                    opacity: 0;
                }

            }
        }
    }
    
</style>


