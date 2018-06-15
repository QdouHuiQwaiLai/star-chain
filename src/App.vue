<template>
    <div id="app">
        <router-view></router-view>
        <Nav></Nav>
    </div>
</template>

<script>
import Nav from './components/Nav.vue'
// import Mining from './components/mining/Mining.vue'
// import Promote from './components/mining/promote/Promote.vue'
// import Invitation from './components/mining/invitation/Invitation.vue'
// import Case from './components/case/Case.vue'
// import News from './components/news/News.vue'
// import Content from './components/news/content/Content.vue'
// import Wallet from './components/wallet/Wallet.vue'
// import Transfer from './components/wallet/transfer/Transfer.vue'
// import Extract from './components/wallet/extract/Extract.vue'
// import Address from './components/wallet/address/Address.vue'
// import Me from './components/me/Me.vue'

export default {
    components: {
        Nav,
        // Mining,
        // Promote,
        // Invitation,
        // Case,
        // News,
        // Content,
        // Wallet,
        // Transfer,
        // Extract,
        // Address,
        // Me
    }
}
</script>

<style lang="less">

</style>


