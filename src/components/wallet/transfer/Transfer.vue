<template>
    <div class="wallet-transfer-wrap">
        <div class="mask"></div>
        <div class="wallet-transfer">
            <TitleBar v-bind:title-obj="titleObj"></TitleBar>  

            <form 
            class="mui-input-group box"
            @submit.prevent="transfer"
            >
                <span>转账地址</span>
                <div class="mui-input-row">   
                    <input 
                    type="text" 
                    class="mui-input-clear" 
                    placeholder="请输入转账地址"
                    minlength="15"
                    maxlength="15"
                    v-model="formData.receive"
                    >
                </div>
                <div class="mp-20"></div>
                <span>转账金额</span>
                <div class="mui-input-row">
                    <input 
                    type="number" 
                    step="0.001" 
                    class="mui-input-clear" 
                    placeholder="请输入转账金额"
                    v-model="formData.num"
                    >
                </div>
                <div class="bt-wrap">
                    <button type="submit" class="mui-btn">确认转账</button>
                </div>
            </form>
        </div>
    </div>  
</template>

<script>
import TitleBar from '../../Title-Bar.vue'
import qs from 'qs'

export default {
    data () {
        return {
            titleObj: {
                title: '转账',
                bold: false,
                back: true,
                ditails: false
            },
            formData: {
                // 接收方的钱包地址,转账的金额
                receive: '',
                num: ''
            }
        }
    },
    methods: {
        async transfer() {
            try{
                const { data: { status } } = await this.$axios.patch('wallet/transfer/', qs.stringify(this.formData))
                mui.toast('转账成功')
                this.$router.push('/wallet')
            } catch(err) {
                mui.alert('请检查转账地址或者金额是否正确')
            }
            
        }
    },
    components: {
        TitleBar
    }
}
</script>

<style lang="less">
    .mask{
        position: fixed;
        z-index: 100;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background: #f5f5f5;
    }

    .wallet-transfer{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 101;

        .box{
            margin-top: 108rem/100;
            padding: 20rem/100 25rem/100 40rem/100 25rem/100;
            box-shadow: 0 3px 5px #ddd;

            span{
                margin-left: 25rem/100;
                font-size: 28rem/100;
                color: #666;
            }

            .mp-20{
                margin-top: 20rem/100;
            }

            .mui-input-row{

                input{
                    padding-left: 25rem/100;
                    font-size: 24rem/100;

                    &::-webkit-input-placeholder{
                        color: #ccc
                    }
                }

                &:last-child{
                    margin-top: 20rem/100;
                }
            }

            .bt-wrap{
                margin-top: 50rem/100;
                width: 100%;
                text-align: center;

                button{
                    width: 550rem/100;
                    height: 70rem/100;
                    font-size: 24rem/100;
                    color: #fff;
                    border-radius: 5px;
                    background: #3a6af2;
                }
            }

            &::before,
            &::after{
                width: 0;
            }

        }
    }

</style>


