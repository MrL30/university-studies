# Exercise 2: Clock arithmetic

print("=" * 64)

def current_time():
    """This function traps the user until they choose a valid clock format."""
    while True:
        clock = int(input("What clock do you use (12 / 24): "))
        if clock == 12 or clock == 24:
            return clock
        else:
            print("Wrong input, try again...\n")

def twelveh_clock():
    """Calculates time for a 12-hour format."""
    hour = int(input("What hour is it (12 hour format): "))
    add_hour = int(input("How many hours do you want to add: "))
    
    final_hour = hour + add_hour
    wrapped_hour = final_hour % 12
    
    # A 12-hour clock has no '0', so if the remainder is 0, we change it to 12.
    if wrapped_hour == 0:
        wrapped_hour = 12
        
    print(f"It will be {wrapped_hour}h after we add {add_hour}h")

def twenty4h_clock():
    """Calculates time for a 24-hour format."""
    hour = int(input("What hour is it (24 hour format): "))
    add_hour = int(input("How many hours do you want to add: "))
    
    final_hour = hour + add_hour    
    wrapped_hour = final_hour % 24
    
    print(f"It will be {wrapped_hour}h after we add {add_hour}h")

def main():
    chosen_format = current_time()
    
    if chosen_format == 12:
        twelveh_clock()
    elif chosen_format == 24:
        twenty4h_clock()
    else:
        print("Debug: Unexpected error in format selection.")

# Start the program
main()

print("=" * 64)