# Создание класса с единственным методом tribonacci
class Solution:

    # Метод tribonacci принимает параметр n типа int и возвращает число типа int
    def tribonacci(self, n: int) -> int:

        # Если n меньше или равно двум
        if n <= 2:
            # Если n равно 0, то возвращаем 0
            if n == 0:
                return 0
            # Если n равно 1 или 2, то возвращаем 1
            if n == 1 or n == 2:
                return 1
        else:
            # Создаем список arr длиной n + 1, заполняем его единицами
            arr = [1] * (n + 1)
            # Записываем в нулевой элемент списка arr значение 0
            arr[0] = 0
            # Записываем во второй элемент списка arr значение 1
            arr[2] = 1
            # Заполняем список arr с третьего до последнего элемента, используя формулу чисел Трибоначчи
            for i in range(3, n + 1):
                arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
        # Возвращаем последний элемент списка arr, который является результатом функции
        return arr[n]