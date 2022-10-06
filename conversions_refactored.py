# Temperature Conversion
# Define a function for conversion

def temp_conversion(temp,current_unit,to_be_convered):
    # temp is the value of temperature and to_be_convered is conversion scale
    
    ### Conversion from Celcius to Fahrenhite ###
    if to_be_convered == "F" and current_unit == "C":
        new_temp = round(9 / 5 * temp + 32, 3)
        print("The converted temperature in Fahrenhite scale is " + str(new_temp) + " degrees")
        
    ### Conversion from Fahrenhite into Celcius ###    
    elif to_be_convered == "C" and current_unit == "F":
        new_temp = round(5 / 9 * (temp - 32), 3)
        print("The converted temperature in Celcius scale is " + str(new_temp) + " degrees")
        
    ### Conversion from Celcius to Kelvin ###    
    elif to_be_convered == "K" and current_unit == "C":
        new_temp = round(temp + 273.15, 3)
        print("The converted temperature in Kelvin scale is " + str(new_temp) + " degrees")
        
    ### Conversion from Kelvin to Celcius ###    
    elif to_be_convered == "C" and current_unit == "K":
        new_temp = round(temp - 273.15, 3)
        print("The converted temperature in Celcius scale is " + str(new_temp) + " degrees")
        
    ### Conversion from Kelvin to Fahrenhite ###    
    elif to_be_convered == "F" and current_unit == "K":
        new_temp = round(9 / 5 * (temp - 273.15) + 32, 3)
        print("The converted temperature in Fahrenhite scale is " + str(new_temp) + " degrees")
    elif to_be_convered == "K" and current_unit == "F":
        new_temp = round(5 / 9 * (temp - 32) + 273.15, 3)
        print("The converted temperature in Kelvin scale is " + str(new_temp) + " degrees")
        
    ### Conversion from Fahrenhite to Kelvin ###    
    else:
        print("The converted temperature in same scale is " + str(temp) + " degrees")
while 1 :
    f = input('enter fromUnit like capital K for Kelvin: ')
    t = input('enter toUnit like capital C for Celcius: ')
    v = input('enter value like 1: ')

    temp_conversion(float(v),f,t)

