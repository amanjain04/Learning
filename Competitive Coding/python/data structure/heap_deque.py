from collections import Counter,deque
import heapq
a = [5,3,8,1,3,4,9]
counter = Counter(a)
print(counter) ## Counter({3: 2, 5: 1, 8: 1, 1: 1, 4: 1, 9: 1})
heap = [-v for v in counter.values()]
print(heap)  ## [-1, -2, -1, -1, -1, -1]
heapq.heapify(heap)
print(heap)  ## [-2, -1, -1, -1, -1, -1]
people = ['mario','luigi','deck']
q = deque(people)  ## deque implementation
print(q)  ## deque(['mario', 'luigi', 'deck'])
q.append('aman')
print(q) ## deque(['mario', 'luigi', 'deck', 'aman'])
q.popleft()
print(q) ## deque(['luigi', 'deck', 'aman'])
q.pop()
print(q) ## deque(['luigi', 'deck'])
q.appendleft('jain')
print(q) ## deque(['jain', 'luigi', 'deck'])
q.rotate(-1)
print(q)  ## deque(['luigi', 'deck', 'jain'])
q.rotate()
print(q)  ## deque(['jain', 'luigi', 'deck'])
q.extend(['kumar','sanu'])
print(q) ## deque(['jain', 'luigi', 'deck','kumar','sanu'])
q.reverse()
print(q) ## deque(['sanu', 'kumar', 'deck', 'luigi', 'jain'])