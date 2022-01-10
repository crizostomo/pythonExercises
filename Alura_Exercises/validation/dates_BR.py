from datetime import datetime, timedelta

class DatesBR:
    def __init__(self):
        self.record_moment = datetime.today()

    def __str__(self):
        return self.format_date()

    def record_month(self):
        months_year = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
            "Nov", "Dec"
        ]
        month = self.record_moment.month - 1
        return months_year[month]

    def day_week(self):
        day_of_the_week = [
            "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
        ]
        day_week = self.record_moment.weekday()
        return day_of_the_week[day_week]

    def format_date(self):
        date_ok = self.record_moment.strftime("%d/%m/%Y %H:%M:%S")
        return date_ok

    def record_time(self):
        record_time_ok = (datetime.today() + timedelta(days=30)) - self.record_moment
        return record_time_ok

