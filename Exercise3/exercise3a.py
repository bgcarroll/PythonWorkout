from statistics import mean

def run_timing():

    run_times = []

    while True:
        run_time = input("Enter 10 km run time: ")
        try:
            run_times.append(float(run_time))
        except:
            break #breaks when the use hits "Enter"

    if len(run_times) == 0:
        print("You did not enter any data.")
    else:
        print(f'Average of {round(mean(run_times), 1)}, over {len(run_times)} runs')

run_timing()
