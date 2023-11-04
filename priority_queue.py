import queue

# Create an empty min-heap (priority queue)
min_heap = queue.PriorityQueue()

# Add elements to the min-heap
min_heap.put(5)
min_heap.put(2)
min_heap.put(9)
min_heap.put(1)

# Get and print the smallest element
smallest = min_heap.get()
print(smallest)  # Output: 1
print(min_heap.get())  # Output: 1
