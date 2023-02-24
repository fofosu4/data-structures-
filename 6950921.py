#list of cars available at jnr`s ltd.
cars={'benz c200':100,'benz c250':150,'benz c300':200,'benz c350':250, \
      'benz c400':300,'benz c450':350,'benz c500':400,'benz c550':450, \
       'benz c600':500,'toyota x':550,'toyota s':600,'toyota ce':650, \
        'toyota y':700,'bugatti a':750,'bugatti b':800,'bugatti c':850, \
       'bugatti d':900,'bugatti e':950,'bugatti f':1000, \
       'ford a':1500,'ford b':2000,'ford c':2500,'ford d':3000, \
        'bmw a':3500,'bmw b':4000,'bmw c':4500,'bmw d':5000, \
        'rolls royce a':5500,'rolls royce b':6000,'rolls royce c':6500, \
         'rolls royce d':7000,'rolls royce e':7500,'rolls royce f':8000, \
        'range rover a':8500,'range rover b':9000,'range rover c':9500, \
        'range rover d':10000, 'range rover e':15000, 'range rover f':20000,'ferrari a':25000, \
                'ferrari b':30000,'ferrari c':35000,'ferrari d':40000,'ferrari e':45000, \
                    'g wagon a':50000, 'g wagon b':55000, 'g wagon c':60000, 'g wagon d':65000, \
                        'honda a':70000,'honda b':75000,'honda c':80000,'honda d':85000,}
#get user input for car name
car_name=input('enter a car_name')
#check if car name is in the list of available cars
if car_name in  cars:
    print('yes')
    #if car_name is present,get its price
    car_price=cars[car_name]
    print('the price of {car_name} is ${car_price}.')
else:
    #if car name is not present,inform customer
    print('sorry,{car_name} is not available')
#github.com/fofosu4

    
    
    
    
    
    
   
