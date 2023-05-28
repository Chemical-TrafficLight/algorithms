class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Создаем список counter, который будет хранить разницу между стоимостью для города B и стоимостью для города A.
        counter = [[c2 - c1,c1,c2] for c1, c2 in costs]
        # Сортируем список counter по возрастанию разницы между стоимостью для города B и стоимостью для города A.
        counter.sort()
        res = 0
        # Добавляем стоимость для города A для первой половины людей, а стоимость для города B - для второй половины людей.
        for i in range(len(counter)):
            res += counter[i][2] if i < len(counter) // 2 else counter[i][1]
        # Возвращаем суммарную стоимость.
        return res
