<template>
    <div class="title-bar"> 
        <a v-if="titleObj.back" @tap.prevent="back" class="left"><i class="icon iconfont icon-back-o"></i></a>
        <h1 v-bind:class="{ bold: titleObj.bold }">{{ titleObj.title }}</h1>
        <a v-if="titleObj.ditails" class="right"><i class="icon iconfont icon-more-transverse-o"></i></a>
    </div>
</template>

<script>
export default {
    // 根据父组件传入的对象 渲染相应的title
    props: ['titleObj'],
    methods: {
        // 返回上一页
        back() {
            this.$router.back()
        }
    }
}

</script>

<style lang="less" scoped>
    .title-bar{
        position: fixed;
        z-index: 1000;
        top: 0;
        left: 0;
        width: 100%;
        height: 88rem/100;
        background: gradient(linear,left top,right bottom,from(#45bffd), to(#3a6af2));
        background: -webkit-gradient(linear,left top,right bottom,from(#45bffd), to(#3a6af2));
        
        h1{
            margin: 0;
            width: 100%;
            line-height: 88rem/100;
            text-align: center;
            font-size: 34rem/100;
            font-weight: normal;
            color: #fff;
            
            &.bold{
                font-weight: bold;
            }
        }

        a{  
            display: block;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            -webkit-transform: translateY(-50%);
            width: 88rem/100;
            height: 88rem/100;
            line-height: 88rem/100;
            text-align: center;
            
            &.right{
                right: 0;
            }

            i{
                color: #fff;
                font-size: 48rem/100px;
            }
        }
    }
</style>
