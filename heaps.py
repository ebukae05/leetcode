#Heaps
import heapq

# #under the hood are arrays
# minHeap = []
# heapq.heappush(minHeap, 3)
# heapq.heappush(minHeap, 2)
# heapq.heappush(minHeap, 4)

# #min is always at index[0]
# print(minHeap[0])

# #to get smallest
# while len(minHeap):
#     print(heapq.heappop(minHeap))

# #no max heap at default
# #so multiply by -1
# maxHeap = []
# heapq.heappush(maxHeap, -3)
# heapq.heappush(maxHeap, -2)
# heapq.heappush(maxHeap, -4)

# #max is always at index[0]
# print(-1 * maxHeap[0])

# while len(maxHeap):
#     print(-1 * heapq.heappop(maxHeap))

#build heap from initial values
arr = [2,1,8,4,5]
heapq.heapify(arr)
print(arr)
while arr:
    print(heapq.heappop(arr))