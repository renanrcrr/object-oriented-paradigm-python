class Clock:

    def __init__(self, hour=0, min=0, sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec
    
    def ajustar_hora(self, hour, min, sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec
    
    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
    
    def tick(self):
        if self.sec == 59:
            self.sec = 0
            if self.min == 59:
                self.min = 0
                if self.hour == 23:
                    self.hour = 0
                else:
                    self.hour += 1
            else:
                self.min += 1
        else:
            self.sec += 1

rel = Clock(23, 59, 59)
print(rel)
rel.tick()
print(rel)