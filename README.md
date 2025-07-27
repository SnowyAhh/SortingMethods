# SortingMethods
## About
<p>
    Methods for sorting kept in one place for my own convenience.
</p>
<p>
    Since Python does not have built in arrays, lists are used in place. 
    But array and list are used interchangeably outside of the code.
</p>
<p>
    Sorting is only done for integers.
</p>
<p>
    Includes code in python, a short description, and time complexity.
</p>

## To do:
<ul>
    <li>Bubble sort</li>
    <li>Early termination bubble sort</li>
    <li>Insertion sort</li>
    <li>Topological sort</li>
    <li>Merge sort</li>
    <li>Quick sort</li>
    <li>Heap sort</li>
    <li>Counting sort</li>
</ul>

## Methods:
### Selection sort
<div>
    <p>
        <b>Complexity:</b>
    </p>
    <p>
        n swaps and n^2 comparisons regardless of case, therefore, O(n^2) complexity
    </p>
    <p>
        <b>Stability:</b> Not stable
    </p>
    <ul>
        <li>Brute force</li>
        <li>Best for small arrays or when writes are more expensive than reads</li>
        <li>Needs a minimal of n - 1 swaps</li>
    </ul>
</div>
<div>
    <b>Steps:</b>
    <ol>
        <li>
            Find the smallest element, swap it with the first element in the array
        </li>
        <li>
            Find the second smallest element, swap it with the second element in the array
        </li>
        <li>
            Repeat until end of array
        </li>
    </ol>
</div>

### Bubble sort
<div>
    <p>
        <b>Complexity:</b>
    </p>
    <ul>
        <li>
            Best case (already sorted): n^2/2 comparisons and 0 swaps, therefore O(n^2)
        </li>
        <li>
            Average case (in a random order): n^2/2 comparisons and n^2/2 swaps, therefore O(n^2) 
        </li>
        <li>
            Worst case (Reverse order): n^2/2 comparisons and n^2/2 swaps, therefore O(n^2)
        </li>
    </ul>
    <p>
        <b>Stability:</b> Stable
    </p>
    <ul>
        <li>Brute force</li>
        <li>Needs a minimal of n - 1 swaps</li>
    </ul>
</div>
<div>
    <b>Steps:</b>
    <ol>
        <li>
            Compare first element with the next element in the array, swapping them if the next element is smaller. Continue swapping until the algorithm reaches the end of the array. Now the largest element is at the end of the list
        </li>
        <li>
            Repeat the first step but until the second-last element of the array and so on, with each iteration stopping one element before. Stop only when all of the elements have been sorted
        </li>
    </ol>
</div>

### Early Termination Bubble sort
<div>
    <p>
        <b>Complexity:</b>
    </p>
    <ul>
        <li>
            Best case (already sorted): n - 1 comparisons and 0 swaps, therefore O(n)
        </li>
        <li>
            Average case (in a random order): Depends on the data set, but only a few would be able to terminate early. The complexity would be lower than regular bubble sort, but the complexity is still likely to be O(n^2) 
        </li>
        <li>
            Worst case (Reverse order): The same as regular bubble sort; n^2/2 comparisons and n^2/2 swaps, therefore O(n^2)
        </li>
    </ul>
    <p>
        <b>Stability:</b> Stable
    </p>
    <ul>
        <li>Brute force</li>
        <li>
            Similar to bubble sort, but if no swaps are made, then break the loop
        </li>
    </ul>
</div>

### Insertion sort
### Topological sort
<div>
    <p>
        (Using source removal method)
    </p>
    <p>Using matrix, and using list</p>
</div>

### Merge sort
### Quick sort
### Heap sort
### Counting sort