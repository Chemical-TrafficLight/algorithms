# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #Создаем пустой список для хранения значений в связанном списке
        vals = []
        cur_vertex = head
        #Пока head не равно None, добавляем значения в список vals и перемещаемся по списку
        while cur_vertex is not None:
            vals.append(cur_vertex.val)
            cur_vertex = cur_vertex.next
        #Сравниваем списки с перевернутым эквивалентом и возвращаем результат
        return vals == vals[::-1]