
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)   # sahte head
        current = dummy
        # carry = elde tutmak için
        carry = 0

        # while döngüsü, l1, l2 veya carry varsa devam eder
        # [2,4,3] =l1
        # [5,6,4] =l2 burdan ilerleyelim
        
        while l1 or l2 or carry:
            # eğer l1 veya l2 None ise 0 olarak kabul et
            # l1.val nedir: l1'in düğümündeki değeri temsil eder
            # [2,4,3] =l1 [5,6,4] =l2 örneği için val1 =2, val2=5
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Toplamı hesapla
            # [2,4,3]  [5,6,4] bu örnekte 2+5=7, 4+6=10, 3+4=7
            total = val1 + val2 + carry
            # Yeni carry ve basamağı hesapla
            # toplam 10'dan büyükse carry 1 olur, değilse 0
            # 10'a bölümünden kalan basamak olur
            carry = total // 10 # elde yani burda şunu yapıyor //: tam sayı bölmesi yapar
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
