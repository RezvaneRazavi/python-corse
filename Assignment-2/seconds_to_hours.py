seconds = int(input('enter seconds: '))

hour = seconds // 3600
temp = seconds % 3600
minutes = temp // 60
second = temp % 60 

if hour < 10:
    hour = '0' + str(hour)
if minutes < 10:
    minutes = '0' + str(minutes)
if second < 10:
    second = '0' + str(second)


print(hour, ':', minutes, ':', second)