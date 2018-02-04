# web_joystick

# 环境
*  mac
*  python3.6.2

# usage
*  使用virtualenv创建虚拟环境
*  安装依赖:`pip install -r requirements.txt`
*  `python main.py`
*  运行起来之后，点击chrome浏览器可看到界面

# 说明
以[examples/01-hello-world](https://github.com/ChrisKnott/Eel/blob/master/examples/01%20-%20hello_world/hello.py)为脚手架


# 原理
[Eel](https://github.com/ChrisKnott/Eel)使用websocket来连接js与python，使它们可以双向通信

本质是cs架构

# 策略
目前该应用的数据流向是前端往后端发送信号(开始/结束录制，以及对应的视频时间)，数据在后端打包发送到云平台


# 后端
使用[asynchronous-python](https://github.com/ChrisKnott/Eel#asynchronous-python)实现非阻塞模型

用的是Gevent


# todo
*  使用空格控制录制


# Question
*  需要一个管道负责数据吗 console
