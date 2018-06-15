1. ps渐变与css中的渐变角度问题
    未找到规律 
    使用左上角到右下角方向渐变解决



mint-ui 使用ajax加载动画


.mint-spinner-snake {
  -webkit-animation: mint-spinner-rotate 0.8s infinite linear;
          animation: mint-spinner-rotate 0.8s infinite linear;
  border: 4px solid transparent;
  border-radius: 50%;
}
@-webkit-keyframes mint-spinner-rotate {
0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
}
100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
}
}
@keyframes mint-spinner-rotate {
0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
}
100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
}
}


2. axios提交数据之前要qs.stringify

3. 跨域问题
django : pip install django-cors-headers 
    # 解决跨域
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = (
        'localhost:8080',
    )

    CORS_ALLOW_CREDENTIALS = True #### 重要 允许带cookies跨域

axios: axios.defaults.withCredentials = true