class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = None

    def append(self, item):
        #lets make sure that we are under capacity
        if len(self.storage) < self.capacity:
            #it's important that we set the oldest so we know what needs to be overwritten once we reach capacity
            #if this is the first item to be added we will set it to the oldest item at the first index of 0
            if len(self.storage) == 0:
                self.oldest = 0
            #otherwise the oldest will work itself from left to right to the index of 1.. 2.. etc.
            else:
                self.oldest += 1
            #append item to array
            self.storage.append(item)
        #and if we have reached capacity
        else:
            #we want to override the oldest item
            #what if it is the last item in the array? move back to beginning
            if self.oldest == self.capacity - 1:
                self.oldest = 0
            #if it is not the last item we just want to move left to right to find the oldest item
            else:
                self.oldest += 1
            #overwrite oldest item
            self.storage[self.oldest] = item

    def get(self):
        return self.storage