# A choose your own adventure program in python.
print('''
                      |
                     _=_
                     \ /.           _=
        .-.    _ .-_ |  |_         |  |
 "   _  | |   | ||  \|    |_.--.   |  |
 |  | |_| |-__| ||          |  |,-.|  |-_   __
| |-|   '                          |     | |  |
                                         |_|  |
''')

print("Welcome to the Morning Commute!")
print("You live in the city, your mission...get to work on time.") 

transport_choice = input("Do you walk or bike?: ").lower()
if transport_choice == 'bike':
  helmet_choice = input("You like your hair today. Do you wear your helmet? 'y' or 'n': ").lower()
  if helmet_choice == 'y' or helmet_choice == 'n':
    stop_or_go = input("You come to an intersection with a yellow light. Do you 'stop' or 'go'?: ").lower()
    if stop_or_go == 'go':
      path = input("You make it through safely. Do you take the 'shortcut' or 'road'?: ").lower()
      if path == 'road':
        print("You ride through construction and get a flat tire. You are late for work!")
      elif path == 'shortcut' and helmet_choice == 'y':
        print("A bird poops on your head. Good thing you wore a helmet on. You arrive for work on time!")
      else:
        print("A bird poops on your head and now your hair is ruined. You go home to shower...you are late for work!")
    elif stop_or_go == 'stop' and helmet_choice == 'y':
      path = input("You are bumped by a driver and fall off your bike but your helmet saves you. Do you take a 'shortcut' or the 'road'?: ").lower()
      if path == 'road':
        print("You ride through construction and get a flat tire. You are late for work!")
      elif path == 'shortcut':
        print("A bird poops on your head. Good thing you had a helmet on. You arrive for work on time!") 
    else:
      print("You are bumped by a driver and fall off your bike. You have brain damage and will be late for work!")
else:
  print("You step off the curb and sprain your ankle...you are late for work!")