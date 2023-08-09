class Date:
    # Constructor initializes the state of new
    # Date objects as they are created by client code.
    # Raises a ValueError if values are out of range.
    def __init__(self, month, day):
        self.set_date(month, day)

    # Compares dates for equality.
    def __eq__(self, other):
        return self.month == other.month and self.day == other.day

    # Returns a string representation of a Date, such as "9/19".
    def __str__(self):
        return str(self._month) + "/" + str(self._day)

    # month property allows get/set access to Date's month value
    # must be between 1-12 inclusive, else a ValueError is raised
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self.set_date(value, self._day)

    # day property allows get/set access to Date's day value
    # must be between 1 - # of days in month, inclusive
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self.set_date(self._month, value)

    # Advances the Date's state to the next day,
    # wrapping into the next month/year as necessary.
    def advance(self):
        self._day += 1
        if self._day > self.days_in_month():
            # wrap to next month
            self._month += 1
            self._day = 1
            if self._month > 12:
                # wrap to next year
                self._month = 1

    # Returns the number of days in this Date's month.
    def days_in_month(self):
        if self._month in {4, 6, 9, 11}:
            return 30
        elif self._month == 2:
            return 28
        else:
            return 31

    # Modifies the date's month and day state.
    # Raises a ValueError if values are out of range.
    def set_date(self, month, day):
        if month >= 1 and month <= 12:
            self._month = month
        else:
            raise ValueError("Invalid month: " + str(month))
        if day >= 1 and day <= self.days_in_month():
            self._day = day
        else:
            raise ValueError("Invalid day: " + str(day))

def absolute_day(Date):
    _abs_day = _day
    for i in range(1, self._month):
        _abs_day += Date(i, 1).days_in_month()
    return _abs_day


date_obj = Date(12, 4)
date_obj.day = 28
date_obj.month = 2
print(date_obj.days_in_month())
print(date_obj.absolute_day())