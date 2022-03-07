def add_time(curr_hour, time_lapse, *day):
    ##### Parameters parsing #####
    strt_hour = int(curr_hour.split(' ')[0].split(':')[0])
    strt_min = int(curr_hour.split(' ')[0].split(':')[1])
    end_hour = int(time_lapse.split(':')[0]) 
    end_min =  int(time_lapse.split(':')[1])
    frmt = curr_hour.split(' ')[1] # AM, PM
    strt_day = day[0].capitalize() if len(day) > 0 else None
    ##### End of parameters parsing #####

    total_days = 0

    total_hours = strt_hour + end_hour
    total_mins = strt_min + end_min
    
    #### Minutes calculus ####
    if total_mins > 60:
        total_hours += 1
        total_mins -= 60
    #### End of minutes calculus #####

    #### Hour & format ('AM', 'PM') calculus #####
    while total_hours >= 12:
        total_hours -= 12
        if frmt == 'AM':
            frmt = 'PM'
            continue

        if frmt == 'PM':
            frmt = 'AM'
            total_days += 1
            continue
    
    if total_hours == 0:
        total_hours = 12
    ##### End of hour & format calculus
    
    ##### Day to display calculus #####
    finish_day = day_to_display(total_days, strt_day) if strt_day else None
    ##### End of day to display calculus #####

    my_str = ""

    ##### Final string formatter #####
    if total_days < 1:
        my_str += (f"{total_hours}:{total_mins if total_mins >= 10 else '0' + str(total_mins)} {frmt}{', ' + finish_day if finish_day else ''}")
    elif total_days == 1:
        my_str += (f"{total_hours}:{total_mins if total_mins >= 10 else '0' + str(total_mins)} {frmt}{', '  + finish_day if finish_day else ''} (next day)")
    elif total_days > 1:
        my_str += (f"{total_hours}:{total_mins if total_mins >= 10 else '0' + str(total_mins)} {frmt}{', ' + finish_day if finish_day else ''} ({total_days} days later)")
    ##### End of final string formatter #####
    
    return my_str


def day_to_display(days, *day_given):
    day_given = day_given[0] # Take the first parameter
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if days % 7 == 0:
        # Return the same day because seven days exactly ends in the same day
        return day_given

    while week_days.index(day_given) != 0:
        # Index day's swapping
        aux_day = week_days[0]
        week_days.remove(aux_day)
        week_days.append(aux_day)
    
    while days > 7:
        # Substract 7 to avoid an IndexError exception
        days -= 7

    day = week_days[week_days.index(day_given) + days]

    return day


# tests
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))


    