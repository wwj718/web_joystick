# web_joystick

# 环境
*  mac
*  python3.6.2


# 说明
以[examples/01-hello-world](https://github.com/ChrisKnott/Eel/blob/master/examples/01%20-%20hello_world/hello.py)为脚手架


# 原理
使用websocket

如果对实时性要求高 可以自行构建websocket

# 策略
前后端只沟通信号，数据在后端打包发送

# todo
*  使用键盘控制
    *  提示开始
*  joystick一直运行，使用信号控制开始和结束，拿到这段时间的录制信息
    *  作为一个独立管道流过去
*  后端返回之前阻塞前段页面 loading

# 后端
使用[asynchronous-python](https://github.com/ChrisKnott/Eel#asynchronous-python)

用的是Gevent


# todo
### Q
*  需要一个管道负责数据吗 console
*  编程风格: js是异步，后端是阻塞还是异步