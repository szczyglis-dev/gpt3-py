#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================== #
# This file is a part of GPT3-py package          #
# WWW: https://github.com/szczyglis-dev/gpt3-py   #
# MIT License                                     #
# Created By  : Marcin Szczyglinski               #
# Created Date: 2022.10.15 16:00:00               #
# =============================================== #

from config import *
import openai
import datetime
import os
import re

openai.api_key = API_KEY


# gets multiline input
def get_multiline():
    lines = []
    print(">>>")
    while True:
        i = input()
        if i == "":
            break
        lines.append(i)
    return "\n".join(lines)


# sends request to API
def get_response(model, prompt, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, stop):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=[stop],
    )
    return response.choices[0].text.strip()


# moderates  output
def moderate(text):
    response = openai.Moderation.create(
        input=text,
    )
    flagged = response["results"][0]["flagged"]
    if flagged:
        text = "<CENSORED>"
    return text


# appends custom place and time
def append_extra(prompt, mode_place, mode_time, custom_place, custom_time):
    extra_data = ""
    # if custom place
    if mode_place == 1:
        extra_data += " " + LANG_PROMPT_PLACE_PREFIX + " " + custom_place.strip()

    # if custom time
    if mode_time == 1:
        extra_data += " " + LANG_PROMPT_TIME_PREFIX + " " + custom_time.strip()

    # if real time
    elif mode_time == 2:
        # append current time
        current_time = daysofweek[datetime.datetime.today().weekday()]
        current_time += ", " + datetime.date.today().strftime(date_format)
        current_time += " at " + datetime.datetime.now().strftime(time_format)
        extra_data += " " + LANG_PROMPT_TIME_PREFIX + " " + current_time

    return prompt.strip().replace("<EXTRA>", extra_data)


# reads version info
def get_version():
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format("__version__"), open('./__init__.py').read())
    return result.group(1)


# stores chat to history
def to_history(text):
    fname = datetime.date.today().strftime("%Y_%m_%d") + ".txt"
    if os.path.exists(history_path) == False:
        os.makedirs(history_path)
    if os.path.exists(history_path):
        file = open(history_path + "/" + fname, 'a')
        prefix = ""
        if store_history_time:
            prefix = datetime.datetime.now().strftime("%H:%M:%S") + ": "
        file.write(prefix + text + "\n")
        file.close()


# appends user input
def append_input(prompt, user_input):
    return prompt.strip().replace("<INPUT>", user_input)


# runs chat
def run(mode, mode_place, mode_time, user_input, temperature, custom_place, custom_time, stop, prompts):
    stop = stop.replace(":", "")
    prompt = ""

    if mode == "chat":
        if stop == "":
            stop = LANG_HUMAN_STOP + ":"
        prompts["chat"] = append_extra(prompts["chat"], mode_place, mode_time, custom_place, custom_time)
        prompt = append_input(prompts["chat"], user_input)
    elif mode == "chat_custom":
        if stop == "":
            stop = LANG_HUMAN_STOP + ":"
        prompt = append_input(prompts["chat"], user_input)
    elif mode == "custom":
        stop = "@!__!@"
        prompt = user_input.strip()
    elif mode == "code_humanize":
        if stop == "":
            stop = LANG_HUMAN_STOP + ":"
        temperature = 0.0
        prompt = append_input(prompts["code_humanize"], user_input)
    elif mode == "linux_cmd":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["linux_cmd"], user_input)
    elif mode == "windows_cmd":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["windows_cmd"], user_input)
    elif mode == "code_python":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_python"], user_input)
    elif mode == "code_php":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_php"], user_input)
    elif mode == "code_js":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_js"], user_input)
    elif mode == "code_typescript":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_typescript"], user_input)
    elif mode == "code_java":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_java"], user_input)
    elif mode == "code_cpp":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_cpp"], user_input)
    elif mode == "code_csharp":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_csharp"], user_input)
    elif mode == "code_sql":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_sql"], user_input)
    elif mode == "code_assembly":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_assembly"], user_input)
    elif mode == "code_bash":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_bash"], user_input)
    elif mode == "code_qsharp":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_qsharp"], user_input)
    elif mode == "code_ruby":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_ruby"], user_input)
    elif mode == "code_go":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_go"], user_input)
    elif mode == "code_perl":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_perl"], user_input)
    elif mode == "code_r":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_r"], user_input)
    elif mode == "code_matlab":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_matlab"], user_input)
    elif mode == "code_lua":
        stop = "@!__!@"
        temperature = 0.0
        prompt = append_input(prompts["code_lua"], user_input)

    return prompt, temperature, stop
