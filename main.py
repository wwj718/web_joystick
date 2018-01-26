import eel
import pygame
pygame.init()
eel.init('web')                     # Give folder containing web files

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

g = 0

@eel.expose                         # Expose this function to Javascript
def get_key(x):
  global g
  # 再写一个进程？
  g += 1
  r = {"hello":"from backend:g={}".format(g)}
  print(r)
  return r
  '''
  while True:
    for event in pygame.event.get():
        # 获取joystick
        print(event) # mac不能获得键盘输入
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                print("Hey, you pressed the key, '0'!")
            if event.key == pygame.K_1:
                print("Doing whatever")
    #break        
    # 获取按键
    import time;time.sleep(1)
    print('Hello from %s' % x)
    '''

# say_hello_py('Python World!')
eel.py_console('Python World!')   # Call a Javascript function

eel.start('hello.html', size=(600, 400))    # Start

# todo
'''
xz公告板：
    可以使用两个程序共同读写一个本地文件来做，依赖同一个资源，而不必使用多进程
    那就需要redis 另一个client去写 去订阅redis
    树莓派redis已经启动 同时保留log
'''