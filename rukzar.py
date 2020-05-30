import operator
from random import randrange, shuffle
from copy import deepcopy
from itertools import combinations
from time import time


class Backpack:
    """
    Класс описания решения
    """
    def __init__(self, max_weight, possible_items):
        self.possible_items = possible_items
        self.items = []
        self.cost = 0
        self.weight = 0
        self.max_weight = max_weight

    def calc_cost(self):
        self.cost = 0
        for item in self.items:
            self.cost += item.cost
        return self.cost

    def tweak(self):
        """
        функция модификации рюкзака для локального поиска
        """
        possible_items = self.possible_items
        for packed_item in self.items:
            for item_key, item in enumerate(self.possible_items):
                if item.weight == packed_item.weight and item.cost == packed_item.cost:
                    del possible_items[item_key]
                    break
        for i in range(int(len(self.items))):
            popped_item = self.items.pop()
            self.weight -= popped_item.weight
        shuffle(possible_items)
        for item in possible_items:
            if self.weight + item.weight <= self.max_weight:
                self.weight += item.weight
                self.items.append(item)
        self.calc_cost()

    def quality(self):
        """
        Функция оценивания рюкзака для локального поиска
        """
        return self.cost

    def __str__(self):
        return f"В рюкзаке столько предметов: {len(self.items)}, весом {self.weight}, с общей стоимостью {self.cost}"


class Item:
    """
    Класс описания предмета
    """
    def __init__(self, weight, cost):
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return f"Сгенерирован предмет с весом {self.weight} и ценой {self.cost}"


def normal_algorithm(max_w, _items):
    items = [(item.weight, item.cost) for item in _items]
    result = max(filter(lambda x: sum(list(zip(*x))[0]) <= max_w, (v for r in range(1, len(items)) for v in combinations(filter(lambda x: x[0] <= max_w, items), r))), key=lambda x: sum(list(zip(*x))[1]))
    result_weight = sum([x[0] for x in result])
    result_cost = sum([x[1] for x in result])
    print(f'Получено решение: {len(result)}')
    print(f'Количество: {len(result)}')
    print(f'Вес: {result_weight}')
    print(f'Сумма: {result_cost}')


def generate_items(items_count):
    items = []
    for i in range(items_count):
        item = Item(randrange(10, 16), randrange(3, 26))
        print(item)
        items.append(item)
    return items


def pack_backpack(backpack):
    for item in backpack.possible_items:
        if backpack.weight + item.weight < backpack.max_weight:
            backpack.weight += item.weight
            backpack.items.append(item)


def random_search(restart_count, solution):
    solutions = []
    for i in range(restart_count):
        local_optimum = local_search(10, solution)
        solutions.append(local_optimum)

    solutions.sort(key=operator.attrgetter('weight'), reverse=False)
    solutions.sort(key=operator.attrgetter('cost'), reverse=True)
    # [print(x) for x in solutions]
    return solutions[0]


def local_search(restart_count, solution):
    for _ in range(restart_count):
        new_solution = deepcopy(solution)
        new_solution.tweak()
        if solution.quality() < new_solution.quality():
            solution = deepcopy(new_solution)
    return solution


possible_items = generate_items(23)

start_time = time()
normal_algorithm(100, possible_items)
print(f'Затраченое время на обычное решение через комбинаторику: {time() - start_time}')

start_time = time()
solution = Backpack(100, possible_items)
pack_backpack(solution)
answer = random_search(100, solution)
print('Упаковываем рюкзак...')
print('Было найдено решение:')
print(answer)
print(f'Затраченое время на решение через локальный поиск со случайными перезапусками: {time() - start_time}')



