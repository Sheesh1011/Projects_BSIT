import time
import os
cyan = "\033[36m"
violet = "\033[35m"
reset = "\033[0m"

def square_loading():
    for k in range(1, 11):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(cyan+"\nLoading...\n"+reset)
        print("[" + "■" * k + " " * (10 - k) + "]""\n")
        time.sleep(0.09)

def square_code_loading():
    for k in range(1, 11):
        os.system('cls' if os.name == 'nt' else 'clear')
        # print(blue+"\nRunning your code...\n"+reset)
        # print("[" + "■" * k + " " * (10 - k) + "]""\n")
        print(cyan+"Running your code" + "." * k + " " * (10 - k) +reset)
        time.sleep(0.1)

def code_exe(): # Function to execute user-entered code
    print(cyan+"Type your Python code below. Type RUN on a new line to finish.\n"+reset)

    code_lines = [] # Collects code line by line
    while True:
        line = input()
        if line.strip().upper() == "RUN":
            break
        code_lines.append(line)

    user_code = "\n".join(code_lines)

    square_code_loading()
    os.system('cls')

    # Attempts to execute the code
    try:
        exec(user_code)
    except Exception as e:
        print(violet+"Error:", e, reset)# Handles errors gracefully