import pygame
import random
import math

pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    BLUE = 0, 0, 255
    RED = 255, 0, 0
    YELLOW = 255, 255, 0
    BACKGROUND_COLOR = (30, 30, 30)

    GRADIENTS = [
        (50, 50, 50),
        (100, 100, 100),
        (150, 150, 150)
    ]

    FONT = pygame.font.SysFont('segoeui', 20)
    LARGE_FONT = pygame.font.SysFont('segoeui', 30)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1,
                                        draw_info.YELLOW)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1,
                                     draw_info.WHITE)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 45))

    sorting = draw_info.FONT.render(
        "I - Insertion | B - Bubble | Q - Quick | M - Merge | S - Selection | H - Heap | E - Shell | C - Comb", 1,
        draw_info.WHITE)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 75))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
        pygame.draw.rect(draw_info.window, draw_info.BLACK, (x, y, draw_info.block_width, draw_info.height),
                         1)  # Border

    if clear_bg:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def get_input_values(draw_info):
    n, min_val, max_val = "", "", ""
    active_input = None

    font = pygame.font.SysFont('segoeui', 30)
    button_font = pygame.font.SysFont('segoeui', 20)

    input_boxes = {
        'n': pygame.Rect(draw_info.width // 2 - 50, draw_info.height // 2 - 100, 100, 50),
        'min_val': pygame.Rect(draw_info.width // 2 - 50, draw_info.height // 2 - 20, 100, 50),
        'max_val': pygame.Rect(draw_info.width // 2 - 50, draw_info.height // 2 + 60, 100, 50),
    }

    input_labels = {
        'n': "Number of Elements:",
        'min_val': "Minimum Value:",
        'max_val': "Maximum Value:"
    }

    input_texts = {
        'n': n,
        'min_val': min_val,
        'max_val': max_val
    }

    submit_button = pygame.Rect(draw_info.width // 2 - 50, draw_info.height // 2 + 150, 100, 50)
    submit_button_text = "Submit"

    while True:
        draw_info.window.fill(draw_info.BACKGROUND_COLOR)

        for label, rect in input_boxes.items():
            pygame.draw.rect(draw_info.window, draw_info.WHITE, rect, 2)
            label_surface = font.render(input_labels[label], True, draw_info.WHITE)
            draw_info.window.blit(label_surface, (rect.x - label_surface.get_width() - 10, rect.y + 10))
            text_surface = font.render(input_texts[label], True, draw_info.WHITE)
            draw_info.window.blit(text_surface, (rect.x + 5, rect.y + 10))

        pygame.draw.rect(draw_info.window, draw_info.WHITE, submit_button)
        button_text_surface = button_font.render(submit_button_text, True, draw_info.BLACK)
        draw_info.window.blit(button_text_surface, (submit_button.x + (submit_button.width - button_text_surface.get_width()) // 2,
                                                     submit_button.y + (submit_button.height - button_text_surface.get_height()) // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None, None, None

            if event.type == pygame.MOUSEBUTTONDOWN:
                for key, rect in input_boxes.items():
                    if rect.collidepoint(event.pos):
                        active_input = key
                        break
                if submit_button.collidepoint(event.pos):
                    if input_texts['n'] and input_texts['min_val'] and input_texts['max_val']:
                        try:
                            n, min_val, max_val = int(input_texts['n']), int(input_texts['min_val']), int(input_texts['max_val'])
                            if n > 5 and min_val > 0 and max_val > 1 and max_val > min_val:
                                return n, min_val, max_val
                        except ValueError:
                            pass

            if event.type == pygame.KEYDOWN and active_input is not None:
                if event.key == pygame.K_BACKSPACE:
                    input_texts[active_input] = input_texts[active_input][:-1]
                elif event.key == pygame.K_RETURN:
                    active_input = None
                else:
                    input_texts[active_input] += event.unicode

# How It Works:
# Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name because smaller elements "bubble" to the top of the list.
# Time Complexity:
# Best Case: O(n) (when the array is already sorted)
# Average & Worst Case: O(n^2)
def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True) # Swapping - red and blue.
                yield True

    return lst


# How It Works:
# Insertion Sort builds the final sorted array one item at a time. It iterates through the list and removes one element per iteration, finds the appropriate location within the sorted portion of the array, and inserts it there.
# Time Complexity:
# Best Case: O(n) (when the array is already sorted)
# Average & Worst Case: O(n^2)
def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

    return lst


# Quick Sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.
# Time Complexity:
# Best Case & Average Case: O(n log n)
# Worst Case: O(n^2) (when the pivot elements are the smallest or largest elements)
def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    stack = [(0, len(lst) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot_index = start
        pivot = lst[end]
        for i in range(start, end):
            if (lst[i] < pivot and ascending) or (lst[i] > pivot and not ascending):
                lst[i], lst[pivot_index] = lst[pivot_index], lst[i]
                pivot_index += 1
        lst[pivot_index], lst[end] = lst[end], lst[pivot_index]
        draw_list(draw_info, {pivot_index: draw_info.GREEN}, True)
        yield True

        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))

    return lst


# Merge Sort is also a divide-and-conquer algorithm. It works by dividing the list into equal halves until each small part has one element, then merging those halves in a sorted manner until the entire list is sorted.
# Time Complexity:
# All Cases: O(n log n)
def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    current_size = 1

    while current_size < len(lst):
        left = 0
        while left < len(lst) - current_size:
            mid = left + current_size - 1
            right = min((left + 2 * current_size - 1), (len(lst) - 1))

            temp = []
            left_subarray = lst[left:mid + 1]
            right_subarray = lst[mid + 1:right + 1]
            while left_subarray and right_subarray:
                if (left_subarray[0] < right_subarray[0] and ascending) or (
                        left_subarray[0] > right_subarray[0] and not ascending):
                    temp.append(left_subarray.pop(0))
                else:
                    temp.append(right_subarray.pop(0))
            temp.extend(left_subarray)
            temp.extend(right_subarray)

            for i in range(left, right + 1):
                lst[i] = temp[i - left]
                draw_list(draw_info, {i: draw_info.BLUE}, True)
                yield True

            left += current_size * 2

        current_size *= 2

    return lst


# Selection Sort divides the input list into two parts: a sorted sublist of items which is built up from left to right and a sublist of the remaining unsorted items. The algorithm proceeds by finding the smallest (or largest) element in the unsorted sublist, swapping it with the leftmost unsorted element, and moving the sublist boundaries one element to the right.
# Time Complexity:
# All Cases: O(n^2)
def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
        min_index = i

        for j in range(i + 1, len(lst)):
            if (lst[j] < lst[min_index] and ascending) or (lst[j] > lst[min_index] and not ascending):
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]
        draw_list(draw_info, {i: draw_info.GREEN, min_index: draw_info.RED}, True)
        yield True

    return lst


# Heap Sort is a comparison-based sorting technique based on a binary heap data structure. It's similar to selection sort, where we first find the maximum element and place it at the end. We repeat the same process for the remaining elements.
# Time Complexity:
# All Cases: O(n log n)
def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(lst, n, i, ascending, draw_info)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        yield from heapify(lst, i, 0, ascending, draw_info)
        yield True


def heapify(lst, n, i, ascending, draw_info):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and ((lst[left] > lst[largest] and ascending) or (lst[left] < lst[largest] and not ascending)):
        largest = left

    if right < n and ((lst[right] > lst[largest] and ascending) or (lst[right] < lst[largest] and not ascending)):
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        draw_list(draw_info, {i: draw_info.GREEN, largest: draw_info.RED}, True)
        yield True
        yield from heapify(lst, n, largest, ascending, draw_info)


# Shell Sort is an optimization over Insertion Sort. It starts by sorting elements far apart from each other and successively reducing the interval between the elements to be sorted. The interval is reduced based on a sequence (e.g., gap = gap / 2).
# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n^1.5)
# Worst Case: O(n^2)
def shell_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and ((lst[j - gap] > temp and ascending) or (lst[j - gap] < temp and not ascending)):
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
            draw_list(draw_info, {j: draw_info.GREEN, j + gap: draw_info.RED}, True)
            yield True
        gap //= 2

    return lst


# Comb Sort improves upon Bubble Sort by comparing elements that are farther apart to eliminate large values from the end of the list more quickly. The gap starts large and shrinks by a shrink factor (commonly 1.3) until it becomes 1.
# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n^2 / 2^p)
# Worst Case: O(n^2)
def comb_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        for i in range(n - gap):
            j = i + gap
            if (lst[i] > lst[j] and ascending) or (lst[i] < lst[j] and not ascending):
                lst[i], lst[j] = lst[j], lst[i]
                sorted = False
                draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
                yield True

    return lst


def main():
    run = True
    clock = pygame.time.Clock() # initialize clock

    draw_info = DrawInformation(1000, 700) # Window Size

    n, min_val, max_val = get_input_values(draw_info)

    if n is None or min_val is None or max_val is None:
        return

    lst = generate_starting_list(n, min_val, max_val) # Generate List To Sort
    draw_info.set_list(lst)

    sorting = False # Is Sorting
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60) # Number of Frames/Sec

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)


        # Input Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort
                sorting_algo_name = "Quick Sort"
            elif event.key == pygame.K_m and not sorting:
                sorting_algorithm = merge_sort
                sorting_algo_name = "Merge Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"
            elif event.key == pygame.K_h and not sorting:
                sorting_algorithm = heap_sort
                sorting_algo_name = "Heap Sort"
            elif event.key == pygame.K_e and not sorting:
                sorting_algorithm = shell_sort
                sorting_algo_name = "Shell Sort"
            elif event.key == pygame.K_c and not sorting:
                sorting_algorithm = comb_sort
                sorting_algo_name = "Comb Sort"

    pygame.quit()

if __name__ == "__main__":
    main()
