import VueRouter from 'vue-router'
import Mining from './components/mining/Mining.vue'
import Promote from './components/mining/promote/Promote.vue'
import Invitation from './components/mining/invitation/Invitation.vue'
import Case from './components/case/Case.vue'
import News from './components/news/News.vue'
import Content from './components/news/content/Content.vue'
import Wallet from './components/wallet/Wallet.vue'
import Transfer from './components/wallet/transfer/Transfer.vue'
import Extract from './components/wallet/extract/Extract.vue'
import Address from './components/wallet/address/Address.vue'
import Me from './components/me/Me.vue'
import Login from './components/login/Login.vue'
import Register from './components/login/Register.vue'
import Vue from 'vue'

const router =  new VueRouter({
    routes: [
        {   
            // 默认为登录
            path: '/',
            component: Login
        },
        {   
            // 挖矿首页
            path: '/mining',
            component: Mining
        },
        {
            // 挖矿-提升算力页面
            path: '/mining/promote/:force',
            component: Promote,
            props: true
        },
        {
            // 挖矿-邀请好友页面
            path: '/mining/invitation',
            component: Invitation
        },
        {   
            // 应用页面
            path: '/case',
            component: Case
        },
        {
            // 资讯页面
            path: '/news',
            component: News
        },
        {
            // 资讯-内容详情页
            path: '/news/content',
            component: Content
        },
        {
            // 资产页面
            path: '/wallet',
            component: Wallet
        },
        {
            // 资产-转账页面
            path: '/wallet/transfer',
            component: Transfer
        },
        {
            // 资产-提现页面
            path: '/wallet/extract',
            component: Extract
        },
        {
            // 资产-钱包信息页面
            path: '/wallet/address/:address',
            component: Address,
            props: true
        },
        {
            // 个人中心页面
            path: '/me',
            component: Me
        },
        {
            // 登录页面
            path: '/login',
            component: Login
        },
        {
            // 注册页面
            path: '/register',
            component: Register
        }
    ],
    linkActiveClass: 'active'
})


// 通过登录状态判断此刻的跳转
router.beforeEach(async (to, from, next) => {
    // 如果是注册页面直接方向
    if (to.path == '/register') {
        next()
        return
    }

    let isLogin = false // 登录状态标志
    const v = new Vue()
    try {
        const { data: { data } } = await v.$axios.get('user/get/login/')
        isLogin = true
    } catch (err) {
        isLogin = false
    }

    if( to.path == '/' || to.path == '/login' ) {
        // 如果已经登录 又要去登录首页 就跳转到矿机首页
        if (isLogin) {
            next('/mining')
        } else {
            next()  
        }       
    } else {
        // 如果没有登录 还要去内页 就跳转到登录页面
        if(isLogin) {
            next()
        } else {
            next('/login')
        }  
    }
})


export default router
