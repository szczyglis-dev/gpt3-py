#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================== #
# This file is a part of GPT3-py package          #
# WWW: https://github.com/szczyglis-dev/gpt3-py   #
# MIT License                                     #
# Created By  : Marcin Szczyglinski               #
# Created Date: 2022.10.15 16:00:00               #
# =============================================== #

API_KEY = "<YOUR API KEY HERE>"  # <<<<< put your API key here

is_moderation = False  # enable or disable output moderation
store_history = True  # enable or disable history storage
store_history_time = True  # enable or disable timestamp in history files
history_path = "./history"  # path to the history directory
temperature = 0.3  # default temperature
max_tokens = 1000  # max tokens in output
model = "text-davinci-002"  # model
top_p = 1  # sampling threshold
frequency_penalty = 0.0  # model’s tendency to repeat predictions
presence_penalty = 0.0  # encourages the model to make novel predictions

# initial values
stop = ""
mode = "chat"
mode_time = 0
mode_place = 0
custom_time = ""
custom_place = ""
date_format = "%Y.%m.%d"
time_format = "%H:%M"

# list of modes
modes = {
    "chat": "Chatbot (default)",
    "chat_custom": "Custom chatbot, SYNTAX: https://beta.openai.com/docs/guides/completion",
    "custom": "Custom completion, SYNTAX: https://beta.openai.com/docs/guides/completion",
    "code_humanize": "Translate code to human language",
    "linux_cmd": "Translate into Linux command",
    "windows_cmd": "Translate into Windows command",
    "code_python": "Translate into Python code",
    "code_php": "Translate into PHP code",
    "code_js": "Translate into Javascript code",
    "code_java": "Translate into Java code",
    "code_cpp": "Translate into C++ code",
    "code_csharp": "Translate into C# code",
    "code_sql": "Translate into SQL code",
    "code_assembly": "Translate into Assembly code",
    "code_bash": "Translate into Bash script",
}

# list of modes with conversation options
modes_chat = [
    "chat",
]

# list of modes with multiline input
modes_multiline = ["custom", "code_humanize"]

# list of time modes
time_modes = {
    0: "Do not set custom time (default)",
    1: "Custom time",
    2: "Real time",
}

# list of place modes
place_modes = {
    0: "Do not set custom place (default)",
    1: "Custom place",
}

# list of dayofweek names
daysofweek = {
    0: "monday",
    1: "thuesday",
    2: "wednesday",
    3: "thursday",
    4: "friday",
    5: "saturday",
    6: "sunday",
}

# prompts
prompts = {
    "chat": "AI is an artificial intelligence that talks to a Human and answering all questions in detail.<EXTRA>\nHuman:Hi\nAI:Hello\nHuman:<INPUT>\nAI:",
    "linux_cmd": "Convert this text to a linux command:\n<INPUT>",
    "windows_cmd": "AI is an artificial intelligence that translates text into two commands: DOS and PowerShell.\nA:format disk 1\nB:DOS:\nformat C: /q\n\nPowerShell:\nclear-disk -number 1 -removedata\nA:<INPUT>\nB:",
    "code_humanize": "AI is an artificial intelligence that analyzes code and translates its parts into human language.\nHuman:a + b = c\nAI:The code adds the variables a and b together and writes the result to the variable c.\nHuman:Describe what the following code does:<INPUT>\nAI:",
    "code_python": "Translate this into Python code:\n<INPUT>",
    "code_php": "Translate this into PHP code:\n<INPUT>",
    "code_js": "Translate this into Javascript code:\n<INPUT>",
    "code_java": "Translate this into Java code:\n<INPUT>",
    "code_cpp": "Translate this into C++ code:\n<INPUT>",
    "code_csharp": "Translate this into C# code:\n<INPUT>",
    "code_sql": "Translate this into SQL code:\n<INPUT>",
    "code_assembly": "Translate this into Assembly code:\n<INPUT>",
    "code_bash": "Translate this into Bash code:\n<INPUT>",
}

# language strings
GITHUB_URL = "https://github.com/szczyglis-dev/gpt3-py"
LANG_APP = "gpt3-py"
LANG_AUTHOR = "author: Marcin 'szczyglis' Szczyglinski"
LANG_MODE_SELECT = "CHOOSE MODE"
LANG_TEMP_CHOOSE = "SET TEMPERATURE FROM 0.0 to 1.0, WHERE 0.0 = LESS ABSTRACTION, 1.0 = MORE ABSTRACTION, OR LEAVE EMPTY TO LEAVE DEFAULT"
LANG_TIME_CHOOSE = "CHOOSE TIME, OR LEAVE EMPTY IF YOU DO NOT WANT TO SET CUSTOM TIME"
LANG_SPECIFY_TIME = "SPECIFY CUSTOM TIME (e.g. Monday, 2022.10.03, 12:00)"
LANG_CHOOSE_PLACE = "CHOOSE PLACE FOR CONVERSATION, OR LEAVE EMPTY IF YOU DO NOT WANT TO SET CUSTOM PLACE"
LANG_SPECIFY_PLACE = "SPECIFY CUSTOM PLACE FOR CONVERSATION (e.g. in cofeeshop)"
LANG_SPECIFY_PROMPT = "SPECIFY CUSTOM CHAT, use <INPUT> for input placeholder, e.g."
LANG_SPECIFY_STOP = "SPECIFY STOP WORD OR LEAVE EMPTY FOR DEFAULT (Human)"
LANG_MULTILINE_TIP = "[MULTILINE - 2x ENTER = send]"
LANG_CHOOSEN_MODE = "CHOOSEN MODE"
LANG_CHOOSEN_TEMPERATURE = "CHOOSEN TEMPERATURE"
LANG_CHOOSEN_TIME = "CHOOSEN TIME"
LANG_CHOOSEN_PLACE = "CHOOSEN PLACE"
LANG_BEGIN = "BEGIN"
LANG_PROMPT_PLACE_PREFIX = "Conversation takes place in"
LANG_PROMPT_TIME_PREFIX = "Current time is"
LANG_HUMAN_STOP = "Human"
