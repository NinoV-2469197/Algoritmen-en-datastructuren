from plotter import plot
from day1 import *
from day2 import *
from day3 import *

#Comment out the days you don't need

# #Day 1
# plot([fib_it,fib_rec,fib_dict],30, "Different implementations of Fibonacci", "numeric")

# #Day 2
# plot([listlength, listlength2],1000, "Different implementations of List length", "list")
# plot([linearsearch, linearsearch_sentinel],1000, "Different implementations of linear search", "search")
# plot([linearsearch, binarysearch], 1000, "Linear vs binary search", "search")

#Day 3
plot([insertion_sort, bubble_sort], 50, "Insertion Sort vs Bubble Sort", 'list')