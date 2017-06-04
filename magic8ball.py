import random
import time
import sys

list = ["Yes, most definitely!", "The chances are high!", "Not likely!", "May the odds be ever in your favor.",
                        "You got no shot, kid.", "Try it out and see!", "23% of working", "99.9% success rate",
                        "Congratulations, yes!", "Ask a probably question," "Ask again later", "Better not tell you now",
           "Cannot predict now", "Concentrate and ask again", "Don't count on it"
        ]
def userinput():
        question = 'Enter your question:'
        print(question)
        stuff = input("> ")

        print("\nThinking..\n")
        time.sleep(3)
        print(random.choice(list))

        final()

def final():
        print("Would you like to ask another question?")
        user_reply = input('> ')
        while(input):
                if user_reply == "yes":
                        userinput()
                else:
                        print("Thanks for playing!")
                        sys.exit(0)
print("Welcome to the Magic 8 Ball!")
userinput()
