# Takes a time from later today from user input and generates timestamps for Discord

import datetime

d = datetime.datetime
tm = input("Enter time (hh:mm):") # No validation (yet)

date_string = d.today().strftime(f"%Y-%m-%d {tm}:00")
date_obj = d.strptime(date_string, f"%Y-%m-%d %H:%M:%S")
unix_time = int(str(d.timestamp(date_obj)).replace('.0', ''))

print(f'\nDATE/TIME INPUT: {date_obj}')
print(f'UNIX TIMESTAMP: {unix_time}\n')
print(f'<t:{unix_time}:f>	{d.fromtimestamp(unix_time).strftime(f"%B %d, %Y %I:%M %p")}')
print(f'<t:{unix_time}:F>	{d.fromtimestamp(unix_time).strftime(f"%A, %B %d, %Y %I:%M %p")}')
print(f'<t:{unix_time}:d>	{d.fromtimestamp(unix_time).strftime(f"%m/%d/%Y")}')
print(f'<t:{unix_time}:D>	{d.fromtimestamp(unix_time).strftime(f"%B %d, %Y")}')
print(f'<t:{unix_time}:t>	{d.fromtimestamp(unix_time).strftime(f"%I:%M %p")}')
print(f'<t:{unix_time}:T>	{d.fromtimestamp(unix_time).strftime(f"%I:%M:%S %p")}')
print(f'<t:{unix_time}:R>	{d.fromtimestamp(unix_time).strftime(f"(relative time)")}')

text = f'Join us <t:{unix_time}:R> (at <t:{unix_time}:t>) for...'

print(f"\n{text}")