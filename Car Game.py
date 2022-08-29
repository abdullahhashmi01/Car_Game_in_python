command = ""
started = False
while command != "quit":
   command = input(">").lower()
   if command  == "start":
       if started:
           print("car is already started, what are you doing....")
       else:
           started = True
           print("car started...")
   elif command == "stop":
       if not started:
           print("car is already stopped")
       else:
           started = False
           print("car stopped..")
   elif command == "help":
       print("""
       start - to start the car
       stop - to stop the car
       quit - to quit
       """)
   else:
       print("sorry, I don't understand that!")
