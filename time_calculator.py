def add_time(start, duration, day_of_week=None):
    list_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dict_days = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}

    time_plus = duration.split(":")
    hours_plus = int(time_plus[0])
    minutes_plus = int(time_plus[1])
    time_start = start.split(":")
    separ_min_from_am_pm = time_start[1].split(" ")
    begin_hours = int(time_start[0])
    begin_minutes = int(separ_min_from_am_pm[0])
    am_pm = separ_min_from_am_pm[1]
    shift_am_to_pm = {'AM':'PM', 'PM':'AM'}
    sum_of_days = int(hours_plus/24)
    finish_minutes = begin_minutes + minutes_plus

    if finish_minutes > 59:
      begin_hours += 1
      finish_minutes %= 60
    sum_of_shifts_am_pm = int((begin_hours + hours_plus) / 12)
    finish_hours = (begin_hours + hours_plus) % 12
    finish_minutes = finish_minutes if finish_minutes > 9 else '0' + str(finish_minutes)
    finish_hours = finish_hours = 12 if finish_hours == 0 else finish_hours

    if(am_pm == "PM" and begin_hours + (hours_plus%12)) >= 12: sum_of_days += 1
    am_pm = shift_am_to_pm[am_pm] if sum_of_shifts_am_pm % 2 == 1 else am_pm
    new_time = str(finish_hours) + ':' + str(finish_minutes) + ' ' + am_pm

    if(day_of_week):
      index = int((dict_days[day_of_week.lower()]) + sum_of_days) % 7
      new_day = list_days[index]
      new_time += ', ' + new_day
      
    if(sum_of_days==1):
      return new_time + ' ' + '(next day)'
    elif(sum_of_days>1):
      return new_time + ' (' + str(sum_of_days) + ' days later)'


    return new_time
