#Forecast checker - checks the previous days forecast against the observed data for that day, you will
#need to run for several days to get enough data that matches up to be compaired.
#NOTE: low temp forecast is only for then 'evening' IE after 12pm and before 12 am, not the overall low.
import datetime, calendar, requests, bs4
date_time = str(datetime.datetime.now())
#url for previously recorded temps
url_p = 'https://w1.weather.gov/data/obhistory/KGAI.html'
#url for future forecast temps
url_f = 'https://forecast.weather.gov/MapClick.php?lat=39.08196000000004&lon=-77.15117999999995'
#getting past H/L temperature readings and saving them to a file
p = requests.get(url_p)
soup = bs4.BeautifulSoup(p.text, 'html.parser')
text = soup.get_text()
#cutting out header and footer info.
header_removed = text[text.find('Min.')+4:]
footer_removed = header_removed[:header_removed.find('DateTime')]
split = footer_removed.split(':')
#getting each line as a correct single entry
table = []
for i in range(len(split)-1):
    table.append(split[i][-4:]+split[i+1][:-4])
#getting a list of values in form DDTIMETT where DD is the day, TIME is time of obs and TT is the temp
temp_find_table = []
codes = ['NDC','CLR','FEW','SCT','BKN','OVC']
for entry in range(len(table)):
    end_pos = table[entry].find('\n')
    for c in range(len(codes)):
        if codes[c] in table[entry]:
            temp_find_table.append(table[entry][table[entry].find(codes[c]):end_pos])
#removing leading cloud cover code if entry has two of the same codes repeated
for it in range(len(temp_find_table)):
    for suf in range(len(codes)):
        if temp_find_table[it].count(codes[suf]) == 2:
            temp_find_table[it] = temp_find_table[it][temp_find_table[it].find(' ')+1:]
temp_find_table_nospace = []
for spaces in range(len(temp_find_table)):
    if ' ' not in temp_find_table[spaces]:
       temp_find_table_nospace.append(temp_find_table[spaces])
#removing cloud cover codes depending on length (codes indicating cover list octas (3 digits))
for u in range(len(temp_find_table_nospace)):
    if 'CLR' in temp_find_table_nospace[u]:
        temp_find_table_nospace[u] = temp_find_table_nospace[u][3:]
    if 'NDC' in temp_find_table_nospace[u]:
        temp_find_table_nospace[u] = temp_find_table_nospace[u][3:]
    if 'OVC' in temp_find_table_nospace[u]:
        temp_find_table_nospace[u] = temp_find_table_nospace[u][6:]
    if 'BKN' in temp_find_table_nospace[u]:
        temp_find_table_nospace[u] = temp_find_table_nospace[u][6:]
    if 'FEW' in temp_find_table_nospace[u]:
        temp_find_table_nospace[u] = temp_find_table_nospace[u][6:]
    if 'SCT' in temp_find_table_nospace[u]:
        temp_find_table_nospace[u] = temp_find_table_nospace[u][6:]
just_temp = []
for tds in range(len(temp_find_table_nospace)):
    if len(temp_find_table_nospace[tds]) == 2:
        just_temp.append(temp_find_table_nospace[tds][:1])
    if len(temp_find_table_nospace[tds]) == 3:
        just_temp.append(temp_find_table_nospace[tds][:2])        
    if len(temp_find_table_nospace[tds]) == 4:
        just_temp.append(temp_find_table_nospace[tds][:2])
    if len(temp_find_table_nospace[tds]) >= 5:
        just_temp.append(temp_find_table_nospace[tds][:3])
date_temp = []
for j in range(len(table)):
    date_temp.append(table[j][:6] + just_temp[j])
#getting a list of yesterdays date_temps (this will always be a full day)
yesterday = str(datetime.datetime.now() - datetime.timedelta(1))
yesterday_date_temp = []
for k in range(len(date_temp)):
    if int(date_temp[k][:2]) == int(yesterday[8:10]):
        yesterday_date_temp.append(date_temp[k])
#finding the high and low temp
all_temps = []
for t in range(len(yesterday_date_temp)):
    if yesterday_date_temp[t][6:9] =='NA':
        all_temps.append(yesterday_date_temp[t][6:9])
    else:
        all_temps.append(int(yesterday_date_temp[t][6:9]))
while 'NA' in all_temps:
    all_temps.remove('NA')
