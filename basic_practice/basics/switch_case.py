# -------------------- switch(match in python) case ------------
from datetime import datetime

def main():
    now = datetime.now()

    current_day = now.strftime("%A") #extracting name of current day
    print(current_day)
    match current_day:
        case "Sunday":
            print("Start of week")
        case "Monday":
            print("Today is monday")
        case _:
            print("Holiday!!")

if __name__ == "__main__":
    main()