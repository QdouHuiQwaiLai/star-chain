<template>
    <div class="me-info">
        <div class="me-info-title">
            <div class="title">
                <h1>
                    个人中心
                </h1>
            </div>
            <div class="info-box clearFix">
                <div class="portrait f-left">
                    <i class="iconfont icon-user-o"></i>
                </div>
                <div class="text f-right">
                    <p>账号: {{ username }}</p>
                    <p>邮箱: {{ email }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            email: ''
        }
    },
    created () {
        this.getUserInfo()
    },
    methods: {
        // 获取当前用户的信息
        async getUserInfo() {
            const { data: { data } } = await this.$axios.get('user/get/login/')
            this.username = data.username
            this.email = data.email
        }
    }
}
</script>

<style lang="less" scoped>
    .me-info{
        .me-info-title{
            position: relative;
            width: 100%;
            height: 300rem/100;
            background: gradient(linear, left top, right bottom, from(#45bffd), to(#3a6af2));
            background: -webkit-gradient(linear, left top, right bottom, from(#45bffd), to(#3a6af2));
            
            h1{
                margin: 0;
                width: 100%;
                line-height: 88rem/100;
                text-align: center;
                font-size: 34rem/100;
                font-weight: bold;
                color: #fff;  
            }

            .info-box{
                position: absolute;
                top: 90rem/100;
                left: 50%;
                transform: translateX(-50%);
                -webkit-transform: translateX(-50%);
                padding: 70rem/100 50rem/100;
                width: 650rem/100;
                height: 300rem/100;
                border-radius: 5px;
                background: #fff;
                box-shadow: 0 2.5px 4px #ddd;

                .portrait{
                    width: 150rem/100;
                    height: 150rem/100;
                    line-height: 135rem/100;
                    text-align: center;
                    color: #fff;
                    border-radius: 50%;
                    background: #45bffd;

                    i{
                        font-size: 100rem/100;
                    }
                }

                .text{
                    width: 380rem/100;
                    margin-top: 20rem/100;
                    font-size: 28rem/100;
                    word-wrap: break-word;
                    word-break: break-all;
                    overflow: hidden;
                }
            }
        }
    }

    
</style>



