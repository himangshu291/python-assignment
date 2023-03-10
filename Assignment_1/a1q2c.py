print("convert temperature into centigrade degrees")
Fahrenheit = float( input("Temperature value in degree Fahrenheit: " ))  
  
# For Converting the temperature from degree Fahrenheit to degree Celsius   
# by using the above given formula  
celsius = (Fahrenheit - 32) / 1.8  
    
# Print the result  
print ('The %.2f degree Fahrenheit is equal to: %.2f Celsius'  
      %(Fahrenheit, celsius))  
  
print("----OR----")  
Fahrenheit = float( input("Temperature value in degree Fahrenheit: " ))  
celsius = (Fahrenheit - 32) * 5/9
    
# Print the result  
print ('The %.2f degree Fahrenheit is equal to: %.2f Celsius'  
      %(Fahrenheit, celsius)) 