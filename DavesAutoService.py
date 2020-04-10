print('Welcome To Davy\'s auto shop\n')
service_list = {
    'Oil change' : 35,
    'Tire rotation' : 19,
    'Car wash' : 7,
    'Car wax' : 12
    }
print('Here is a list of all of our services: \n')
for item in service_list:
    print(item)
service_1 = input('Select first service: ')
service_2 = input('Select second service: ')
if service_1 == '-':
    int(x = 0) and str(service_1 = 'No service')
if service_2 == '-':
    int(y = 0) and str(service_2 = 'No service')    
print('Davy\'s auto shop services')
x = service_list.get(service_1)
y = service_list.get(service_2)
print ('Service 1: ' + service_1 + ', ' + '$' + str(x))
print ('Service 2: ' + service_2 + ', ' + '$' + str(y))
print('Total: $' + int((int(x)+ int(y))))
