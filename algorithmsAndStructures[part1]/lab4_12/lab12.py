import os
import heapq
import tempfile
import random

def external_sort(input_filename, output_filename, chunk_size=10):
    # Phase 1: Divide into sorted chunks
    with open(input_filename, 'r') as input_file:
        chunks = []
        chunk_number = 0
        while chunk_number!=20:
            chunk_size = 10
            chunk = sorted([line.strip() for line in (input_file.readline() for _ in range(chunk_size)) if line.strip()])
            print(chunk)
            if not chunk:
                print("awd",chunk)
                break
            chunk_filename = f'chunk_{chunk_number}.txt'
            with open(chunk_filename, 'w') as chunk_file:
                chunk_file.write('\n'.join(chunk))
            chunks.append(chunk_filename)
            chunk_number += 1

    # Phase 2: Merge sorted chunks
    with open(output_filename, 'w') as output_file:     
            handles = [open(chunk, 'r') for chunk in chunks]
            heap = [(handle.readline().strip(), i, handle) for i, handle in enumerate(handles) if handle.readline().strip()]
            heapq.heapify(heap)

            while heap:
                current, i, handle = heapq.heappop(heap)
                output_file.write(current + '\n')
                line = handle.readline().strip()
                if line:
                    print(line)
                    heapq.heappush(heap, (line, i, handle))
                else:
                    handle.close()
                    os.remove(chunks[i])

if __name__ == '__main__':
    input_filename = 'unsorted_data.txt'
    output_filename = 'sorted_data.txt'


    # Perform external sort
    external_sort(input_filename, output_filename)

    print("Sorting completed. Check the 'sorted_data.txt' file.")
