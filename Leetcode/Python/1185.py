class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
        if month == 1:
            year -= 1
            month = 13
        if month == 2:
            year -= 1
            month = 14
        c = year // 100
        year %= 100
        w = (c//4 - 2*c + year + year//4 + (13*(month+1)//5) + day - 1) % 7
        return week[w-1]


day = 3
month = 1
year = 2022

print(Solution().dayOfTheWeek(day, month, year))
