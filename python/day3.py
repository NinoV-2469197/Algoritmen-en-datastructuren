from plotter import count, lt, eq   # This assumes the plotter module has these

def insertion_sort(A):
    """
    Sorteert een lijst A met Insertion Sort.
    Args:
    A: De te sorteren lijst.
    """
    n = len(A)
    for i in range(1, n):
        insert = A[i]
        place = i
        while place > 0 and lt(insert, A[place - 1]):
            A[place] = A[place - 1]
            place -= 1
        A[place] = insert
    return A

def bubble_sort(A):
    """
    Sorteert een lijst A met Bubble Sort.
    Args:
    A: De te sorteren lijst.
    """
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if lt(A[j + 1], A[j]):
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

# print(insertion_sort([3, 4, 1, 2, 6]))
# print(bubble_sort([3, 4, 1, 2, 6]))