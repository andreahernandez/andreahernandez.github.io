# --- Define your functions below! ---
def hi():
    print("hi")

def hello():
    print("hello")

def day():
    print("pretty good hbu")

def process_input():
    if (answer == "hello" ):
        hi()
    elif("hi" in answer):
        hello()
    elif( answer == "how is your day? "):
        day()


# --- Put your main program below! ---
def main():
  while True:
    answer == input("What will you say")
    process_input()


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
