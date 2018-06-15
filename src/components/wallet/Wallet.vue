<template>
    <div class="wallet">
        <TitleBar :title-obj="titleObj"></TitleBar>

        <div class="wallet-box-wrap">
            <div class="wallet-box">
                <div class="main clearFix">
                    <div class="money f-left">
                        <i class="iconfont icon-dollar-o"></i>
                    </div>
                    <div class="text f-right">
                        <p>Star Wallet</p>
                        <p>余额: {{ walletInfo.money }}</p>
                        <p>地址: {{ hideAddress }}</p>
                    </div>
                </div>
                <div class="bt clearFix">
                    <router-link to="/wallet/transfer" tag="button" class="f-left mui-btn mui-btn-primary">
                        转账
                    </router-link>
                    <router-link to="/wallet/extract" tag="button" class="f-right mui-btn mui-btn-primary">
                        提现
                    </router-link>
                </div>
            </div>
        </div>

        <div class="show-menu">
            <a href="#popover" id="openPopover"></a>
            <div id="popover" class="mui-popover">
                <ul class="mui-table-view">
                    <li class="mui-table-view-cell">
                        <a href="#" @tap.prevent="goAdress">钱包信息</a>
                    </li>
                    <li class="mui-table-view-cell">
                        <a href="javascript:void(0)">转账信息</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import TitleBar from '../Title-Bar.vue'

export default {
    data () {
        return{
            titleObj: {
                title: '我的资产',
                bold: true,
                back: false,
                ditails: true
            },
            walletInfo: {}
        }
    },
    computed: {
        hideAddress: function () {
            return '************' + (this.walletInfo.address + '').substring(7)
        }
    },
    created: function () {
        this.getWalletInfo()
    },
    methods: {
        goAdress() {
            mui('.mui-popover').popover('hide');
            this.$router.push(`/wallet/address/${this.walletInfo.address}`)
        },
        async getWalletInfo() {
            const { data: { data } } = await this.$axios.get('/wallet/get/login/')
            this.walletInfo = data
        }
    },
    components: {
        TitleBar
    }
    
}
</script>

<style lang="less" scoped>
    .wallet-box-wrap{
        margin-top: 108rem/100;
        width: 100%;
        padding: 0 25rem/100;

        .wallet-box{
            padding: 40rem/100 30rem/100;
            width: 100%;
            border-radius: 10px;
            background: #fff;
            box-shadow: 0 3px 5px #ddd;

            .main{
                width: 100%;

                .money{
                    width: 150rem/100;
                    height: 150rem/100;
                    line-height: 150rem/100;
                    text-align: center;
                    border-radius: 50%;
                    background: #45bffd;

                    i{
                        font-size: 100rem/100;
                        color: #fff;
                    }
                }

                .text{
                    p{  
                        // margin-left: 100rem/100;
                        margin-bottom: 0;
                        height: 50rem/100;
                        font-size: 30rem/100;

                    }
                }
            }

            .bt{
                margin-top: 50rem/100;
                width: 100%;

                button{
                    width: 200rem/100;
                    height: 70rem/100;
                    background-color: #3a6af2;
                }
            }

        }
    }

    .show-menu{
        #openPopover{
            display: block;
            position: fixed;
            top: 0;
            right: 25rem/100;
            width: 88rem/100;
            height: 88rem/100;
            opacity: 0;
            z-index: 99999;
        }

        #popover{
            width: 250rem/100;
        }
    }
</style>


