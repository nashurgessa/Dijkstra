
def heappop(heap):
    # print(heap)
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
    else:
        returnitem = lastelt
    return returnitem

def _shiftdown(heap, startpos, pos):
    newitem = heap[pos]

    while pos >> startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem[0] < parent[0]:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def _siftup(heap, pos):
    # print(heap)
    # hep = data, pos = [0, len(data)//2
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # print(newitem)
    
    childpos = 2*pos + 1
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos][0] < heap[rightpos][0]:
            childpos = rightpos
        
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
        # print(heap)
    
    heap[pos] = newitem
    _shiftdown(heap, startpos, pos)
    
def heapify(x):
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)