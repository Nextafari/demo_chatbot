from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import date
from datetime import datetime
# from datetime import time
# import os

# naming the bot
bot = ChatBot("Demo_bot")

trainer = ListTrainer(bot)

today = str(date.today())
date_today = ("Today is, " + today)

date_and_time = str(datetime.now())
say_datetime = ("Today's date and time are " + date_and_time)

conversations = [
    "Hello",
    "Hi",
    "How are you today ?",
    "I am quite well, thank you.",
    "What is today's date ?",
    date_today,
    "What is today ?",
    say_datetime,
    "Are you sapien ?",
    "No I am just a chatbot built by Emmanuel",
]

trainer.train(conversations)


# Variable holding the path to chatterbot_corpus files
# basepath = os.listdir("/home/emmanuel/Desktop/chatbot/chatterbot_corpus/data/english/")

# for files in basepath:
#     # Opening the files in the basepath variable and reading them
#     # line by line to train the bot
#     data = open("/home/emmanuel/Desktop/chatbot/chatterbot_corpus/data/english/" + files, "r").readlines()
#     trainer.train(data)


while True:
    # User input
    message = input("You: ")
    if message != "bye".lower():
        # Bot gets response for user input
        reply = bot.get_response(message)
        print("Demo_bot: ", reply)

    if message == "bye".lower():
        print("Demo_bot: Goodbye")
        break
