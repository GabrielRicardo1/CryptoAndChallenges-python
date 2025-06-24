def add_time(start, duration, day=None):
    start_parts = start.split()
    start_hour, start_minute = start_parts[0].split(':')
    period = start_parts[1]
    start_hour = int(start_hour)
    start_minute = int(start_minute)

    duration_hour, duration_minute = duration.split(':')
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)

    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hours
    days_passed = total_hours // 24
    final_24h = total_hours % 24

    if final_24h == 0:
        final_hour = 12
        final_period = 'AM'
    elif final_24h < 12:
        final_hour = final_24h
        final_period = 'AM'
    elif final_24h == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = final_24h - 12
        final_period = 'PM'

    final_minutes_str = f"{final_minutes:02d}"
    new_time = f"{final_hour}:{final_minutes_str} {final_period}"

    if day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
