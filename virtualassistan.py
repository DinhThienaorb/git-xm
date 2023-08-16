import speech_recognition
import pyttsx3 
from datetime import date
from datetime import datetime
from random import randint

story = randint(1,3)

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    #Nơi nhận dạng âm thanh(nghe)
    with speech_recognition.Microphone() as mic:
        x =  " I'm listening!"
        print("Robot: " + x)
        robot_mouth.say(x)
        robot_mouth.runAndWait()
        audio = robot_ear.listen(mic)
    print("Robot:...")
    
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you )
    #Nơi xử lí điều kiện (Hiểu)
    if you == "":
        robot_brain = "Sorry, I can't hear, try again!"


    elif "hello" in you :
        robot_brain = "Hi sir!"

    elif "what is your name" in you:
        robot_brain = "I'm Luffy. I can have a mini chat"


    elif  "day" in you:
        today = date.today()
        robot_brain = today.strftime("%A %D")


    elif "time" in you :
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")


    elif "what is your gender" in you :
        robot_brain = "I don't know. But I think I'm bisexual"


    


    elif "when was you born" in you:
        robot_brain = "I was born on march 26, 2023"


    elif "president" in you:
        robot_brain = "Võ Văn Thưởng is a president of Viet Nam"


    elif "girlfriend" in you :
        robot_brain = "oh!I don't"


    elif "you are stupid" in  you:
        robot_brain = "Sorry, I'm being developed "


    elif "do you think I'm so handsome" in you :
        robot_brain = " YES, you are handsome"


    elif  "working" in you :
        robot_brain = " I'm a virtual assistant, and work in a start up "

    if "who are your parents" in you:
        robot_brain = "I was invented by Thiên"

    elif "love you" in you :
        robot_brain = "Wow can you believe this! When finally this moment comes. You know, I've been waiting a long time to say this: I love you too, the best person in the world"


    elif "play a song" in you:
        robot_brain = "I can't sing, but i can read a song. We don't talk anymore, We don't talk anymore, We don't talk anymore, Like we used to do, We don't love anymore, What was all of it for? Oh, we don't talk anymore Like we used to do"


    elif "a ghost story" in you :
        robot_brain = " In the old days of processing, there was a member assistant who was looking up information when suddenly… lost his life"

    elif "can i outside" in you   :
        robot_brain = "You can go out anytime."

    elif "who is the best" in you :
        robot_brain = " Yah sure! I'm the best "

    elif "some money" in you :
        robot_brain = "Sorry, I have no money "

    elif "comedy" in you :    
                    if story == 1 :
                        robot_brain = "China has a population of a billion people. One billion. That means even if you're a one in a million kind of guy, there are still a thousand others exactly like you."
                    elif story == 3 :
                        robot_brain = "Three guys stranded on a desert island find a magic lantern containing a genie, who grants them each one wish. The first guy wishes he was off the island and back home. The second guy wishes the same. The third guy says: 'I'm lonely. I wish my friends were back here.'"
                    elif story == 2:
                        robot_brain = "A guy is sitting at home when he hears a knock at the door. He opens the door and sees a snail on the porch. He picks up the snail and throws it as far as he can. Three years later there’s a knock on the door. He opens it and sees the same snail. The snail says, 'What the hell was that all about?'."
    elif "bye" in you or "good job " in you :
        robot_brain = "Have a good day, bye"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else :
        robot_brain = "I'm fine thank you"
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()


