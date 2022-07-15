#https://www.acmicpc.net/problem/11279
import sys

input = sys.stdin.readline

N = int(input())
queue = []

def up_heapify(index, queue_up):
    child_index = index
    while child_index != 0:
        parent_index = (child_index-1)//2
        if queue_up[parent_index] <queue_up[child_index]:
            queue_up[parent_index],queue_up[child_index] = queue_up[child_index], queue_up[parent_index]
            child_index = parent_index
        else:
            return

def find_child_index(index, heap_size):
    parent = index
    left_child = (parent*2) + 1
    right_child = (parent*2) + 2
    if left_child < heap_size and queue[parent] < queue[left_child]:
        parent = left_child
    if right_child < heap_size and queue[parent] < queue[right_child]:
        parent = right_child
    return parent

def dn_heapify(index, queue_dn):
    parent_index = index
    bigger_child_index = find_child_index(parent_index, len(queue_dn))
    while parent_index != bigger_child_index:
        queue_dn[parent_index], queue_dn[bigger_child_index] = queue_dn[bigger_child_index], queue_dn[parent_index]
        parent_index = bigger_child_index
        bigger_child_index = find_child_index(parent_index, len(queue_dn))

def heap_pop(queue_pop):
    if len(queue_pop) == 0:
        return 0
    temp = queue_pop[0]
    queue_pop[0] = queue_pop[-1]
    queue_pop.pop()
    dn_heapify(0, queue_pop)
    return temp

for i in range(N):
    x = int(input())
    if x == 0:
        print(heap_pop(queue))
    else:
        queue.append(x)
        up_heapify(len(queue)-1, queue)