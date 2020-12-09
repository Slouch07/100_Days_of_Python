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
print("Welcome to the Morning Commute!.")
print("You live in the city, your mission...get to work on time.") 

transport_choice = input("Do you walk or bike?: \n").lower()
if transport_choice == 'bike':
  helmet_choice = input("You like your hair today. Do you wear your helmet? 'y' or 'n': \n").lower()
  if helmet_choice == 'y' or helmet_choice == 'n':
    stop_or_go = input("You come to an intersection with a yellow light. Do you 'stop' or 'go'?: \n").lower()
    if stop_or_go == 'go':
      path = input("You make it through safely. Do you take the 'shortcut' or the 'road'?: \n").lower()
      if path == 'road':
        print("You ride through construction and get a flat tire. You are late! Game over.")
      elif path == 'shortcut' and helmet_choice == 'y':
        print("A bird poops on your head. Good thing you wore a helmet. You arrive for work on time! You Win.")
      else:
        print("A bird poops on your head and now your hair is ruined. You go home to shower...you are late! Game over.")
    elif stop_or_go == 'stop' and helmet_choice == 'y':
      path = input("You are bumped by a driver and fall off your bike but your helmet saves you. Do you take a 'shortcut' or the 'road'?: \n").lower()
      if path == 'road':
        print("You ride through construction and get a flat tire. You are late! Game over.")
      elif path == 'shortcut':
        print("A bird poops on your head. Good thing you wore a helmet. You arrive for work on time! You win.") 
    else:
      print("You are bumped by a driver and fall off your bike. You have brain damage and will be late! Game over.")
else:
  print("You step off the curb and sprain your ankle...you are late! Game over.")


