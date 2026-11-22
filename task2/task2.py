from math import hypot

def elipse_distance(x: float, y:float, cx:float,
                    cy:float, rx:float, ry:float) -> float:
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


def main():
    ellipse_path = input()
    dots_path = input()

    with open(ellipse_path,'r') as file:
        x1,y1 = map(float,file.readline().split())
        # Предположительно:
        # x2 - радиус по горизонтали, y2 - радиус по вертикали
        x2,y2 = map(float,file.readline().split())


    with open(dots_path,'r') as file:
        for d in file:
            x,y = map(float,d.split())
            ans = elipse_distance(x,y,x1,y1,x2,y2)
            if ans < 1:
                print(0)
            elif ans ==1:
                print(1)
            else:
                print(2)


if __name__ == '__main__':
    main()