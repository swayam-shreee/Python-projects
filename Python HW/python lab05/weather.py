import json
import calendar

def read_data(*, filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def write_data(*, data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def max_temperature(*, data, date):
    temps = [reading['t'] for key, reading in data.items() if date in key]
    return max(temps) if temps else None

def min_temperature(*, data, date):
    temps = [reading['t'] for key, reading in data.items() if date in key]
    return min(temps) if temps else None

def max_humidity(*, data, date):
    hums = [reading['h'] for key, reading in data.items() if date in key]
    return max(hums) if hums else None

def min_humidity(*, data, date):
    hums = [reading['h'] for key, reading in data.items() if date in key]
    return min(hums) if hums else None

def tot_rain(*, data, date):
    rains = [reading['r'] for key, reading in data.items() if date in key]
    return sum(rains) if rains else 0

def report_daily(*, data, date):
    report = "========================= DAILY REPORT ========================\n"
    report += "Date                 Time     Temperature Humidity Rainfall\n"
    report += "==================== ======== =========== ======== ========\n"
    
    for key, reading in data.items():
        if date in key:
            date_part = key[:8]
            time_part = key[8:]
            date_str = f"{calendar.month_name[int(date_part[4:6])]} {int(date_part[6:]):02}, {date_part[:4]}"
            time_str = f"{time_part[:2]}:{time_part[2:4]}:{time_part[4:]}"
            report += f"{date_str:<20} {time_str} {reading['t']:>11} {reading['h']:>8} {reading['r']:>8.2f}\n"
    
    return report

def report_historical(*, data):
    report = "============================== HISTORICAL REPORT ===========================\n"
    report += "Date                 Minimum     Maximum     Minumum  Maximum  Total\n"
    report += "                     Temperature Temperature Humidity Humidity Rainfall\n"
    report += "==================== =========== =========== ======== ======== ========\n"
    
    dates = sorted(set(key[:8] for key in data.keys()))
    
    for date in dates:
        date_str = f"{calendar.month_name[int(date[4:6])]} {int(date[6:]):02}, {date[:4]}"
        min_temp = min_temperature(data=data, date=date)
        max_temp = max_temperature(data=data, date=date)
        min_hum = min_humidity(data=data, date=date)
        max_hum = max_humidity(data=data, date=date)
        total_rain = tot_rain(data=data, date=date)
        report += f"{date_str:<20} {min_temp:>10} {max_temp:>10} {min_hum:>8} {max_hum:>8} {total_rain:>8.2f}\n"
    
    return report

    