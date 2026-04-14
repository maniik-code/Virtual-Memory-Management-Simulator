# Virtual Memory Management Simulator
# Supports FIFO, LRU, Optimal Page Replacement

def fifo(pages, capacity):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1
        print(f"Memory: {memory}")
    
    return faults


def lru(pages, capacity):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1
        else:
            memory.remove(page)
            memory.append(page)

        print(f"Memory: {memory}")

    return faults


def optimal(pages, capacity):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < capacity:
                memory.append(pages[i])
            else:
                future = pages[i+1:]
                index = []

                for m in memory:
                    if m in future:
                        index.append(future.index(m))
                    else:
                        index.append(float('inf'))

                memory[index.index(max(index))] = pages[i]

            faults += 1

        print(f"Memory: {memory}")

    return faults

def segmentation():
    segments = int(input("Enter number of segments: "))
    segment_table = {}

    for i in range(segments):
        base = int(input(f"Enter base for segment {i}: "))
        limit = int(input(f"Enter limit for segment {i}: "))
        segment_table[i] = (base, limit)

    seg = int(input("Enter segment number: "))
    offset = int(input("Enter offset: "))

    if seg in segment_table:
        base, limit = segment_table[seg]
        if offset < limit:
            physical_address = base + offset
            print("Physical Address:", physical_address)
        else:
            print("Offset exceeds segment limit!")
    else:
        print("Invalid segment number!")

def main():
    pages = list(map(int, input("Enter page reference string: ").split()))
    capacity = int(input("Enter frame capacity: "))

    print("\n--- FIFO ---")
    fifo_faults = fifo(pages, capacity)
    print("Page Faults:", fifo_faults)

    print("\n--- LRU ---")
    lru_faults = lru(pages, capacity)
    print("Page Faults:", lru_faults)

    print("\n--- Optimal ---")
    opt_faults = optimal(pages, capacity)
    print("Page Faults:", opt_faults)
    
    print("\n--- Segmentation ---")
    segmentation()


if __name__ == "__main__":
    main()