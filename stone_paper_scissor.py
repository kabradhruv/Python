import random
import pyttsx3

# this line is to initiate pyttsx3 module and change the speed of the voice
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio, rate=150):
    engine.setProperty('rate', rate)
    engine.say(audio)
    engine.runAndWait()


def game():
    computer_choice_func = lambda c=None: random.choice(['stone', 'paper', 'scissor'])
    user_points = 0
    computer_points = 0
    speak("Choose between 1 for Stone"
          "2 for paper "
          "and 3 for scissor")
    for i in range(3):
        print(f"Sir your points=={user_points}")
        print(f"My points=={computer_points}")
        print(f"{i + 1}. Chance ")
        computer_choice = computer_choice_func()
        print("Choose between 3\n1 for Stone\n2 for paper\n3 for scissor")
        user_choice = int(input("Enter your choice:"))
        try:
            user_choice = choice_dict[user_choice]
        except KeyError:
            print("Wrong input.Type between 1-3")
            game()
        except Exception as e:
            print(e)

        if user_choice == computer_choice:
            speak(f"We both choose {user_choice} so no points")
            print(f"We both choose {user_choice} so no points")
        elif user_choice == 'stone' and computer_choice == 'paper':
            speak(f"I won this round as you choose {user_choice} and I choose {computer_choice}")
            print(f"I won this round as you choose {user_choice} and I choose {computer_choice}")
            computer_points += 1
        elif user_choice == 'stone' and computer_choice == 'scissor':
            speak(f"You won this round as you choose {user_choice} and I choose {computer_choice}")
            print(f"You won this round as you choose {user_choice} and I choose {computer_choice}")
            user_points += 1
        elif user_choice == 'paper' and computer_choice == 'stone':
            speak(f"You won this round as you choose {user_choice} and I choose {computer_choice}")
            print(f"You won this round as you choose {user_choice} and I choose {computer_choice}")
            user_points += 1
        elif user_choice == 'paper' and computer_choice == 'scissor':
            speak(f"I won this round as you choose {user_choice} and I choose {computer_choice}")
            print(f"I won this round as you choose {user_choice} and I choose {computer_choice}")
            computer_points += 1
        elif user_choice == 'scissor' and computer_choice == 'stone':
            speak(f"I won this round as you choose {user_choice} and I choose {computer_choice}")
            print(f"I won this round as you choose {user_choice} and I choose {computer_choice}")
            computer_points += 1
        elif user_choice == 'scissor' and computer_choice == 'paper':
            speak(f"You won this round as you choose {user_choice} and I choose {computer_choice}")
            print(f"You won this round as you choose {user_choice} and I choose {computer_choice}")
            user_points += 1
        else:
            pass
    return user_points, computer_points


def start_game():
    user_points, computer_points = game()
    if user_points > computer_points:
        speak("You won this round Congratulations sir you beat me")
        print("You won this round Congratulations sir you beat me")
    elif computer_points > user_points:
        speak("You lost this round Sorry sir you can play again")
        print("You lost this round Sir")
        rotate_screen()
    elif computer_points == user_points:
        speak("It's a tie sir")
        print("It's a tie sir")
    else:
        pass
    play_again_func()


def rotate_screen():
    import rotatescreen
    import time
    screen = rotatescreen.get_primary_display()
    speak("Don't do anything sir It's just a price you have to pay as you lost It will fix automaticaly")
    for i in range(10):
        screen.rotate_to(i * 90 % 360)
        time.sleep(1.5)
    screen.rotate_to(0)


def play_again_func():
    speak("Sir Do you want to play again")
    print("Sir Do you want to play again")
    speak("Type 1 for yes and 2 for no")
    play_again = int(input("Type 1 for yes\n2 for no:"))
    try:
        if play_again == 1:
            start_game()
        elif play_again == 2:
            speak("Ok sir bye bye and Come again")
            print("Ok sir bye bye and Come again")
        else:
            raise IndexError
    except IndexError:
        speak("Type between 1 and 2 fool")
        print("Type between 1 and 2 fool")
        play_again_func()


choice_dict = {1: 'stone', 2: 'paper', 3: 'scissor'}

speak("Welcome to the Stone paper scissor game I am jarvis your host and competition sir Let's start")
print("Welcome to the Stone paper scissor game I am jarvis your host and competition Let's start")
speak("A round contains 10 chances and a winner is declared after that")
print("A round contains 10 chances and a winner is declared after that")

start_game()
