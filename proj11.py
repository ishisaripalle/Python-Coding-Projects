###########################################################
#  Computer Project #11
#  Algorithm
#    prompt for a choice
#    input a valid choice
#    loop while not in choice for error checking 
#       if choice is a 
#       if choice is d
#       if choice is l
#       if choice is q
#    break out of while loop and end program 
###########################################################
from p11_calendar import P11_Calendar
from p11_event import P11_Event

CAL_TYPE = ['meeting','event','appointment','other']

MENU = '''Welcome to your own personal calender.
  Available options:
    (A)dd an event to calender
    (D)elete an event
    (L)ist the events of a particular date
    (Q)uit'''

def check_time(time,duration):
    ''' function checks time
        
        the function utilizes the try and except used
        for time in the event class but returns False instead of None
        and if the start time is greater than 360 and end time is less 
        than 1020 then True is returned and if not False is returned
        
        Parameters: time, duration 
        
        Returns: False or True '''
    new_time = time.split(":")
    if len(new_time) == 2 and type(duration) == int and duration > 0: 
        if new_time[0].isdigit() == True and new_time[1].isdigit() == True: 
            if 0 <= int(new_time[0]) <= 23:
                if 0 <= int(new_time[1]) <= 59:
                        pass
                else: 
                    return False 
            else: 
                return False 
        else: 
            return False  
    else: 
        return False 
    if (int(new_time[0]) * 60 + int(new_time[1])) >= 360:
        if ((int(new_time[0]) * 60 + int(new_time[1])) + duration) <= 1020:
            return True 
        else: 
            return False 
    else: 
        return False 
                      
def event_prompt():
    ''' function has four prompts that the user must input and then the 
        function uses them as parameters to initilize event and if event is
        valid the event is returned and if not the event is invalid'''
    date = input("Enter a date (mm/dd/yyyy): ")
    time = input("Enter a start time (hh:mm): ")
    duration = int(input("Enter the duration in minutes (int): "))
    cal_type = input("Enter event type ['meeting','event','appointment','other']: " ).lower()
    event = P11_Event(date, time, duration, cal_type)
    if event.valid == True and check_time(time, duration) == True:
        return event 
    else: 
        print("Invalid event. Please try again.")
                
def main():
    calendar = P11_Calendar()
    while True: 
        print(MENU)
        choices = ['a', 'd', 'l', 'q']
        choice = input("Select an option: ").lower()
        while choice not in choices: 
            print("Invalid option. Please try again.")
            choice = input("Select an option: ").lower()
        if choice == 'a':
            event = event_prompt()
            print("Add Event")
            calendar.add_event(event)
            print("Event successfully added.")
        if choice == 'd':
            print("Delete Event")
            date = input("Enter a date (mm/dd/yyyy): ").lower()
            time = input("Enter a start time (hh:mm): ").lower()
            if calendar.delete_event(date,time):
                print("Event successfully deleted.")
            else: 
                print("Event was not deleted.")
        if choice == 'l':
            print("List Events")
            date = input("Enter a date (mm/dd/yyyy): ").lower()
            list_1 = calendar.day_schedule(date)
            if len(list_1) == 0: 
                print("No events to list on " , date)  
            else: 
                for i in list_1:
                    print(P11_Event.__str__(i))
        if choice == 'q':
            break
    
if __name__ == '__main__':
     main()