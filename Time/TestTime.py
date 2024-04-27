from time import gmtime, strftime
print(strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
print(strftime("Date: %b %d, %Y. Time: %H:%M", gmtime()))
print(strftime("Date: %b %d, %Y. Time: %I:%M%p", gmtime()))
time_date = strftime("Date: %b %d, %Y. Time: %I:%M%p", gmtime())
print(time_date)