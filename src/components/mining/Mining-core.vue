<template>
    <div class="core-wrap">
        <div class="core">
            <div class="main">
                <div class="machine">
                </div>
                <div class="progress">
                    <div class="wrap">
                        <transition 
                        name="fade"
                        v-on:after-enter="innersManage(1)"
                        >
                            <div class="inner" v-if="oneShow"></div>
                        </transition>
                    </div>
                    <div class="wrap">
                        <transition 
                        name="fade"
                        v-on:after-enter="innersManage(2)"
                        >
                            <div class="inner"  v-if="twoShow"></div>
                        </transition>
                    </div>
                    <div class="wrap">
                        <transition 
                        name="fade"
                        v-on:after-enter="innersManage(3)"
                        >
                            <div class="inner"  v-if="threeShow"></div>
                        </transition>
                    </div>
                </div>
                <div 
                class="ore" 
                @tap="gainStar">
                    <s></s>
                    <span>{{ mayNum }}</span>
                </div>
                <i class="ware icon iconfont icon-money"></i>
                <i 
                class="star"
                :class="{now: isNow}"
                ></i>
            </div>
            <div class="bt clearFix">
                <button  @tap="goPromote" tag="button" type="button" class="mui-btn">              
                    <i class="ware icon iconfont icon-navigation-o"></i>
                    <span>提升算力</span>
                    <span class="mui-badge num">{{ miningInfo.force }}</span>
                </button>
                <router-link to="/mining/invitation" tag="button" type="button" class="mui-btn">
                    <i class="ware icon iconfont icon-group-o"></i>
                    <span>邀请好友</span>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import qs from 'qs'

export default {
    data: () => {
        return {
            miningInfo: {}, // 矿机信息
            mayNum : 0,  // 当前可领取的矿石
            // 三根进度条的显示情况
            oneShow: true,
            twoShow: true,
            threeShow: true,
            isNow: false    // 领取矿石的动画类标志
        }
    },
    // 这里要设置异步
    created: async function() {
        await this.getMiningInfo()  // 获取矿机信息
        await this.getMay() // 获取可领取矿石数量
        this.setInners()    // 根据后台返回的时间初始化进度条
    },
    mounted: function () {
        // star 动画结束事件 改变动画标志状态
        document.querySelector('.star').addEventListener("webkitAnimationEnd", () => {
            this.isNow = false
        })
    },
    methods: {
        // 获取当前登录用户的矿机信息
        async getMiningInfo () {
            const { data: { data } } = await this.$axios.get('mining/get/login/')
            this.miningInfo = data     
        },

        // 获取当前可领取的矿石
        async getMay () {
            const { data: { data: { may_num } } } = await this.$axios.get('mining/get/may/')
            this.mayNum = may_num
        },

        // 跳转提升算力里面
        goPromote () {
            this.$router.push(`/mining/promote/${this.miningInfo.force}`)
        },

        // 设置进度条的显示情况
        setInners () {
            const addTime =  Date.parse(new Date(this.miningInfo.add_time))
            const nowTime = Date.parse(new Date())
            // 现在时间减去矿机添加时间 相差的秒速 除30的取余
            const seconds = ((nowTime - addTime)/1000) % 30
            /*
            * 如果在0到10秒 播放第一根进度条动画
            * 如果10到20秒 第一根进度条100%显示 播放第二根进度条动画
            * 如果20到30秒 第一二跟100%显示 播放第三根进度条动画
            * 
            * 因为vue的过渡原因 必须使用setTimeout设置要开始的动画
            */
            if (seconds >= 0 && seconds < 10) {
                this.oneShow = this.twoShow = this.threeShow = false;
                setTimeout(() => {
                    this.oneShow = true
                }) 
            } else if ( seconds >= 10 && seconds < 20 ) {
                this.twoShow = this.threeShow = false;
                setTimeout(() => {
                    this.twoShow = true
                }) 
            } else if ( seconds >= 20 && seconds < 30 ) {
               this.threeShow = false;
               setTimeout(() => {
                    this.threeShow = true
                }) 
            }   
        },

        // 进度条管理
        async innersManage(index) {
            // 当前进度条播放结束后开启下一根进度条的动画
            switch (index){
                case 1:
                    this.twoShow = true
                    break;
                case 2:
                    this.threeShow = true
                    break
                case 3:
                    // 当第三根进度条结束时 把三根进度条进度情况
                    // 在更新当前可获取的矿石数量
                    // 最后开启第一根进度条的动画
                    this.oneShow = this.twoShow = this.threeShow = false
                    await this.getMay()
                    this.oneShow = true
                    break
            }
        },
        
        // 获取矿石
        async gainStar() {
           if(this.isNow) return // 如果动画还没有执行完毕 退出
           try {
               const { data: { status } } = await this.$axios.patch('mining/gain/', qs.stringify({
                   num: 1
               }))
               this.isNow = true    // 开启动画
               this.mayNum -= 1
           } catch (err) {
               mui.alert('领取失败')
           } 
        }

    }
}
</script>

