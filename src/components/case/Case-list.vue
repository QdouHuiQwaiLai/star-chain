<template>
    <div class="case-list">
        <h3>
            <s></s>
            <span>星子链应用</span>
        </h3>
        <ul class="clearFix">
            <li>
                <i class="iconfont icon-dollar-o"></i>
                <br>
                <span>虚拟交易</span>
            </li>
            <li>
                <i class="iconfont icon-compare-o"></i>
                <br>
                <span>电子竞技</span>
            </li>
            <li>
                <i class="iconfont icon-shopping-cart-o"></i>
                <br>
                <span>虚拟购物</span>
            </li>           
            <li>
                <i class="iconfont icon-dollar-o"></i>
                <br>
                <span>虚拟交易</span>
            </li>
            <li>
                <i class="iconfont icon-dollar-o"></i>
                <br>
                <span>虚拟交易</span>
            </li>
            <li>
                <i class="iconfont icon-dollar-o"></i>
                <br>
                <span>虚拟交易</span>
            </li>
            <li>
                <i class="iconfont icon-dollar-o"></i>
                <br>
                <span>虚拟交易</span>
            </li>
            <li>
                <i class="iconfont icon-dollar-o"></i>
                <br>
                <span>虚拟交易</span>
            </li>
            <li>
                <i class="iconfont icon-more-transverse-o"></i>
                <br>
                <span>待开发...</span>
            </li>
            <li>
            </li>
            <li>
            </li>
            <li>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    
}
</script>

<style lang="less" scoped>
    .case-list{
        margin-top: 108rem/100;
        background: #fff;
        box-shadow: 0 2px 5px #ddd;
        -webkit-box-shadow: 0 2px 5px #ddd;

        h3{
            padding: 0 25rem/100;
            width: 100%;
            height: 80rem/100;
            line-height: 80rem/100;
            font-size: 24rem/100;
            color: #3a6af2;

            s{
                display: inline-block;
                vertical-align: middle;
                margin: -8rem/100 15rem/100 0 0;
                width: 20rem/100;
                height: 40rem/100;
                background: #3a6af2;
            }

            span{
                font-weight: normal;
            }
        }

        ul{
            width: 100%;
            
            li{
                float: left;
                padding: 30rem/100 0;
                width: 25%;
                height: 150rem/100;
                text-align: center;
                border-top: 1px solid #ddd;
                border-right: 1px solid #ddd;

                i{  
                    font-size: 64rem/100;
                    color: #dbdbdb;
                }

                span{
                    font-size: 24rem/100;
                    color: #666;
                }

                &:nth-child(4n){
                    border-right: 0;
                }

                &:nth-child(2),
                &:nth-child(3){
                    i{
                        color: #444;
                    }
                }
            }
        }
    }
</style>


