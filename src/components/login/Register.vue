<template>
    <div class="rigister">
        <a @tap.prevent="back"><i class="icon iconfont icon-back-o"></i></a>
        <form class="rigister-box" action="#" @submit.prevent="rigister">
            <label for="username">登录用户名</label>
            <input 
            id="username" 
            type="text"
            v-model="formData.username"
            required
            minlength="6"
            maxlength="20"
            >
            <label for="email">邮箱</label>
            <input 
            id="email" 
            type="email"
            v-model="formData.email"
            required
            >
            <label for="name">昵称</label>
            <input 
            id="name" 
            type="text"
            v-model="formData.name"
            required
            maxlength="20"
            >
            <label for="password">密码</label>
            <input 
            id="password" 
            type="password"
            v-model="formData.password"
            required
            minlength="6"
            >
            <button type="submit">注 册</button>
        </form>
        <s class="s1"></s>
        <s class="s2"></s>
    </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'

export default {
    data() {
        return {
            formData: {
                username: '',
                email: '',
                name: '',
                password: ''
            }
        }
    },
    methods: {
        async rigister() {
            try{
                const {data: {status}} = await axios.post(
                    'http://127.0.0.1:8000/user/register/', qs.stringify(this.formData)
                )
                console.log(status)
                // 如果登录成功，登录用户并且跳转到矿机页面
                const req = await axios.post(
                    'http://127.0.0.1:8000/user/login/', qs.stringify({
                        username: this.formData.username,
                        password: this.formData.password
                    })
                )
                if(req.data.status == 'success') this.$router.push('/mining')
            } catch(err) {
                console.log(err)
            }
        },
        back() {
            this.$router.push('/login')
        },
    }
}
</script>

<style lang="less" scoped>
    .rigister{
        position: fixed;
        top: 0;
        bottom: 0;
        right: 0;
        left: 0;
        padding: 0 70rem/100;
        background: gradient(linear, left top, right bottom, from(#45bffd), to(#3a6af2));
        background: -webkit-gradient(linear, left top, right bottom, from(#45bffd), to(#3a6af2));
        z-index: 1;

        a{  
            display: block;
            position: absolute;
            top: 50rem/100;
            left: 25rem/100;
            width: 88rem/100;
            height: 88rem/100;
            line-height: 88rem/100;
            text-align: center;
            z-index: 100;
            
            &.right{
                right: 0;
            }

            i{
                color: #fff;
                font-size: 48rem/100px;
            }
        }

        .rigister-box{
            margin-top: 300rem/100;

            label{
                font-size: 28rem/100;
                color: #fff;
            }

            input{
                padding: 0;
                font-size: 28rem/100;
                color: #fff;
                background: transparent;
                border: 0;
                border-radius: 0;
                border-bottom: 1px solid #fff;
            }

             button{
                margin-top: 30rem/100;
                width: 100%;
                height: 70rem/100;
                color: #fff;
                background: transparent;
                border: 1px solid #fff;
                border-radius: 5px;
            }
        }

       
        .s1{
            position: absolute;
            top: 30rem/100;
            left: 30rem/100;
            display: block;
            width: 191rem/100;
            height: 191rem/100;
            background: url(../../image/login-s1.png) no-repeat center;
            background-size: 191rem/100 191rem/100;
        }

        .s2{
            position: absolute;
            bottom: 300rem/100;
            right: 10rem/100;
            display: block;
            width: 245rem/100;
            height: 245rem/100;
            background: url(../../image/login-s2.png) no-repeat center;
            background-size: 245rem/100 245rem/100; 
        }
    }
</style>
