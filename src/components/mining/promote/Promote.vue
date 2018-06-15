<template>
    <div class="promote-wrap">
        <div class="mask"></div>
        <div class="promote">
            <div class="my-force-wrap">
                <div class="title">
                    <h2>
                        <a @tap.prevent="back" class="left"><i class="icon iconfont icon-back-o"></i></a>
                        提升算力
                    </h2>
                </div>
                <div class="my-force">
                    <span>{{ myForce }}</span>
                </div>
            </div>

            <ul class="task-list">
                <li>
                    <i class="iconfont icon-signed-o"></i>
                    <span class="text">每日签到</span>
                    <span class="mui-badge num">+1算力</span>
                    <div class="bt-wrap">
                        <button
                        v-if="signed"
                        type="button" 
                        class="mui-btn done"
                        >
                        已签订
                        </button>
                        <button 
                        v-else
                        type="button" 
                        class="mui-btn"
                        @click="sign"
                        >
                        签到
                        </button>
                    </div>      
                </li>
                <li>
                    <i class="iconfont icon-key-o"></i>
                    <span class="text">实名认证</span>
                    <span class="mui-badge num">+150算力</span>
                    <div class="bt-wrap">
                        <button type="button" class="mui-btn done">已完成</button>
                    </div>      
                </li>
            </ul>
        </div>
        </div>
</template>

<script>
import qs from 'qs'
import Vue from 'vue'

export default {
    // 在进入路由器加载签到情况 解决闪烁
    async beforeRouteEnter (to, from, next) {
        const v = new Vue() // 应为axios被封装 所以要new 一个vue来发请求
        const { data: { data } } = await v.$axios.get('mining/sign/')
        next(vm => {
            vm.signed = data.signed
        })
    },
    props: ['force'],
    data() {
        return {
            myForce: this.force - 0,
            // 是否已经签到
            signed: false
        }
    },
    created() {
        // this.getSignStatus()
    },
    methods: {
        // 返回上一页
        back() {
            this.$router.back()
        },
        // 获取能否签到状态
        async getSignStatus() {
            const { data: { data } } = await this.$axios.get('mining/sign/')
            this.signed = data.signed
        },
        // 签到
        async sign() {
            try{
                const { data: { stutas } } =  await this.$axios.patch('mining/sign/')
                if(!stutas == 'success') return
                this.signed = true
                const req = await this.$axios.patch('mining/promote/', qs.stringify({
                    num: 1
                }))
                this.myForce += 1
                mui.toast('签到成功')
            } catch(err){
                mui.alert('签到出错')
            }
        }
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

    .promote{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 101;

        .my-force-wrap{
            position: relative;
            width: 100%;
            height: 300rem/100;
            background: gradient(linear, left top, right bottom, from(#45bffd), to(#3a6af2));
            background: -webkit-gradient(linear, left top, right bottom, from(#45bffd), to(#3a6af2));
            
            h2{
                position: relative;
                margin: 0;
                width: 100%;
                line-height: 88rem/100;
                text-align: center;
                font-size: 34rem/100;
                font-weight: normal;
                color: #fff;  
                
                a{  
                    display: block;
                    position: absolute;
                    top: 50%;
                    transform: translateY(-50%);
                    -webkit-transform: translateY(-50%);
                    left: 0;
                    width: 88rem/100;
                    height: 88rem/100;
                    line-height: 88rem/100;
                    text-align: center;

                    i{
                        color: #fff;
                        font-size: 48rem/100px;
                    }
                }
            }

            .my-force{
                position: absolute;
                top: 105rem/100;
                left: 50%;
                transform: translateX(-50%);
                -webkit-transform: translateX(-50%);
                width: 150rem/100;
                height: 150rem/100;
                line-height: 150rem/100;
                text-align: center;
                border: 3px solid #78c1fc;
                border-radius: 50%;

                span{
                    font-size: 48rem/100;
                    font-weight: normal;
                    color: #fff;
                }   
            }

            
        }

        .task-list{
            padding: 20rem/100 25rem/100;
            
            li{
                margin-bottom: 20rem/100;
                padding: 0 25rem/100;
                width: 100%;
                height: 100rem/100;
                line-height: 100rem/100;
                background: #fff;
                border-radius: 10px;
                box-shadow: 0px 3px 3px #ddd;
                -webkit-box-shadow: 0px 3px 3px #ddd;

                i{  
                    display: inline-block;
                    margin-top: -10rem/100;
                    vertical-align: middle;
                    font-size: 48rem/100;
                    color: #3a6af2;
                }

                .text{
                    font-size: 28rem/100;
                    color: #666;
                }

                .num{
                    color: #fff;
                    background: #3a6af2;
                }

                .bt-wrap{
                    float: right;
                    height: 100rem/100;

                    button{
                        margin-top: -10rem/100;
                        vertical-align: middle;
                        border-radius: 5px;
                        background: #3a6af2;
                        color: #fff;

                        &.done{
                            background: #ccc;
                            color: #666;
                        }
                    }
                }
            }
        }
    }

    
</style>


