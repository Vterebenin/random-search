def quality(solution):
    """
    Берем решение, выявляем его качество
    :param solution: решение
    :return: возвращаем оценку решения в о.е. от 0 до 1
    """
    pass


def tweak(solution):
    """
    Функция модификации текущего решения
    :param solution: какое-то решение
    :return: модифицированное значение
    """
    return 0


def local_search(solution):
    """
    Функция локального поиска. обычно запускаем в каком-либо цикле, который зависит либо от времени, либо от условий
    :param solution:
    :return: лучшее из двух решений
    """
    new_solution = tweak(solution)
    if quality(new_solution) > quality(solution):
        solution = new_solution
    return solution




