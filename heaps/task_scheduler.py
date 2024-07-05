# 621. Task Scheduler
# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
# ​Return the minimum number of intervals required to complete all tasks.

import heapq
def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    counts = {task: tasks.count(task) for task in set(tasks)}
    maxHeap = [-x for x in counts.values()]
    heapq.heapify(maxHeap)
    queue = []
    time = 0
    while maxHeap or queue:
        # if there are tasks waiting in the queue, check to see if they can be ran
        time +=1 
        # pop task_to_run, increase value, calculate the time when it can be ran again, and put that tuple into the queue 
        if maxHeap:
            task_to_run = heapq.heappop(maxHeap) + 1
            if task_to_run:
                queue.append([task_to_run, time + n])
        if queue:
            # if the second value in stored task is == to the global time, add this task back to the queue
            if queue[0][1] == time:
                task_to_add_back_to_maxHeap = queue.pop(0)[0]
                if task_to_add_back_to_maxHeap != 0:
                    heapq.heappush(maxHeap, task_to_add_back_to_maxHeap)
    return time



# Example 1:
n1 = 2
tasks1 = ["A","A","A","B","B","B"]
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.


# Example 2:
tasks2 = ["A","C","A","B","D","B"]
n2 = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:
tasks3 = ["A","A","A", "B","B","B"]
n3 = 3
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

print(leastInterval(tasks1, n1))
print(leastInterval(tasks2, n2))
print(leastInterval(tasks3, n3))