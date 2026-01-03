import logging

logging.basicConfig(level=logging.ERROR, filename="time calculation.log")
def calc_time():
    try:
        speed = int(input("Enter the speed...")) # user may enter text which raises value error
        distance = int(input("Enter the distance..."))
        if speed <= 0: # <0: negative, =0: division by zero
            raise ValueError("Speed must be greater than zero")
        time = distance/speed
        print(f"Time required: {time}")
    except Exception:
        logging.error("Failed to calculate time", exc_info=True) # logging just records error. doesn't prevent crash

calc_time()

print("Program still running after handling error. Logs printed to file")