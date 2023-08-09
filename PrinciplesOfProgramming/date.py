class Date:
    def __init__(self, month, day):
        self._month = month
        self._day = day
    @property
    def month(self):
        return self._month
    @month.setter
    def month(self, value):
        if not 1 <= value <= 12:
            raise ValueError("Invalid month")
        self._month = value
    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, value):
        if not 1 <= value <= self.days_in_month():
            raise ValueError("Invalid day")
        self._day = value
    def advance(self):
        days_in_month = self.days_in_month()
        if self._day < days_in_month:
            self._day += 1
        else:
            self._day = 1
            self._month += 1
            if self._month > 12:
                self._month = 1
    def days_in_month(self):
        _days = 31
        if self._month in (4, 6, 9, 11):
            _days = 30
        if self._month == 2:
            _days = 28
        return _days


    def absolute_day(self):
        _abs_day = self._day
        for i in range(1, self._month):
            _abs_day += Date(i, 1).days_in_month()
        return _abs_day

    def from_absolute_day(self, abs_day):
        self._month = 1
        while abs_day > self.days_in_month():
            abs_day -= self.days_in_month()
            self._month += 1
        # self._month = month
        self._day = abs_day

    def __eq__(self, other):
        return self._month == other.month and self._day == other.day
    def __str__(self):
        return f"{self._month}/{self._day}"

date_obj = Date(7, 4)
# date_obj.day = 28
# date_obj.month = 2
# print(date_obj.days_in_month())
# print(date_obj.absolute_day())
date_obj.from_absolute_day(305)
print(date_obj.month)
print(date_obj.day)