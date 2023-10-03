import datetime
d = datetime.datetime

def get_input():
    today = input("Enter 1 for today or 2 for another date: ")

    if (int(today) == 1):
        tm = input("Enter time (HH:MM): ")
        date_string = d.today().strftime(f"%Y-%m-%d {tm}:00")
        date_obj = d.strptime(date_string, f"%Y-%m-%d %H:%M:%S")
        unix_time = int(d.timestamp(date_obj))
        return unix_time, date_obj
    elif (int(today) != 1):
        tm = input("Enter date/time (YYYY-MM-DD HH:MM:SS): ")
        date_string = d.today().strftime(f"{tm}")
        date_obj = d.strptime(date_string, f"%Y-%m-%d %H:%M:%S")
        unix_time = int(d.timestamp(date_obj))
        return unix_time, date_obj

unix_time, date_obj = get_input()
print(f'\nDATE/TIME INPUT: {date_obj}')
print(f'UNIX TIMESTAMP: {unix_time}\n')
print(f'<t:{unix_time}:f>	{d.fromtimestamp(unix_time).strftime(f"%B %d, %Y %I:%M %p")}')
print(f'<t:{unix_time}:F>	{d.fromtimestamp(unix_time).strftime(f"%A, %B %d, %Y %I:%M %p")}')
print(f'<t:{unix_time}:d>	{d.fromtimestamp(unix_time).strftime(f"%m/%d/%Y")}')
print(f'<t:{unix_time}:D>	{d.fromtimestamp(unix_time).strftime(f"%B %d, %Y")}')
print(f'<t:{unix_time}:t>	{d.fromtimestamp(unix_time).strftime(f"%I:%M %p")}')
print(f'<t:{unix_time}:T>	{d.fromtimestamp(unix_time).strftime(f"%I:%M:%S %p")}')
print(f'<t:{unix_time}:R>	(relative time)')

text = f'Join us <t:{unix_time}:R> (at <t:{unix_time}:t>) for...'

print(f"\n{text}")