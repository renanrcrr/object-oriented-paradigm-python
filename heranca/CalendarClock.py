from Clock import Clock
from Calendar import Calendar

class CalendarClock(Clock, Calendar):
    def __init__(self, hour, min, sec, day, month, year):
        Clock.__init__(self, hour, min, sec)
        Calendar.__init__(self, day, month, year)
    
    def __str__(self):
        return Clock.__str__(self) + ' , ' + Calendar.__str__(self)
    
    def tick(self):
        previous_hour = self.hour
        Clock.tick(self)
        if self.hour < previous_hour:
            self.next_day(self)

cc = CalendarClock(23, 59, 59, 31, 12, 2024)
print(cc)