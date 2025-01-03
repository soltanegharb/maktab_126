def event_schedular():
    """ This function is a simple event schedular that allows the user
      to add, delete, view and edit events """
    
    # using while loop to keep the program running
    # until the user decides to exit
    while True:
            action = input("action (add, delete, view, edit or exit): ")
            # exiting the program
            if action.lower() == "exit":
                break
            # adding an event
            elif action.lower() == "add":
                # using while loop to break in the middle of the loop
                # before executing the whole loop
                while True:
                    try:
                        # reading previous events
                        with open("events.txt", "r") as file:
                            lines = file.readlines()
                            event=[]
                            for line in lines:
                                event.append(line.strip().split("-SEP-"))
                    except Exception:
                        pass
                    # getting the event title
                    event_title = input("Enter event Title: ")
                    if event_title == "":
                        print("Title Can't Be Empty")
                        break
                    # checking if the event already exists
                    if len(event) != 0:
                        for i in range(len(event)):
                            if event_title in event[i]:
                                print("Event Already Exists")
                                # asking user if he/she wants to overwrite the event
                                action = input("if you want to overwrite the event Enter \"overwrite\" else \"no\": ")
                                # in case of overwriting the event
                                if action.lower() == "overwrite":
                                    # here we are deleting the repeated event
                                    event.pop(i)
                                    break
                                elif action.lower() == "no":
                                    break
                    # user decides not to add the event
                    if action.lower() == "no":
                        break
                    # its time to get the date and time
                    # getting the event date
                    while True:
                        try:
                             event_date = input("Enter event Date (yyyy-mm-dd): ")
                             test = event_date.split("-")
                             if len(test) != 3 or len(test[0]) !=4:
                                 print("Not Complete")
                                 raise ValueError
                             elif test[1] not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
                                 print("Not Correctly Written")
                                 raise ValueError
                             elif test[2] not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]:
                                 print("Not Correctly Written")
                                 raise ValueError
                             else:
                                  for item in test:
                                        if not item.isnumeric():
                                            print("Not Numeric")
                                            raise ValueError
                             break
                        except ValueError:
                            print("Please Enter Correct Date")
                    # getting the event time
                    while True:
                        try:
                             event_time = input("Enter event Time (hh:mm): ")
                             test = event_time.split(":")
                             if len(test) != 2:
                                 print("Not Complete")
                                 raise ValueError
                             elif len(test[0]) != 2 or len(test[1]) != 2:
                                 print("Not Correctly Written")
                                 raise ValueError
                             elif test[0] not in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]:
                                    print("Not Correctly Written")
                                    raise ValueError
                             elif test[1] not in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]:
                                    print("Not Correctly Written")
                                    raise ValueError
                             break
                        except:
                            print("Please Enter Correct Time")
                    # adding the event to the event list
                    event.append([event_title, event_date, event_time])
                    # writing the events to the file
                    with open("events.txt", "w") as file:
                        for i in range(len(event)):
                            file.write(f"{event[i][0]}-SEP-{event[i][1]}-SEP-{event[i][2]}\n")
                    break
            # deleting an event
            elif action.lower() == "delete":
                # using while loop to break in the middle of the loop
                # before executing the whole loop
                while True:
                    try:
                        with open("events.txt", "r") as file:
                            lines = file.readlines()
                    except Exception:
                        print("No Events added yet")
                        break
                    # deleting the event
                    with open("events.txt", "w") as file:
                        event_title = input("Enter event Title to delete: ")
                        for line in lines:
                            event = line.strip().split("-SEP-")
                            if event_title in event:
                                print("Event Deleted")
                            if event_title not in event:
                                file.write(line)
                    # undoing the delete
                    action = input("if you want to undo the delete Enter \"undo\" else \"no\": ")
                    if action.lower() == "undo":
                        with open("events.txt", "w") as file:
                            for line in lines:
                                file.write(line)
                        print("Event Restored")
                    break
            # viewing the events
            elif action.lower() == "view":
                action = input("sort by events' \"title\", \"date\" or \"time\" \n or by a special event, type it\'s name: ")
                try:
                    with open("events.txt", "x") as file:
                        pass
                except FileExistsError:
                    pass
                with open("events.txt", "r") as file:
                    while True:
                        lines = file.readlines()
                        # making a list of the events
                        event = []
                        try:
                            for line in lines:
                                # using -SEP- to separate the title, date and time
                                # using strip to remove the spaces and \n
                                event.append(line.strip().split("-SEP-"))
                        except Exception:
                            print("No Events")
                            break
                        # sorting the events by title
                        if action.lower() == "title":
                            # making a dictionary to sort the events by title
                            events = dict()
                            for i in range(len(event)):
                                events[event[i][0]] = event[i]
                            # printing the events sorted by title
                            print()
                            for i in sorted(events.keys()):
                                print(f"title: {i}, date: {events[i][1]}, time: {events[i][2]}")
                        # sorting the events by date
                        elif action.lower() == "date":
                            events = []
                            for i in range(len(event)):
                                events.append((event[i][1], event[i]))
                            # Sorting the events by date
                            # using key to sort the events by date
                            # using lambda to sort the events by the first item in the tuple
                            sorted_events = sorted(events, key=lambda x: x[0])
                            # Printing the sorted events
                            print()
                            for date, ev in sorted_events:
                                print(f"title: {ev[0]}, date: {date}, time: {ev[2]}")
                        # sorting the events by time
                        elif action.lower() == "time":
                            events = []
                            for i in range(len(event)):
                                events.append((event[i][2], event[i]))
                            # Sorting the events by time
                            # using key to sort the events by time
                            # using lambda to sort the events by the first item in the tuple
                            sorted_events = sorted(events, key=lambda x: x[0])
                            # printing the events sorted by time
                            print()
                            for time, ev in sorted_events:
                                print(f"title: {ev[0]}, date: {ev[1]}, time: {time}")
                        else:
                            # printing the event by its name
                            for i in range(len(event)):
                                if action.lower() == event[i][0].lower():
                                    print(f"\ntitle: {event[i][0]}, date: {event[i][1]}, time: {event[i][2]}")
                                    checker = True
                            if not checker:
                                print("Event Not Found")
                        break
            # editing an event
            elif action.lower() == "edit":
                event_to_edit = input("Enter the event title to edit: ")
                # checking if the events.txt file exists
                try:
                    with open("events.txt", "x") as file:
                        print("No Events")
                except FileExistsError:
                    pass
                with open("events.txt", "r") as file:
                    lines = file.readlines()
                with open("events.txt", "w") as file:
                    event = []
                    # using while loop if somewhere in the middle of this loop we want to break
                    while True:
                        try:
                            for line in lines:
                                # using -SEP- to separate the title, date and time
                                # using strip to remove the spaces and \n
                                event.append(line.strip().split("-SEP-"))
                        except:
                            # if the file is empty
                            print("No Events")
                            break
                        if event_to_edit in event:
                            action = input("Enter what you want to edit (title, date or time): ")
                            # if wanted to change title
                            if action.lower() == "title":
                                new_title = input("Enter the new title: ")
                                # changing title 
                                for i in range(len(event)):
                                    if event[i][0] == event_to_edit:
                                        event[i][0] = new_title
                                        checker = True
                                    if checker:
                                        print("event title edited")
                            # if wanted to change date
                            elif action.lower() == "date":
                                while True:
                                    try:
                                         new_date = input("Enter the new date: ")
                                         test = new_date.split("-")
                                         if len(test) != 3 or len(test[0]) != 4:
                                             print("Not Complete")
                                             raise ValueError
                                         elif test[1] not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
                                             print("Not Correctly Written")
                                             raise ValueError
                                         elif test[2] not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]:
                                             print("Not Correctly Written")
                                             raise ValueError
                                         else:
                                              for item in test:
                                                    if not item.isnumeric():
                                                        print("Not Numeric")
                                                        raise ValueError
                                         break
                                    except:
                                        print("Please Enter Correct Date")
                                # changing date
                                for i in range(len(event)):
                                    if event[i][0] == event_to_edit:
                                        event[i][1] = new_date
                                        checker = True
                                    if checker:
                                        print("event date edited")
                            # if wanted to change time
                            elif action.lower() == "time":
                                while True:
                                    try:
                                         new_time = input("Enter the new time: ")
                                         test = new_time.split(":")
                                         if len(test) != 2:
                                             print("Not Complete")
                                             raise ValueError
                                         elif test[0] not in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]:
                                             print("Not Correctly Written")
                                             raise ValueError
                                         elif test[1] not in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]:
                                             print("Not Correctly Written")
                                             raise ValueError
                                         break
                                    except:
                                        print("Please Enter Correct Time")
                                # changing time
                                for i in range(len(event)):
                                    if event[i][0] == event_to_edit:
                                        event[i][2] = new_time
                                        checker = True
                                    if checker:
                                        print("event time edited")
                                    
                            break
                        else:
                            print("Event Not Found")
                            break

event_schedular()