<style lang="less" scoped>
.core-wrap{
    padding: 108rem/100 25rem/100 30rem/100 25rem/100;
    .core{
        width: 100%;
        overflow: hidden;
        border-radius: 15rem/100;
        box-shadow: 0 4px 8px #ddd;

        .main{
            position: relative;
            width: 100%;
            height: 450rem/100;
            background: gradient(linear,left top,right bottom,from(#45bffd), to(#3a6af2));
            background: -webkit-gradient(linear,left top,right bottom,from(#45bffd), to(#3a6af2));

            .machine{
                position: absolute;
                top: 53%;
                margin-top: -90rem/100;
                left: 20rem/100;
                width: 178rem/100;
                height: 178rem/100;
                background: url(../../image/machine.png) no-repeat center;
                background-size: 178rem/100 178rem/100;
                animation: machine-rotate 2.5s linear infinite;
                -webkit-animation: machine-rotate 2.5s linear infinite;
            }

            .progress{
                position: absolute;
                top: 53%;
                transform: translateY(-50%);
                left: 220rem/100;
                .wrap{
                    margin-bottom: 40rem/100;
                    width: 450rem/100;
                    height: 15rem/100;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    overflow: hidden;

                    .inner{
                        height: 100%;
                        background: #fff;
                    }

                    /* 过度进入时候的状态  */
                    .fade-enter{
                        width: 0%;
                    }
                    /* 定义进入过度生效时的状态 定义过度的时间曲线等 */ 
                   .fade-enter-active {
                        transition: all linear 10s;
                    }
                    /* 定以过度结束的状态 */ 
                   .fade-enter-to{
                       width: 100%;
                   }
                   .fade-leave-active {
                      transition: all linear 0s;
                   }
                   .fade-leave-to{
                    //   width: 100%;
                   }
                    
                    &:nth-child(3){
                        margin-bottom: 0;
                    }        
                }
            }

            .ore{
                position: absolute;
                top: 25rem/100;
                right: 25rem/100;
                padding: 10rem/100;
                width: 120rem/100;
                height: 120rem/100;
                text-align: center;
                background: #51adf9;
                border-radius: 50%;
                animation: ore-updown .8s linear infinite alternate;


                s{  
                    display: inline-block;
                    position: absolute;
                    top: 10rem/100;
                    left: 50%;
                    transform: translateX(-50%);
                    -webkit-transform: translateX(-50%);
                    width: 48rem/100;
                    height: 48rem/100;
                    background: url(../../image/stars-white.png) no-repeat center;
                    background-size: 45rem/100 45rem/100;
                }

                span{
                    display: inline-block;
                    position: absolute;
                    bottom: 20rem/100;
                    left: 50%;
                    transform: translateX(-50%);
                    -webkit-transform: translateX(-50%);
                    color: #fff;
                    font-size: 12rem/100;
                }
            }

            .ware{
                position: absolute;
                bottom: 30rem/100;
                left: 50%;
                transform: translateX(-50%);
                -webkit-transform: translateX(-50%);
                color: #fff;
                font-size: 85rem/100;
            }

            .star{  
                display: inline-block;
                position: absolute;
                z-index: -1;
                opacity: 0;
                top: 60rem/100;
                right: 60rem/100;
                width: 48rem/100;
                height: 48rem/100;
                background: url(../../image/stars-white.png) no-repeat center;
                background-size: 45rem/100 45rem/100;
            }

            .star.now{
                animation: gain-star 1s linear;
                -webkit-animation: gain-star 1s linear;
            }

        }

        .bt{
            padding: 17rem/100 20rem/100;
            width: 100%;
            font-size: 28rem/100;
            background: #fff;
            
            button{
                float: right;
                width: 300rem/100;

                &:first-child{
                float: left;

                .num{
                    color: #fff;
                    background: #3a6af2;
                }
                }  
            }

        }
    }
}

@keyframes machine-rotate {
    from{
        transform: rotate(0deg);
    }
    to{
        transform: rotate(360deg);
    }
} 

@keyframes ore-updown{
    from{
        transform: translateY(8rem/100);
    }
    to{
        transform: translateY(-4rem/100);
    }
}

@keyframes gain-star {
    0%{
        z-index: 100;
        opacity: 1;
    }
    100%{
        z-index: 100;
        opacity: 1;
        transform: translateX(-260rem/100) translateY(300rem/100);
    }
}
</style>
