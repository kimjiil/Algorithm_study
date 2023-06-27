op1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
re1 = [0,0]

op2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
re2 = [333, -45]

def solution(operations):
    answer = []
    max_heap_arr = []
    min_heap_arr = []
    for operation in operations:
        op, num = operation.split(' ')
        if op == 'I':
            heap_insert(max_heap_arr, int(num))
            heap_insert(min_heap_arr, -int(num))
        elif op == 'D':
            if int(num) > 0: # 최대값 삭제
                max_heap_arr, delete_element = heap_delete(max_heap_arr)
                if not delete_element is None:
                    min_heap_arr, _ = heap_delete(min_heap_arr, -(delete_element))
            else: #최소값 삭제
                min_heap_arr, delete_element = heap_delete(min_heap_arr)
                if not delete_element is None:
                    max_heap_arr, _ = heap_delete(max_heap_arr, -(delete_element))
    if len(max_heap_arr) == 0:
        return [0, 0]

    _, max_value = heap_delete(max_heap_arr)
    _, min_value = heap_delete(min_heap_arr)
    return [max_value, -min_value]

def heap_insert(arr, a):
    arr.append(a)
    idx = len(arr) - 1
    while True:
        if arr[int((idx - 1)/2)] < arr[idx]: # 부모가 더작을 경우
            arr[idx] , arr[int((idx - 1)/2)] = arr[int((idx - 1)/2)], arr[idx]
            idx = int((idx - 1)/2)
        else:
            break

def heap_delete(arr, a = None):
    '''
            1) find, 삭제할 노드를 last 노드와 swap
            2) swap된 노드로 부터 아래로 heapify
            3) 양쪽 노드중 큰것과 swap
            4) 왼쪽 노드만 있는경우 swap
        '''

    # find
    if len(arr) == 0:
        return arr, None

    if not a:
        a = arr[0]
    idx = 0
    for index, i in enumerate(arr):
        if i == a:
            idx = index
            delete_element = a
            arr[idx], arr[-1] = arr[-1], arr[idx]
            arr = arr[:-1]
            break

    # heapify
    while idx < len(arr):
        # leaf node 인 경우
        if 2 * idx + 1 > len(arr) - 1:
            idx = 2 * idx + 1
            break
        else:
            # 양쪽 노드인 경우 왼쪽 노드만 있는 경우
            if 2 * idx + 2 <= len(arr) - 1: # 양쪽노드
                if arr[2 * idx + 2] > arr[2 * idx + 1]:
                    arr[idx], arr[2 * idx + 2] = arr[2 * idx + 2],  arr[idx]
                    idx = 2* idx + 2
                else:
                    arr[idx], arr[2 * idx + 1] = arr[2 * idx + 1], arr[idx]
                    idx = 2 * idx + 1
            else:
                arr[idx], arr[2 * idx + 1] = arr[2 * idx + 1], arr[idx]
                idx = 2 * idx + 1

    return arr, delete_element

result = solution(op1)
print(result)
result = solution(op2)
print(result)


'''
       0
   1       2
 3   4   5   6
7 8 9 10

i의 자식은  2i + 1 / 2i + 2 
'''


# 2023-06-27 다시 품
import heapq

class dual_queue:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.length = 0

    def __len__(self):
        return self.length

    def insert(self, element):
        heapq.heappush(self.max_heap, -element)
        heapq.heappush(self.min_heap, element)
        self.length += 1

    def delete(self, type):
        if self.length > 0:
            if type == 1: # 최대값 삭제
                heapq.heappop(self.max_heap)
                self.length -= 1

            elif type == -1: # 최소값 삭제
                heapq.heappop(self.min_heap)
                self.length -= 1


        if len(self.max_heap) == 0:
            self.min_heap = []
        if len(self.min_heap) == 0:
            self.max_heap = []
        if self.length == 0:
            self.max_heap = []
            self.min_heap = []

    def GetMinMax(self):
        if self.length > 0:
            return [-self.max_heap[0], self.min_heap[0]]
        else:
            return [0, 0]

def solution(operations):
    answer = []

    dq = dual_queue()
    for operation in operations:
        op, num = operation.split(' ')
        num = int(num)
        if op == 'I':
            dq.insert(num)
        elif op == 'D':
            dq.delete(num)

    return dq.GetMinMax()