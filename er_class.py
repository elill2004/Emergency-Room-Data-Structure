"""
   CISC-121 2022F

   Name:   <Elill Mathivannan>
   Student Number: <20342676>
   Email:  <elillmath2004@gmail.com>
   Date: 2022-12-05

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""


class Emergency_Room: #Priority Queue
    
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self.er_list = [] #list attribute for class
        
    def arrive(self, name, priority, time): #insert
        """
        -------------------------------------------------------
        Receives a name, priority level, and arrival time as
        parameters and then checks the priority level and arrival
        time with the other elements of the queue to find the 
        position within the emergency room queue.
        Use: pq.arrive(name, priority, time)
        -------------------------------------------------------
        Parameters:
            name - Patient's name (string)
            priority - Priority level (int)
            time - Arrival time (string)
        Returns:
            er_list.append(name, priority, time)
        -------------------------------------------------------
        """
        #convert time string to integer to sort
        arr_time = int(time.replace(':', ''))
        #if length of list 0 append name, priority, time to list
        if len(self.er_list) == 0:
            return self.er_list.append((name, priority, time))
        
        #iterate through list to sort priority levels in the queue
        for x in range(0, len(self.er_list)):
            #check priority level
            if self.er_list[x][1] > priority:
                return self.er_list.insert(x, (name, priority, time))
            #if priority level equal sort by arrival times
            elif self.er_list[x][1] == priority:
                if int(self.er_list[x][2].replace(':','')) > arr_time:
                    return self.er_list.insert(x, (name, priority, time))
        return self.er_list.append((name, priority, time))
    
    def schedule(self): #remove
        """
        -------------------------------------------------------
        Removes and returns the highest priority patient from the 
        emergency room queue.
        Use: value = pq.schedule()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue.
        -------------------------------------------------------
        """
        #if length of queue is 0 return 'Queue empty'
        if len(self.er_list) == 0:
            return 'Queue empty'
        
        #remove first elelment of queue(highest priority)
        value = self.er_list.pop(0)
        return value
    
    def announce(self): #peek
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the emergency room queue.
        Use: v = pq.announce()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. 
        -------------------------------------------------------
        """
        #find first element of queue(highest priority)
        value = self.er_list[0]
        return value
    
    
    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue 
        -------------------------------------------------------
        """
        #iterate through queue
        for value in self.er_list:
            yield value
    
    