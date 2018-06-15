<template>
    <div class="me-list-wrap">
        <ul class="me-list">
            <li>
                设置
                <i class="iconfont icon-arrow-right f-right"></i>
            </li>
            <li>
                关于
                <i class="iconfont icon-arrow-right f-right"></i>   
            </li>
        </ul>
        <div class="bt-wrap">
            <button 
            type="button" 
            class="mui-btn mui-btn-danger"
            @tap="logout"
            >
                退出登录
            </button>
        </div>
        
    </div>
</template>

<script>
export default {
    methods: {
        // 退出登录
        async logout() {
            mui.confirm('是否确认退出', async (e) => {
                if (e.index == 1) {
                    const { data: { status } } = await this.$axios.get('user/logout/')
                    this.$router.push('/login')
                }
            })
        }
    }
    
}
</script>

<style lang="less" scoped>
    .me-list-wrap{
        width: 100%;

        .me-list{
            margin-top: 130rem/100;
            width: 100%;

            li{
                margin-bottom: 10rem/100;
                padding: 0 30rem/100;
                width:100%;
                height: 100rem/100;
                font-size: 28rem/100;
                color: #666;
                line-height: 100rem/100;
                background: #fff; 
            }

            i{
                font-size: 48rem/100;
            }
        }

        .bt-wrap{
            margin-top: 30rem/100;
            width: 100%;
            text-align: center;
            
            button{
                width: 80%;
            }
        }
        

    }
    
</style>



