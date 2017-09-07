# the BEST way to deal with times is to convert them to UTC as soon as you receive them
# and only convert them back to local time when you display them to the end user
import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print('Naive local time {}'.format(local_time))
print('Naive UTC time {}'.format(utc_time))

aware_local_time = pytz.utc.localize(local_time).astimezone()  # localize uses naive time, so use .astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print('Aware local time {}, time zone {} '.format(aware_local_time, aware_local_time.tzinfo))
print('Aware UTC time {}, time zone {} '.format(aware_utc_time, aware_utc_time.tzinfo))

# working in UTC time to prevent issues with time zones
gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

s = 1445754600
t = s + (60 * 60)

tz = pytz.timezone('America/Chicago')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(tz)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(tz)

print('{} seconds since the epoch is {}'.format(s, dt1))
print('{} seconds since the epoch is {}'.format(t, dt2))
