<template>
    <div class="login-wrap">
        <div class="mask"></div>
        <div class="login">
            <TitleBar v-bind:title-obj="titleObj"></TitleBar>
            <form action="#" class="clearFix" @submit.prevent="login">
                <div class="logo">
                    <s></s>
                </div>
                <div class="input-wrap clearFix">
                    <i class="icon iconfont icon-user-o"></i>
                    <input 
                    type="text" 
                    v-model="formData.username"
                    placeholder="请输入用户名"
                    required>
                </div>  
                <div class="input-wrap clearFix">
                    <i class="icon iconfont icon-lock-o"></i>
                    <input 
                    type="password"
                    v-model="formData.password"
                    placeholder="请输入密码"
                    required
                    minlength="6">
                </div>
                <button type="submit">登录</button>  
                <p>
                    <router-link to="/register" tag="u">
                        没有账号？ 立即注册加入星子链
                    </router-link>
                </p>
            </form>
        </div>
    </div>
</template>

<script>
import TitleBar from '../Title-Bar.vue'
import axios from 'axios'
import qs from 'qs'


export default {
    data () {
        return{
            // 页面TitleBar中的属性
            titleObj: {
                // 标题 是否出题 返回按钮 详细按钮
                title: '登录',
                bold: true,
                back: false,
                ditails: false
            },
            formData: {
                username: '',
                password: ''
            }
        }
    },
    created() {
        
    },
    methods: {
        // 登录处理函数
        async login() {
            try{
                const { data: {status} } = await axios.post(
                    'user/login/', qs.stringify(this.formData)
                    )
                if(status == 'success') this.$router.push('/mining')
            } catch(err) {
                mui.alert('用户名或者密码错误')
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

    .login{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 101;
        margin: 300rem/100 0;
        padding: 0 50rem/100;

        form{
            width: 100%;
            padding: 30rem/100 0;
            text-align: center;
            border-radius: 5px;
            background: #fff;
            box-shadow: 0 2px 4px #DDD;

            .logo{
                margin: 0 auto 40rem/100;
                width: 150rem/100;
                height: 150rem/100;
                line-height: 220rem/100;
                border: 1px solid #45bffd;
                border-radius: 50%;

                s{
                    display: inline-block;
                    width: 100rem/100;
                    height: 100rem/100;
                    background: url(../../image/stars-active.png) no-repeat center;
                    background-size: 100rem/100 100rem/100;
                }
            }

            .input-wrap{
                margin: 0 auto 30rem/100;
                width: 80%;
                padding: 0;
                line-height: 70rem/100;
                border-bottom: 1px solid #ccc;

                i{
                    float: left;
                    font-size: 48rem/100;
                }

                input{
                    float: right;
                    margin-bottom: 0;
                    padding: 10rem/100 10rem/100;
                    display: inline-block;
                    width: 90%;
                    height: 70rem/100;
                    font-size: 28rem/100;
                    border: 0;
                    border-radius: 0;
                }
            }

            button{
                margin: 10rem/100 auto 20rem/100;
                padding: 15rem/100 80rem/100;
                width: 80%;
                color: #fff;
                border-radius: 5px;
                background: #3a6af2;
            }

            p{
                margin: 0rem/100 auto;
                width: 80%;
                u{
                    float: left;
                    font-size: 24rem/100;
                    color: #999;
                }
            }

            
        }
    }
</style>


