from datetime import datetime
import time

class Session:
    
    def __init__(self, days, start_time, end_time, start_date, end_date):
        self.days = days
        self.start_datetime = datetime.strptime(start_time, '%I:%M%p')
        self.end_datetime = datetime.strptime(end_time, '%I:%M%p')
        self.start_time = time.strptime(start_time, '%I:%M%p')
        self.end_time = time.strptime(end_time, '%I:%M%p')         
        self.session_length = self.end_datetime - self.start_datetime

    def does_session_overlap(self, other):
        for day in self.days:
            if day in other.days:
                if self.end_time >= other.start_time and self.start_time <= other.end_time:
                    return True
        return False
    
    def __str__(self):
        return self.days + ' ' + time.strftime('%I:%M%p', self.start_time) + ' ' + time.strftime('%I:%M%p', self.end_time)
    
    def __lt__(self, other):
        return self.session_length < other.session_length