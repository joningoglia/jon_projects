import datetime

d = datetime.datetime

# credit to https://gist.github.com/zhangsen/1199964 for this function
def get_age(date):
    '''Take a datetime and return its "age" as a string.
    The age can be in second, minute, hour, day, month or year. Only the
    biggest unit is considered, e.g. if it's 2 days and 3 hours, "2 days" will
    be returned.
    Make sure date is not in the future, or else it won't work.
    '''

    def formatn(n, s):
        '''Add "s" if it's plural'''

        if n == 1:
            return "1 %s" % s
        elif n > 1:
            return "%d %ss" % (n, s)

    def q_n_r(a, b):
        '''Return quotient and remaining'''

        return a / b, a % b

    class PrettyDelta:
        def __init__(self, dt):
            now = d.now()
            dt = d.fromtimestamp(dt)
            delta = dt - now
            self.day = delta.days
            self.second = delta.seconds

            self.year, self.day = q_n_r(self.day, 365)
            self.month, self.day = q_n_r(self.day, 30)
            self.hour, self.second = q_n_r(self.second, 3600)
            self.minute, self.second = q_n_r(self.second, 60)

        def format(self):
            for period in ['year', 'month', 'day', 'hour', 'minute', 'second']:
                n = getattr(self, period)
                if n > 0:
                    return formatn(n, period)
            return "0 second"

    return PrettyDelta(date).format()

today = input("Enter 1 for today or 0 for another date: ")

if (not today):
    tm = input("Enter time (HH:MM): ")

    date_string = d.today().strftime(f"%Y-%m-%d {tm}:00")
    date_obj = d.strptime(date_string, f"%Y-%m-%d %H:%M:%S")
    unix_time = int(d.timestamp(date_obj))
else:
    tm = input("Enter date/time (YYYY-MM-DD HH:MM:SS): ")

    date_string = d.today().strftime(f"{tm}")
    date_obj = d.strptime(date_string, f"%Y-%m-%d %H:%M:%S")
    unix_time = int(d.timestamp(date_obj))

print(f'\nDATE/TIME INPUT: {date_obj}')
print(f'UNIX TIMESTAMP: {unix_time}\n')
print(f'<t:{unix_time}:f>	{d.fromtimestamp(unix_time).strftime(f"%B %d, %Y %I:%M %p")}')
print(f'<t:{unix_time}:F>	{d.fromtimestamp(unix_time).strftime(f"%A, %B %d, %Y %I:%M %p")}')
print(f'<t:{unix_time}:d>	{d.fromtimestamp(unix_time).strftime(f"%m/%d/%Y")}')
print(f'<t:{unix_time}:D>	{d.fromtimestamp(unix_time).strftime(f"%B %d, %Y")}')
print(f'<t:{unix_time}:t>	{d.fromtimestamp(unix_time).strftime(f"%I:%M %p")}')
print(f'<t:{unix_time}:T>	{d.fromtimestamp(unix_time).strftime(f"%I:%M:%S %p")}')
print(f'<t:{unix_time}:R>	in {get_age(unix_time)}')

text = f'Join us <t:{unix_time}:R> (at <t:{unix_time}:t>) for...'

print(f"\n{text}")