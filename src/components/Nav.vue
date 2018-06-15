<template>
    <footer class="footer-nav">
        <ul>
            <router-link to="/case" tag="li">
                <i class="icon iconfont icon-app-o"></i>
                应用
            </router-link>
            <router-link to="/news" tag="li">
                <i class="icon iconfont icon-news-o"></i>
                资讯
            </router-link>
            <router-link to="/mining" tag="li">
            </router-link>
            <router-link to="/wallet" tag="li">
                <i class="icon iconfont icon-wallet-o"></i>
                资产
            </router-link>
            <router-link to="/me" tag="li">
                <i class="icon iconfont icon-user-o"></i>
                我的
            </router-link>
        </ul>
    </footer>
</template>

<script>
export default {
    
}
</script>

<style lang="less" scoped>
    .footer-nav{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        font-size: 20rem/100;
        color: #999;
        border-top: 1px solid #ddd;
        background: #fff;

        li{
            float: left;
            padding: 10rem/100 0;
            width: 20%;
            height: 97rem/100;
            text-align: center;

            i{
                display: block;
                font-size: 48rem/100;
                color: #dbdbdb;
            }

            &.active{
                color: #3a6af2;
                i{
                    color: #3a6af2;
                }
            }

            &:nth-child(3){
                background: url(../image/stars-native.png) no-repeat center;
                background-size: 64rem/100 64rem/100;

                &.active{
                   background-image: url(../image/stars-active.png) 
                }     
            }
        }
    }
</style>

