# 后台接口文档
 
### 用户信息
+ 接口名称： 用户注册
+ 接口地址： user/register/
+ 请求方式： post
+ 参数说明  
    参数名称|是否必须|说明
    username|是|登录用户名
    email|是|邮箱
    name|是|用户名称
    password|是|密码
+ 返回说明
    {
        "status": "success"
    }
    ...


+ 接口名称： 登录
+ 接口地址： user/login/
+ 请求方式： post
+ 参数说明  
    参数名称|是否必须|说明
    username|是|登录用户名
    password|是|密码
+ 返回说明
    {
        "status": "success"
    }
    ...


+ 接口名称： 退出登录
+ 接口地址： user/logout/
+ 请求方式： get
+ 参数说明  
    参数名称|是否必须|说明
+ 返回说明
    {
        "status": "success"
    }


+ 接口名称： 获取当前用户信息
+ 接口地址： user/get/login/
+ 请求方式： get
+ 参数说明  
    参数名称|是否必须|说明
+ 返回说明
    {
        "status": "success",
        "data": {
            "username": "123456789",
            "email": "123@qq.com"
        }
    }



### 钱包信息
+ 接口名称： 钱包转账
+ 接口地址： wallet/transfer/
+ 请求方式： patch
+ 参数说明  
    参数名称|是否必须|说明
    num|是|转账的金额
    address|是|接收方的地址
+ 返回说明
     {
        "status": "success"
     }

    
+ 接口名称： 钱包提现 （没有实现）
+ 接口地址： wallet/extract/
+ 请求方式： patch
+ 参数说明  
    参数名称|是否必须|说明
    num|是|转账的金额
    address|否|交易所的地址
+ 返回说明
     {
        "status": "success"
     }


+ 接口名称： 获取当前用户的钱包信息
+ 接口地址： wallet/get/login/
+ 请求方式： get
+ 参数说明  
    参数名称|是否必须|说明
+ 返回说明
     {
        "status": "success",
        "data": {
            "id": 4,
            "user_id": 7,
            "address": "g7vKBka8MzdWqRx",
            "money": 0
        }
    }



### 矿机信息
+ 接口名称： 获取用户算力排行榜top10
+ 接口地址： mining/rank/
+ 请求方式： get
+ 参数说明  
    参数名称|是否必须|说明
+ 返回说明
     {
        "status": "success",
        "data": [
            {
                "id": 13,
                "user_id": 18,
                "wallet_id": 15,
                "force": 55655,
                "add_time": "2018-06-10 21:56:49",
                "extract": 165,
                "name": "记不得哦"
            },
            ....]
     }

    
+ 接口名称： 提升矿机算力
+ 接口地址： wallet/promote/
+ 请求方式： patch
+ 参数说明  
    参数名称|是否必须|说明
    num|是|提升的算力值
+ 返回说明
    {
        "status": "success"
     }


+ 接口名称： 领取矿石到钱包
+ 接口地址： mining/gain/
+ 请求方式： patch
+ 参数说明  
    参数名称|是否必须|说明
    num|是|领取的矿石
+ 返回说明
    {
        "status": "success"
     }


+ 接口名称： 获取当前用户的矿机信息
+ 接口地址： mining/get/login/
+ 请求方式： get
+ 参数说明  
    参数名称|是否必须|说明
+ 返回说明
    {
        "status": "success",
        "data": {
            "id": 2,
            "user_id": 7,
            "wallet_id": 4,
            "force": 100,
            "add_time": "2018-06-10 21:24:26",
            "extract": 0
        }
    }


+ 接口名称： 获取当前可领取的矿石
+ 接口地址： get/may/
+ 请求方式： get
+ 参数说明  
    参数名称|是否必须|说明
+ 返回说明
    {
        "status": "success",
        "data": {
            "may_num": 1852
        }
    }


+ 接口名称： 矿机能否签到查询
+ 接口地址： sign/
+ 请求方式： get
+ 参数说明  
    参数名称|是否必须|说明
+ 返回说明
    {
        "status": "success",
        "data": {
            "signed": false
        }
    }


+ 接口名称： 矿机签到
+ 接口地址： sign/
+ 请求方式： patch
+ 参数说明  
    参数名称|是否必须|说明
+ 返回说明
    {
        "status": "success",
    }
