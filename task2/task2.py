from math import hypot

def elipse_distance(x, y, cx, cy, rx, ry):
    '''
    Расчет положения точки на эллипсе
    :param x: Координата точки по х
    :param y: Координата точки по У
    :param cx: Центр эллипса по х
    :param cy: Центр эллипса по у
    :param rx: Большой радиус эллипса
    :param ry: Меньший радиус эллипса
    :return: Значение ответа
    '''
    k = (x-cx)**2/rx**2 + (y-cy)**2/ry**2
    return k

with open('circle.txt','r') as file:
    x1,y1 = map(float,file.readline().split())
    # Предположительно:
    # x2 - радиус по горизонтали, y2 - радиус по вертикали
    x2,y2 = map(float,file.readline().split())


with open('dots.txt','r') as file:
    for d in file:
        x,y = map(float,d.split())
        ans = elipse_distance(x,y,x1,y1,x2,y2)
        if ans < 1:
            print(0)
        elif ans ==1:
            print(1)
        else:
            print(2)

