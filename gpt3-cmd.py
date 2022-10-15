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
import sys

# get user input
user_input = sys.argv[1]

# strip whitespaces
user_input = user_input.strip()

# run
prompt, temperature, stop = run(mode, mode_place, mode_time, user_input, temperature, custom_place, custom_time, stop, prompts)

# store to history
if store_history:
	to_history("> " + user_input)

# show response	
output = get_response(model, prompt, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, stop)
if is_moderation:
	output = moderate(output)

# store to history
if store_history:
	to_history(output)

# show output
print(output)