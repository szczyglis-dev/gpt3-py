#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# This file is a part of GPT3-py package
# WWW: https://github.com/szczyglis-dev/gpt3-py
# MIT License
# Created By  : Marcin Szczyglinski
# Created Date: 2022.10.15 16:00:00
# =============================================================================

from config import *
from core import *

# init defaults
multiline = False

print("\n========================================")
print(LANG_APP + ", v." + get_version())
print(LANG_AUTHOR)
print(GITHUB_URL)
print("========================================\n")
print(LANG_MODE_SELECT + ":\n")

# list modes
i = 1
for key in modes:
    if modes[key] != "":
        print(str(i) + " - " + modes[key])
        i += 1
    else:
        print("-------------------")

# select mode
tmp_mode = int(input("> ") or 1)
i = 1
for key in modes:
    if modes[key] != "":
        if i == tmp_mode:
            mode = key
            break
        i += 1

# get user config
if mode in modes_chat:
    # temperature / level of abstraction
    print("\n" + LANG_TEMP_CHOOSE + " (" + str(temperature) + "):")
    temperature = float(input("> ") or temperature)

    # custom time
    print("\n" + LANG_TIME_CHOOSE + ":")
    for key in time_modes:
        print(str(key) + " - " + time_modes[key])
    mode_time = int(input("> ") or 0)
    if mode_time == 1:
        print(LANG_SPECIFY_TIME + ":")
        custom_time = input("> ")
    elif mode_time == 2:
        is_realtime = True

    # custom place
    print("\n" + LANG_CHOOSE_PLACE + ":")
    for key in place_modes:
        print(str(key) + " - " + place_modes[key])
    mode_place = int(input("> ") or 0)
    if mode_place == 1:
        print(LANG_SPECIFY_PLACE + ":")
        custom_place = input("> ")

if mode == "chat_custom":
    print(LANG_SPECIFY_PROMPT + ":\n\n" + prompts["chat"])
    print("\n" + LANG_MULTILINE_TIP + "\n")
    prompts["chat"] = get_multiline() or prompts["chat"]

    print(LANG_SPECIFY_STOP)
    stop = input("> ") or ""

# show config
print("\n" + LANG_CHOOSEN_MODE + ": [" + str(tmp_mode) + "] " + modes[mode])

if mode == "chat":
    print(LANG_CHOOSEN_TEMPERATURE + ": " + str(temperature))

    if mode_time == 0:
        print(LANG_CHOOSEN_TIME + ": [" + str(mode_time) + "] " + time_modes[mode_time])
    elif mode_time == 1:
        print(LANG_CHOOSEN_TIME + ": [" + str(mode_time) + "] " + time_modes[mode_time] + " => " + custom_time)
    elif mode_time == 2:
        print(LANG_CHOOSEN_TIME + ": [" + str(mode_time) + "] " + time_modes[mode_time])

    if mode_place == 0:
        print(LANG_CHOOSEN_PLACE + ": [" + str(mode_place) + "] " + place_modes[mode_place])
    elif mode_place == 1:
        print(LANG_CHOOSEN_PLACE + ": [" + str(mode_place) + "] " + place_modes[mode_place] + " => " + custom_place)

elif mode == "chat_custom":
    print("---\n" + prompts["chat"])

# begin chat
print("\n" + LANG_BEGIN + ":")
print("------------------------------")

# if mode requires multiline input
if mode in modes_multiline:
    multiline = True

if multiline:
    print(LANG_MULTILINE_TIP + "\n")

# begin main loop
while (1):
    # get user input
    if multiline:
        user_input = get_multiline();
    else:
        user_input = input("> ")

    # prevent empty input
    if user_input == "":
        continue

    # strip whitespaces
    user_input = user_input.strip()

    # run
    prompt, temperature, stop = run(mode, mode_place, mode_time, user_input, temperature, custom_place, custom_time,
                                    stop, prompts)

    # store to history
    if store_history:
        to_history("> " + user_input)

    # get response
    output = get_response(model, prompt, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, stop)
    if is_moderation:
        output = moderate(output)

    # store to history
    if store_history:
        to_history(output)

    # show output
    print(output)
