class Calendar:
    months = (31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30)

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def set_data(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.day, self.month, self.year)
    
    def next_date(self):
        max_day = Calendar.months[self.month - 1]

        if self.day == max_day:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1

# cal = Calendar(31, 1, 2024)
# print(cal)
# cal.next_date()
# print(cal)


