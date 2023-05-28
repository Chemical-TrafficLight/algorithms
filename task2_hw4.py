# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Создание класса решения
class Solution:
    # Создание метода, принимающего корень дерева и возвращающего минимальную разность между нодами
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Инициализация стэка с корнем дерева и списка для хранения значений нод
        stack = [root]
        res = []

        # Проход по дереву в глубину
        while stack:
            # Извлечение последнего элемента из стэка
            sort = stack.pop()
            # Добавление левой ноды в стек и значений в список res
            if sort.left:
                stack.append(sort.left)
                res.append((sort.left).val)
            # Добавление правой ноды в стек и значений в список res
            if sort.right:
                stack.append(sort.right)
                res.append((sort.right).val)

        # Инициализация переменной для хранения минимального значения
        min_values = 10 ** 6
        # Добавление значения корневой ноды в список res и сортировка списка
        res.append(root.val)
        res.sort()

        # Поиск минимальной разности между значениями нод
        for i in range(len(res)):
            if min_values > abs(res[i - 1] - res[i]):
                min_values = abs(res[i - 1] - res[i])
        # Возвращение минимальной разности значений нод
        return min_values