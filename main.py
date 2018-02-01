import eel
import pygame
g = 0
recording = False

pygame.init()
eel.init('video_lab')                     # Give folder containing web files

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)


@eel.expose                         # Expose this function to Javascript
def get_key(x):
  global g
  # 再写一个进程？
  g += 1
  r = {"hello":"from backend:g={}".format(g)}
  print(r)
  return r

@eel.expose
def start_record(start_time):
  print('start_record| start_time: {}'.format(start_time))
  global recording
  recording = True
  return recording

@eel.expose
def stop_record(stop_time):
  print('stop_record| stop_time: {}'.format(stop_time))
  global recording
  recording = False
  return recording

# say_hello_py('Python World!')
# eel.py_console('Python World!')   # Call a Javascript function

eel.start('index.html', block=False, size=(600, 400))    # Start

# 这个循环一直获取硬件输入，控制recording/stop ，使用一个容器收集


while True:
  # print("hello")
  eel.sleep(0.01) #需要休眠 否则http服务器会无法启动
  # print("test")
  if recording:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    #print("I'm a main loop")
    # eel.sleep(1.0)  #非阻塞
    joystick = pygame.joystick.Joystick(0)#只有一个
    joystick.init()
    name = joystick.get_name()
    # print("Joystick name: {}".format(name) )
    axes = joystick.get_numaxes()
    for i in range( axes ):
    # pygame.joystick.Joystick.get_axis
    # 选择你关心的选为元组
      axis = joystick.get_axis( i )
      # 只有值大于某个值才展示
      # print("axis:",axis)
      if (abs(axis)) > 0.01 and (abs(axis) < 1) :
        print("Axis {} value: {:>6.3f}".format(i, axis) ) #四舍五入 1
    eel.sleep(0.01) # 调整频率


# todo
'''
小庄公告板：
    可以使用两个程序共同读写一个本地文件来做，依赖同一个资源，而不必使用多进程
    那就需要redis 另一个client去写 去订阅redis
    树莓派redis已经启动 同时保留log
'''