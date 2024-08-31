"""Alarm clock"""

import datetime as dt

print(dt.datetime.now().strftime("%H:%M:%S"))


# TODO: User time input
def set_alarm():
    while True:
        time = input("Enter time in 24 hours format (hh:mm): ")
        if ":" in time:
            split_time = time.split(":")
            if len(split_time) == 2:
                if not split_time[0].isdigit() or not split_time[1].isdigit():
                    print("Invalid time format. Please try again.")
                    continue

                hours = int(split_time[0])
                minutes = int(split_time[1])
                if hours < 24 and minutes < 60:
                    if len(split_time[0]) == 1:
                        split_time[0] = "0" + split_time[0]
                    if len(split_time[1]) == 1:
                        split_time[1] = "0" + split_time[1]
                    time = ":".join(split_time)
                    print("Alarm set for", time)

                    return time
                else:
                    print("Invalid time format. Please try again.")
                    continue
            else:
                print("Invalid time format. Please try again.")
                continue
        else:
            print("Invalid time format. Please try again.")
            continue


user_time = set_alarm()
now = dt.datetime.now().strftime("%H:%M")


# comparing the actual time to the user set time
while user_time != now:
    now = dt.datetime.now().strftime("%H:%M")
    # print actual time with seconds
    print(dt.datetime.now().strftime("%H:%M:%S"))

print("Wake up!")
