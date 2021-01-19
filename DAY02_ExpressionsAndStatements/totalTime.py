start_time_hr = 6 + 52 / 60.0
easy_pace_hr = (8 + 15 / 60.0 ) / 60.0
tempo_pace_hr = (7 + 12 / 60.0) / 60.0
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
breakfast_sec= (breakfast_min-int(breakfast_min))*60
print(int(breakfast_hr),":",int(breakfast_min),":",int(breakfast_sec))

