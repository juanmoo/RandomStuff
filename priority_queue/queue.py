'''
Priority Queue

Operations:
    1. Insert (key, element)
    2. Pop max
    3. Is empty
'''

class TwoQueue(object):
    def __init__(self):
        self.queue = []
        self.temp = []

    def is_empty(self):
        return len(self.queue) == 0

    def pop(self):
        if not self.is_empty():
            # Elements are stored as (key, value)
            return self.queue.pop()[1]
        return False

    def insert(self, key, val):
        # Move elements w/ higher priority to temp stack
        while(len(self.queue) > 0 and self.queue[-1][0] > key):
            self.temp.append(self.queue.pop())

        self.queue.append((key, val))

        while(len(self.temp) > 0):
            self.queue.append(self.temp.pop())

class oneQueue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def pop(self):
        if not self.is_empty():
            # Elements are stored as (key, value)
            return self.queue.pop()[1]
        return False

    def insert(self, key, value):
        if len(self.queue) > 0 and self.queue[-1][0] > key:
            temp = self.queue.pop()
            self.insert(key, value)
            self.queue.append(temp)
        else:
            self.queue.append((key, value))



#tq = TwoQueue()
tq = oneQueue()
for k in range(9, -1, -1):
    print('Inserting', k)
    tq.insert(k, 2*k)

print(tq.queue)


