
def count_steps(l: list)->None:
    """
    Расчет шагов относительно медианы
    :param l: Список переменных
    :return:
    """
    l.sort()
    print(l)
    median = l[len(l)//2]
    moves = sum(abs(x-median)for x in l)

    if moves > 20:
        print('20 ходов недостаточно для приведения всех элементов массива к одному числу')
    else:
        print(moves)


def main():
    file_path = input()
    nums = []
    with open(file_path, 'r') as f:
        nums = [int(x) for x in f.read().split()]
    count_steps(nums)

if __name__ == '__main__':
    main()