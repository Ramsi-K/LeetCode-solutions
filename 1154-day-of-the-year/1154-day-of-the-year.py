class Solution:
    def dayOfYear(self, date: str) -> int:
        days_in_month_normal = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        days_in_month_leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

        year, month, day = map(int, date.split('-'))
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        days_in_month = days_in_month_leap if is_leap_year else days_in_month_normal

        return days_in_month[month - 1] + day