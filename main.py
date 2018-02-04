import eel # https://github.com/ChrisKnott/Eel
import pygame
# g = 0
recording = False # 开关变量

pygame.init()
eel.init('video_lab')                     # Give folder containing web files

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

'''
# for test

@eel.expose                         # Expose this function to Javascript
def get_key(x):
  global g
  g += 1
  r = {"hello":"from backend:g={}".format(g)}
  print(r)
  return r
'''

@eel.expose
def start_record(start_time):
  print('start_record| start_time: {}'.format(start_time)) # 拿到前端通过websocket传过来的数据
  global recording
  recording = True
  return recording

@eel.expose
def stop_record(stop_time):
  print('stop_record| stop_time: {}'.format(stop_time))
  global recording
  recording = False
  return recording


eel.start('index.html', block=False, size=(600, 400))    # Start ，非阻塞

# 这个循环一直获取硬件输入
while True:
  eel.sleep(0.01) #需要休眠 否则http服务器会无法启动
  if recording: # 这是一个全局变量，方便前端来控制是否开始录制
    # 开始进入pygame的事件循环，监听硬件输入
    for event in pygame.event.get(): # User did something
        '''
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        '''
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    joystick = pygame.joystick.Joystick(0) #只有一个摇杆，0表示第一个摇杆，这块参考文档
    joystick.init()
    # name = joystick.get_name()
    # print("Joystick name: {}".format(name) )
    axes = joystick.get_numaxes()
    for i in range( axes ):
    # pygame.joystick.Joystick.get_axis
    # 选择你关心的选为元组
      axis = joystick.get_axis( i ) # 目前的摇杆时0，1两个轴
      # 只有值大于某个值才展示，设置阈值
      if (abs(axis)) > 0.01 and (abs(axis) < 1) :
        print("Axis {} value: {:>6.3f}".format(i, axis) ) #当心四舍五入
    eel.sleep(0.01) # 需要短暂休眠，否则会独占进程


# todo:与本项目无关
'''
小庄公告板：
    可以使用两个程序共同读写一个本地文件来做，依赖同一个资源，而不必使用多进程
    那就需要redis 另一个client去写 去订阅redis
    树莓派redis已经启动 同时保留log
'''