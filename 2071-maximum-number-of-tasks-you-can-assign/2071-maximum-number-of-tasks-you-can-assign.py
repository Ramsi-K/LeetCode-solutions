class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        n = len(tasks)
        m = len(workers)
        
        left, right = 0, min(n, m)

        def can_complete(k):
            # Take the k smallest tasks
            curr_tasks = tasks[:k]
            
            # Use a list to track which workers are available
            available_workers = workers.copy()
            remaining_pills = pills
            
            # Try to assign tasks from hardest to easiest
            for i in range(k-1, -1, -1):
                task = curr_tasks[i]
                assigned = False
                
                # First try to assign without using a pill
                # Find the weakest worker who can complete the task
                worker_idx = -1
                for j in range(len(available_workers)):
                    if available_workers[j] >= task:
                        worker_idx = j
                        break
                
                if worker_idx != -1:
                    # Found a worker who can do the task without a pill
                    assigned = True
                    # Remove this worker from available workers
                    available_workers.pop(worker_idx)
                    continue
                
                # If we can't assign without a pill, try with a pill
                if remaining_pills > 0:
                    # Find the weakest worker who can complete the task with a pill
                    worker_idx = -1
                    for j in range(len(available_workers)):
                        if available_workers[j] + strength >= task:
                            worker_idx = j
                            break
                    
                    if worker_idx != -1:
                        # Found a worker who can do the task with a pill
                        assigned = True
                        # Remove this worker from available workers
                        available_workers.pop(worker_idx)
                        remaining_pills -= 1
                
                if not assigned:
                    # Cannot assign this task
                    return False
            
            return True
        
        # Binary search for the maximum number of tasks
        while left <= right:
            mid = (left + right) // 2
            if can_complete(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right