# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #Создаем указатель ptr и присваиваем ему начальное значение head
        ptr = head
        #Пустая строка для хранения двоичной системы
        s = ''
        res = 0
        #изначально не равен None
        while ptr != None:
            #Преобразуем значение узла в строку и добавляем его к строке s
            # s += str(ptr.val)
            #преобразуем в двоичную систему
            res *= 2
            res += ptr.val
            #Переходим к следующему узлу списка
            ptr = ptr.next
        return res