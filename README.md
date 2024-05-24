# Sorting Algorithm Visualizer Using py-game

## Summary of Features
- **Graphical Visualization**: Visual representation of sorting algorithms.
- **User Input via GUI**: Interactive input for the number of elements and their value range.
- **Multiple Algorithms**: Visualization for various sorting algorithms.
- **Algorithm Selection**: Easy switching between different algorithms using keyboard shortcuts.
- **Sorting Order Control**: Option to sort in ascending or descending order.
- **Control Over Sorting**: Start, pause, and reset the sorting process.
- **Real-time Updates**: Visual feedback on the sorting process with color-coded comparisons and swaps.
- **Responsive Layout**: Adaptation to different window sizes.
- **User Instructions**: Clear instructions and feedback provided within the GUI.

## Algorithms Explanation and Complexity

### Bubble Sort
**Explanation**: 
- Compares and swaps adjacent elements if they are in the wrong order.
- Multiple passes are made through the list until it is sorted.

**Time Complexity**:
- Best: O(n)
- Average: O(n^2)
- Worst: O(n^2)

**Space Complexity**: O(1)

### Insertion Sort
**Explanation**: 
- Iterates over the list, inserting each element into its correct position in the sorted portion.

**Time Complexity**:
- Best: O(n)
- Average: O(n^2)
- Worst: O(n^2)

**Space Complexity**: O(1)

### Quick Sort
**Explanation**: 
- Uses a pivot to partition the list into sub-lists, recursively sorting each sub-list.

**Time Complexity**:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n^2)

**Space Complexity**: O(log n)

### Merge Sort
**Explanation**: 
- Divides the list into sub-lists, recursively sorts them, and merges the sorted sub-lists.

**Time Complexity**:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)

**Space Complexity**: O(n)

### Selection Sort
**Explanation**: 
- Selects the minimum element from the unsorted portion and swaps it with the first unsorted element.

**Time Complexity**:
- Best: O(n^2)
- Average: O(n^2)
- Worst: O(n^2)

**Space Complexity**: O(1)

### Heap Sort
**Explanation**: 
- Builds a max heap from the list, then repeatedly removes the largest element and rebuilds the heap.

**Time Complexity**:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)

**Space Complexity**: O(1)

### Shell Sort
**Explanation**: 
- Sorts elements far apart and gradually reduces the gap between elements to be sorted.

**Time Complexity**:
- Best: O(n log n)
- Average: O(n (log n)^2)
- Worst: O(n (log n)^2)

**Space Complexity**: O(1)

### Comb Sort
**Explanation**: 
- Similar to Bubble Sort, but compares elements far apart and reduces the gap over iterations.

**Time Complexity**:
- Best: O(n log n)
- Average: O(n^2 / 2^p)
- Worst: O(n^2)

**Space Complexity**: O(1)

