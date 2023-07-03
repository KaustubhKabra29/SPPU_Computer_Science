"""
Parallel mergesort versus sequential and built-in.
Using multiprocessing Process/Pipe.

$ python[3] parallelMergesort.py [500000]

This code exemplifies the Process/Pipe paradigm of
parallel design.  Mergesort says simply:
-sort the left side of the list.
-sort the right side of the list.
-merge the results.
So a parallel version comes from the realization that
the two sorts are independent of one another.
-sort the left and right sides in parallel
-merge the results.

Process objects are instantiated to perform the
sorting on the left and right sublists. Pipes are
used to transmit the sorted sublists back up the
execution tree.

This mergesort is not standard; it is NlogN in memory,
and does not sort the argument lyst as a side effect,
but rather returns a sorted version of the lyst.

See:
http://docs.python.org/library/multiprocessing.html
http://docs.python.org/py3k/library/multiprocessing.html
"""

import random
import sys
import time
from multiprocessing import Process, Pipe


# Dependencies defined below main()

def main():
    """
    This is the main method, where we:
    -generate a random list.
    -time a sequential mergesort on the list.
    -time a parallel mergesort on the list.
    -time Python's built-in sorted on the list.
    """
    N = 50000
    if len(sys.argv) > 1:  # the user input a list size.
        N = int(sys.argv[1])
    print('Number of Elements in list:%i' % N)
    # We want to sort the same list, so make a backup.
    lystbck = [random.random() for x in range(N)]

    # Sequential mergesort a copy of the list.
    lyst = list(lystbck)
    start = time.time()  # start time
    lyst = mergesort(lyst)
    elapsed = time.time() - start  # stop time

    if not isSorted(lyst):
        print('Sequential mergesort did not sort. oops.')

    print('Sequential mergesort: %f sec' % elapsed)

    # So that cpu usage shows a lull.
    time.sleep(3)

    # Now, parallel mergesort.
    lyst = list(lystbck)
    start = time.time()
    n = 3  # 2**(n+1) - 1 processes will be instantiated.

    # Instantiate a Process and send it the entire list,
    # along with a Pipe so that we can receive its response.
    pconn, cconn = Pipe()
    p = Process(target=mergeSortParallel, args=(lyst, cconn, n))
    p.start()
    lyst = pconn.recv()
    # Blocks until there is something (the sorted list)
    # to receive.

    p.join()
    elapsed = time.time() - start

    if not isSorted(lyst):
        print('mergeSortParallel did not sort. oops.')

    print('Parallel mergesort: %f sec' % (elapsed))

    time.sleep(3)

    # Built-in test.
    # The underlying c code is obviously the fastest, but then
    # using a calculator is usually faster too.  That isn't the
    # point here, obviously.
    lyst = list(lystbck)
    start = time.time()
    lyst = sorted(lyst)
    elapsed = time.time() - start
    print('Built-in sorted: %f sec' % (elapsed))


def merge(left, right):
    """returns a merged and sorted version of the two already-sorted lists."""
    ret = []
    li = ri = 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            ret.append(left[li])
            li += 1
        else:
            ret.append(right[ri])
            ri += 1
    if li == len(left):
        ret.extend(right[ri:])
    else:
        ret.extend(left[li:])
    return ret


def mergesort(lyst):
    """
    The seemingly magical mergesort. Returns a sorted copy of lyst.
    Note this does not change the argument lyst.
    """
    if len(lyst) <= 1:
        return lyst
    ind = len(lyst) // 2
    return merge(mergesort(lyst[:ind]), mergesort(lyst[ind:]))


def mergeSortParallel(lyst, conn, procNum):
    """mergSortParallel receives a list, a Pipe connection to the parent,
       and procNum. Mergesort the left and right sides in parallel, then 
       merge the results and send over the Pipe to the parent."""

    # Base case, this process is a leaf or the problem is
    # very small.
    if procNum <= 0 or len(lyst) <= 1:
        conn.send(mergesort(lyst))
        conn.close()
        return

    ind = len(lyst) // 2

    # Create processes to sort the left and right halves of lyst.

    # In creating a child process, we also create a pipe for that
    # child to communicate the sorted list back to us.
    pconnLeft, cconnLeft = Pipe()
    leftProc = Process(target=mergeSortParallel, args=(lyst[:ind], cconnLeft, procNum - 1))

    # Create a process for sorting the right side.
    pconnRight, cconnRight = Pipe()
    rightProc = Process(target=mergeSortParallel, args=(lyst[ind:], cconnRight, procNum - 1))

    # Start the two subprocesses.
    leftProc.start()
    rightProc.start()

    # Recall that expression execution goes from first evaluating
    # arguments from inside to out.  So here, receive the left and
    # right sorted sublists (each receive blocks, waiting to finish),
    # then merge the two sorted sublists, then send the result
    # to our parent via the conn argument we received.
    conn.send(merge(pconnLeft.recv(), pconnRight.recv()))
    conn.close()

    # Join the left and right processes.
    leftProc.join()
    rightProc.join()


def isSorted(lyst):
    """
    Return whether the argument lyst is in non-decreasing order.
    """
    # Cute list comprehension way that doesn't short-circuit.
    # return len([x for x in
    #            [a - b for a,b in zip(lyst[1:], lyst[0:-1])]
    #            if x < 0]) == 0
    for i in range(1, len(lyst)):
        if lyst[i] < lyst[i - 1]:
            return False
    return True


# Execute the main method now that all the dependencies
# have been defined.
# The if __name is so that pydoc works and we can still run
# on the command line.
if __name__ == '__main__':
    main()