high = str(max(all_temps))
night_temps = []
for l in range(len(yesterday_date_temp)):
    if int(yesterday_date_temp[l][2:4]) > 11:
        if yesterday_date_temp[l][6:9] == 'NA':
            night_temps.append(yesterday_date_temp[l][6:9])
        else:
            night_temps.append(int(yesterday_date_temp[l][6:9]))
while 'NA' in night_temps:
    night_temps.remove('NA')
low = str(min(night_temps))
#checking to see if this data has already been aquired
check_temps_for_dup = open('C://py//weatherData//past.txt', 'r')
check_temps_dup_list = check_temps_for_dup.readlines()
check_temps_for_dup.close()
#saving the recorded temperatures to the file
if int(check_temps_dup_list[-1][8:10]) != int(yesterday[8:10]):
    save_past = open('C://py//weatherData//past.txt', 'a')
    save_past.write(yesterday[:10] + ': ' + high + ' ' + low + '\n')
    save_past.close()
#getting forecast H/L temperatures and saving them to a file.
f = requests.get(url_f)
future_soup = bs4.BeautifulSoup(f.text, 'html.parser')
future_text = future_soup.get_text()
#cutting out the part we want
start_just_ext = future_text.find('Extended Forecast for')
end_just_ext = future_text.find('Detailed Forecast')
just_ext = future_text[start_just_ext:end_just_ext]
#finding the correct days (tomorrow)
day_finder = calendar.weekday(int(date_time[0:4]),int(date_time[5:7]),int(date_time[8:10]))
if day_finder < 6:
    forecast_day = calendar.day_name[day_finder + 1]
elif day_finder == 6:
    forecast_day = calendar.day_name[0]
if day_finder < 5:
    forecast_end = calendar.day_name[day_finder + 2]
elif day_finder == 5:
    forecast_end = calendar.day_name[0]
elif day_finder == 6:
    forecast_end = calendar.day_name[1]
#getting tomorrow's forecast
full_forecast_day = just_ext[just_ext.find(forecast_day):just_ext.find(forecast_end)]
#getting the forecast temperatures
forecast_high = full_forecast_day[full_forecast_day.find('High: ')+6:full_forecast_day.find('High: ')+8]
forecast_low = full_forecast_day[full_forecast_day.find('Low: ')+5:full_forecast_day.find('Low: ')+7]
#getting the date of tomorrows forecast
future_date = str(datetime.date.today() + datetime.timedelta(days=1))
#checking to see if this data has already been aquired
check_future_dup = open('C://py//weatherData//future.txt', 'r')
check_future_list = check_future_dup.readlines()
check_future_dup.close()
#saving the forecast to a file
if check_future_list[-1][8:10] != future_date[8:10]:
    save_future = open('C://py//weatherData//future.txt', 'a')
    save_future.write(future_date + ': ' + forecast_high +' '+ forecast_low + '\n')
    save_future.close()
#result of comparison
file1 = open('C://py//weatherData//past.txt', 'r')
past_data = file1.readlines()
file1.close()
file2 = open('C://py//weatherData//future.txt', 'r')
future_data = file2.readlines()
file2.close()
numForecasts = 0
sumHighError = 0
sumLowError = 0
for observation in range(len(past_data)):
    for forecast in range(len(future_data)):
        if past_data[observation][:10] == future_data[forecast][:10]:
            obs_high = int(past_data[observation][12:14])
            for_high = int(future_data[forecast][12:14])
            obs_low = int(past_data[observation][15:17])
            for_low = int(future_data[forecast][15:17])
            high_error = abs(round((obs_high - for_high)/obs_high * 100, 2))
            low_error = abs(round((obs_low - for_low)/obs_low * 100, 2))
            numForecasts += 1
            sumHighError += high_error
            sumLowError += low_error
            print(f'{future_data[forecast][:10]}: Forecast high: {for_high}°F Observed high: {obs_high}°F', end = '')
            print(f' Forecast low: {for_low}°F Observed low: {obs_low}°F')
            print(f'This is a high temp forecast error of {high_error}%', end='')
            print(f' and a low temp forecast error of {low_error}%\n')
print(f'This is a cumulative high forecast error of {round(sumHighError / numForecasts, 2)}% ', end = '')
print(f'and a cumulative low forecast error of {round(sumLowError / numForecasts, 2)}%')
