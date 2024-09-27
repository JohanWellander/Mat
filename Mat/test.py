import os
from datetime import datetime

def main():
    print("testing testing!!!!")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"This test is performed at: {current_time}")
    print("This is an added test")


if __name__ == "__main__":
    main()