import heapq as hq
from contextlib import ExitStack
import sys


def merge_all(files):
    final_file = "Final_sorted_file.txt"

    with open(final_file, 'w') as sf:

        heap = []
        sorted_arr = []

        """
            Here heap is our traditional Min_Heap.

            sort_arr holds root of Min_Heap after each pop()
        """

        with ExitStack() as stack:

            """
                Here ExitStack() holds each file handler.

                enter_context : it adds each file handler

                file_names is a list comprehension of all sorted files                 
            """
            file_names = [stack.enter_context(open(file, 'r')) for file in files]

            for file in file_names:
                # add first element of each file into heap
                line = file.readline()
                # entry looks like [number, file_num]
                entry = list(map(int, line.strip().split()))
                # heapq takes a list object and heapify w.r.t first element
                hq.heappush(heap, entry)

            heap_root = hq.heappop(heap)

            # ['number file_number\n'] -> int(number), int(next_file)
            # We are adding the value of first root into sorted_arr,
            # and grabbing the next_file from which we push element into heap

            number, next_file = heap_root
            sorted_arr.append(str(number) + '\n')

            while True:
                line = file_names[next_file].readline()
                if not line:
                    # for num equivalent to infinity and using list to make it comparable to other entries
                    entry = [sys.maxsize]
                else:
                    entry = list(map(int, line.strip().split()))

                heap_root = hq.heappushpop(heap, entry)

                # heap[0] != sys.maxsize
                if heap_root == [sys.maxsize]:
                    break

                number, next_file = heap_root
                sorted_arr.append(str(number) + '\n')

                # Here I am emptying my sorted_arr after every 200 elements.
                # You can update it according to the available capacity of your hardware and your input.

                if len(sorted_arr) == 200:
                    sf.writelines(sorted_arr)
                    sorted_arr = []  # reset the necessary variables





