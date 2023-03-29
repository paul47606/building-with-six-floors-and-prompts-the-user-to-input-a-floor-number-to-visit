import pyttsx3

text_speech = pyttsx3.init()
first = "sorry, Please use steps hint: go to ground floor and use steps"
second = "sorry, Please use steps hint: go to ground floor and use steps"
third = "Welcome to 3rd floor"
forth = "Welcome to 4th floor"
five = "Welcome to 5th floor"
six = "Welcome to 6th floor"
zero = "welcome to ground floor"

print("  0 \n1 2 3\n4 5 6")
while True:
    left = int(input("Please enter your number: "))
    if left == 1:
        print(
            f"sorry, Please use steps hint: go to ground floor and use steps {text_speech.say(first)}{text_speech.runAndWait()}")
        print("1 2 3\n4 5 6")
        left = int(input("Please enter your number: "))
    elif left == 2:
        print(
            f"sorry, Please use steps hint: go to ground floor and use steps {text_speech.say(first)}{text_speech.runAndWait()}")
        print("1 2 3\n4 5 6")
        left = int(input("Please enter your number: "))

    elif left == 0:
        print(
            f"*******************Welcome to ground floor******************* {text_speech.say(zero)}{text_speech.runAndWait()}")
        if left == 1:
            print(
                f"sorry, Please use steps hint: go to ground floor and use steps {text_speech.say(first)}{text_speech.runAndWait()}")
        elif left == 2:
            print(
                f"sorry, Please use steps hint: go to ground floor and use steps {text_speech.say(second)}{text_speech.runAndWait()}")
        elif left == 4:
            print(
                f"*******************Welcome to 4th floor******************* {text_speech.say(forth)}{text_speech.runAndWait()}")
        elif left == 5:
            print(
                f"*******************Welcome to 5th floor******************* {text_speech.say(five)}{text_speech.runAndWait()}")
        elif left == 6:
            print(
                f"*******************Welcome to 6th floor******************* {text_speech.say(six)}{text_speech.runAndWait()}")

    elif left == 3:
        print(
            f"*******************Welcome to 3rd floor******************* {text_speech.say(third)}{text_speech.runAndWait()}")
        print("1 2 3\n4 5 6")
        left = int(input("Please enter your number: "))
        if left == 0:
            print(
                f"*******************Welcome to ground floor*******************{text_speech.say(zero)}{text_speech.runAndWait()}")
        elif left == 4:
            print(
                f"*******************Welcome to 4th floor******************* {text_speech.say(forth)}{text_speech.runAndWait()}")
        elif left == 5:
            print(
                f"*******************Welcome to 5th floor******************* {text_speech.say(five)}{text_speech.runAndWait()}")
        elif left == 6:
            print(
                f"*******************Welcome to 6th floor******************* {text_speech.say(six)}{text_speech.runAndWait()}")

    elif left == 4:
        print(
            f"*******************Welcome to 4th floor******************* {text_speech.say(forth)}{text_speech.runAndWait()}")
        print("1 2 3\n4 5 6")
        left = int(input("Please enter your number: "))
        if left == 0:
            print(
                f"*******************Welcome to ground floor******************* {text_speech.say(zero)}{text_speech.runAndWait()}")
        elif left == 3:
            print(
                f"*******************Welcome to 3rd floor******************* {text_speech.say(third)}{text_speech.runAndWait()}")
        elif left == 5:
            print(
                f"*******************Welcome to 5th floor******************* {text_speech.say(five)}{text_speech.runAndWait()}")
        elif left == 6:
            print(
                f"*******************Welcome to 6th floor******************* {text_speech.say(six)}{text_speech.runAndWait()}")

    elif left == 5:
        print(
            f"*******************Welcome to 5th floor******************* {text_speech.say(five)}{text_speech.runAndWait()}")
        print("1 2 3\n4 5 6")
        left = int(input("Please enter your number: "))
        if left == 0:
            print(
                f"*******************Welcome to ground floor******************* {text_speech.say(zero)}{text_speech.runAndWait()}")
        elif left == 3:
            print(
                f"*******************Welcome to 3rd floor******************* {text_speech.say(third)}{text_speech.runAndWait()}")
        elif left == 4:
            print(
                f"*******************Welcome to 4th floor******************* {text_speech.say(forth)}{text_speech.runAndWait()}")
        elif left == 6:
            print(
                f"*******************Welcome to 6th floor******************* {text_speech.say(six)}{text_speech.runAndWait()}")

    elif left == 6:
        print(
            f"*******************Welcome to 6th floor******************* {text_speech.say(six)}{text_speech.runAndWait()}")
        print("1 2 3\n4 5 6")
        left = int(input("Please enter your number: "))
        if left == 0:
            print(
                f"*******************Welcome to ground floor******************* {text_speech.say(zero)}{text_speech.runAndWait()}")
        elif left == 3:
            print(
                f"*******************Welcome to 3rd floor******************* {text_speech.say(third)}{text_speech.runAndWait()}")
        elif left == 4:
            print(
                f"*******************Welcome to 4th floor******************* {text_speech.say(forth)}{text_speech.runAndWait()}")
        elif left == 5:
            print(
                f"*******************Welcome to 5th floor******************* {text_speech.say(five)}{text_speech.runAndWait()}")

