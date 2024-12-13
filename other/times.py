import time

def main():
    start_time = time.time()

    # Your code here
    time.sleep(5)  # Simulate a process that takes time (2 minutes)

    end_time = time.time()
    elapsed_time_in_minutes = (end_time - start_time) / 60
    print(f"Elapsed time: {elapsed_time_in_minutes:.2f} minutes")


    # Get the current time in seconds since the epoch
    current_time = time.time()

    # Convert the time to minutes
    current_time_in_minutes = current_time / 60

    print(f"Current time in minutes since the epoch: {current_time_in_minutes:.2f}")

if __name__=="__main__":
    main()