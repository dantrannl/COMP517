
def memory_management():
  requests = []
  cache = []

  while True:
    page = input("Enter an integer or enter 0 to start, Q to quit: ")
    if page == "Q":
      exit()
    
    page = int(page)
    if page == 0:
      break
    else:
     requests.append(page)

  for page in requests:
    if page in cache:
      print("Hit")
    else: 
      print("Miss")
      if len(cache) >= 8: #Checking if cache memory is full
       cache.pop(0) #Evict the first element
      cache.append(page)
  
  return cache

while True:
  result = memory_management()
  print(result) #tells program to run memory management