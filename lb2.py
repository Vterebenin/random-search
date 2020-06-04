from random import randrange


class Program:
    """
    Класс описания решения
    """

    def __call__(self, *args, **kwargs):
        current_time = 3600
        queue_working_station_1 = 0
        queue_working_station_2 = 0
        queue_personal_evm = 0
        personal_evm = 0
        working_station_1 = 0
        working_station_2 = 0
        que_end_working_station_1 = None
        que_end_working_station_2 = None
        que_end_evm = None
        ws1_in_que = False
        ws2_in_que = False
        evm_in_que = False
        should_add_student = True
        new_student_time = 0
        students_count_in = 0

        while current_time > 0:  # пока идет время
            if should_add_student:  # Создаем по нормальному распределению нового студента с промежутком от 4-8
                should_add_student = False
                new_student_time = current_time - randrange(4, 8)
                students_count_in += 1
            current_time -= 1
            if new_student_time > 0 and current_time <= new_student_time:  # если установлено время, но студент уже добавлен
                should_add_student = True

            # если прошло время, убираем очереди
            if ws1_in_que and current_time < que_end_working_station_1:
                ws1_in_que = False
            if ws2_in_que and current_time < que_end_working_station_2:
                ws2_in_que = False
            if evm_in_que and current_time < que_end_evm:
                evm_in_que = False
                queue_working_station_1 += 1

            # если кто-то есть в очереди, добавляем
            if not evm_in_que and queue_personal_evm:
                evm_in_que = True
                queue_personal_evm -= 1
                personal_evm += 1
                que_end_evm = current_time - randrange(17, 20)
            elif not ws1_in_que and queue_working_station_1:
                ws1_in_que = True
                que_end_working_station_1 = current_time - randrange(22, 33)
                working_station_1 += 1
                queue_working_station_1 -= 1
            elif not ws2_in_que and queue_working_station_2:
                ws2_in_que = True
                que_end_working_station_2 = current_time - randrange(22, 33)
                working_station_2 += 1
                queue_working_station_2 -= 1

            # ограничиваем длину очереди до 4х по всей лаборатории
            if queue_working_station_2 + queue_working_station_1 + queue_personal_evm <= 4:

                # если пришло время добавить нового студента
                if current_time <= new_student_time:
                    # то с вероятностью 33% он идет на evm
                    go_for_evm = True if randrange(0, 3) == 2 else False

                    if go_for_evm and not evm_in_que:
                        evm_in_que = True
                        personal_evm += 1
                        que_end_evm = current_time - randrange(17, 20)
                    elif go_for_evm and evm_in_que:
                        queue_personal_evm += 1

                    # иначе он идет на ws2
                    if not go_for_evm and not ws2_in_que:
                        ws2_in_que = True
                        que_end_working_station_2 = current_time - randrange(22, 33)
                        working_station_2 += 1
                    elif not go_for_evm and ws2_in_que:
                        que_end_working_station_2 += 1

        # вывод результатов
        print('Занятость PC1:', working_station_1)
        print('Занятость PC2:', working_station_2)
        print('Занятость ПЭВМ:', personal_evm)
        print('Количество отказов:', students_count_in - (working_station_2 + personal_evm))
        print('Всего запросов:', students_count_in)


run = Program()
run()
