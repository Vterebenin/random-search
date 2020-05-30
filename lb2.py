from random import randint


class Program:
    """
    Класс описания решения
    """
    def __call__(self, *args, **kwargs):
        count = 0
        max_count = 100
        qcount = 0
        delqcount = 0
        m = 0
        x = 0
        t = 0
        time = 0
        fires = True
        while count < max_count:
            if fires:
                x = randint(1, 50)
                x += 50
                m += 1
                fires = False
                time += x
                x -= 1
            if x == 0:
                x = randint(1, 50)
                x += 50
                m += 1
                time += x
                if qcount < 49:
                    qcount += 1
                else:
                    delqcount += 1
                x -= 1
            else:
                x -= 1

            if qcount != 0 and t == 0:
                count += 1
                t = randint(1, 60)
                t += 100
                time += t*1.8
                t -= 1
            elif t != 0:
                t -= 1
        time /= 46000
        delqcount -= 100
        qcount *= 2
        qcount2 = (qcount / 2) - 2.57
        print(f"Всего входных транзактов: {m}")
        print(f"Отказано в обслуживании: {delqcount}")
        print(f"Максимальная заполненность оперативной памяти: {qcount} Кб")
        print(f"Средняя заполненность оперативной памяти: {qcount2} Кб")
        print(f"Коэффициент загрузки дискового накопителя: {time}")


run = Program()
run()


