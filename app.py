import pygame,sys
from random import randint
ORIGIN_ALTITUDE,SCALE = 5700, 0.15
DATA_X_MAX,DATA_Y_MAX = 1401,1401
SCREEN_W,SCREEN_H  = 1400,640
def RT_get_drawy(z):
    return SCREEN_H-(z-ORIGIN_ALTITUDE)*SCALE

# data read
datafile = open('Qomolangma.asc','r')
strList = datafile.readlines()
datafile.close()
# pygame init
pygame.init()
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption('3d viewer')
screen.fill((0,0,225))
# draw North
maxList, minList = [0]*DATA_X_MAX,[SCREEN_H]*DATA_X_MAX 
dataList = []

for dataStr in strList:
    dataStr =  dataStr.strip('\n')
    line = []
    for s in dataStr.split(' '):
        line.append(eval(s))
    dataList.append(line)
    x0,z0=0,RT_get_drawy(line[DATA_X_MAX-1])
    for x in range(DATA_X_MAX):
        z = RT_get_drawy(line[DATA_X_MAX-1-x])
        flag = 0
        if z<minList[x]:
            minList[x],flag = z,1
        if z>maxList[x]:
            maxList[x],flag = z,1
        if flag == 1 and abs(z-z0)<100:
            pygame.draw.line(screen,(225,0,0),(x0,z0),(x,z),1)
        x0,z0 = x,z
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()