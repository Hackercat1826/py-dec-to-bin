while True:
  # Decimal work
  decimal_request = input(">> ") 
  decimal_request = int(decimal_request) 
  
  # Binary work
  binary_value = bin(decimal_request)
  
  # Printing the binary value
  print(binary_value[2:])
