Python: **3.7+**, current release: **1.0.0** build 2022-10-15

# GPT3-py

**GPT-py is a Bring-Your-Own-Key terminal application written in Python 3, allowing easy interaction with the OpenAI's GPT-3 artificial intelligence. The application provides a chat mode in the form of a configurable chatbot, as well as additional functions such as generating code in several different languages (Python, C++, C#, Java, Javascript, PHP, Assembly, SQL and Bash), translating the code into a human language, generating Linux and Windows commands based on the description and much more. The application is easy to configure and can be extended with your own features.**

>**INFO: The application requires your own API key to work and is intended for home use on a local machine.**

## Features:

- GPT-3 powered chatbot running in the terminal
- defining the terms of conversation with the chatbot, such as time and place
- chatbot configuration
- creating custom queries to GPT-3
- Python, C++, C#, Java, Javascript, PHP, Assembly, SQL and Bash code generation from description
- analysis and translation of code operation into human language
- generating commands for Linux on the description
- generating commands for Window (DOS and Powershell) from the description
- easy to configure and modify
- works under any operating system in the terminal
- includes separate scripts that take input from STDIN and command line argument
- built-in output content moderation

## Requirements:

- Python: 3.7+
- openai >= 0.22.1


## How to install:

Download or clone repository and install required packages:

```pip3 install -r ./requirements.txt```

or 

```pip3 install openai```


## First launch:

You must have an OpenAI account and obtain **your own API key** required for use with the application.
After registering on the https://beta.openai.com/ website, generate your own API key and put it in the config file:

```./config.py```

in section:

```API_KEY = "<YOUR API KEY HERE>"```


After placing your API key in the config file, the application is ready for use, run it with:


```python3 ./gpt3.py```

or

```./gpt3.py```

## Screenshot:

![gpt33](https://user-images.githubusercontent.com/61396542/195992693-74ba8623-01ee-4810-ab2b-d6685ed2e45d.png)


## Feature list:

```
1 - Chatbot
2 - Custom chatbot
3 - Custom completion
4 - Translate code to human language
5 - Translate into Linux command
6 - Translate into Windows command
7 - Translate into Python code
8 - Translate into PHP code
9 - Translate into Javascript code
10 - Translate into Java code
11 - Translate into C++ code
12 - Translate into C# code
13 - Translate into SQL code
14 - Translate into Assembly code
15 - Translate into Bash script
```

# Usage:


## 1 - Chatbot (default)

Default chatbot with which you can talk to GPT-3.

After selecting this option, configuration options will be displayed allowing you to define the terms of the conversation:

```SET TEMPERATURE FROM 0.0 to 1.0, WHERE 0.0 = LESS ABSTRACTION, 1.0 = MORE ABSTRACTION, OR LEAVE EMPTY TO LEAVE DEFAULT (0.3):```

The above allows to define the temperature of the conversation in the range from 0.0 to 1.0.
The lower the value, the more precise chatbot responses are, the higher the value, the more abstract the responses will be.

In the next step, you can define the time of the conversation:

```
CHOOSE TIME, OR LEAVE EMPTY IF YOU DO NOT WANT TO SET CUSTOM TIME:
0 - Do not set custom time (default)
1 - Custom time
2 - Real time```
```
By default, the time is not specified, but you can enter your own time or choose the real time. When choosing the option to enter your own time, you can enter the full date, time or time of the day, e.g.:

```Monday, 2022.10.03, 12:00```

or

```evening```

If you choose real time, the time will be determined automatically according to the current time.

In the last prompt, you can choose the circumstances or place of the conversation, or leave the default selection so as not to specify the place:

```
CHOOSE PLACE FOR CONVERSATION, OR LEAVE EMPTY IF YOU DO NOT WANT TO SET CUSTOM PLACE:
0 - Do not set custom place (default)
1 - Custom place
```

Example of choosing a place if you have chosen to define your own place:

**[1] and press Enter**

```SPECIFY CUSTOM PLACE FOR CONVERSATION (e.g. in cofeeshop):
> in home
```

This will result in the following behavior during the conversation:

```
BEGIN:
------------------------------
> hi, where are we now?
We are currently in your home.
> what do you thing about this place?
I think this place is great! It's really cozy and has a lot of character.

---------
```

**Tip:** to end the conversation at any time and exit the application, use the **CTRL+C** key combination.

## 2 - Custom chatbot

In this feature, you can program GPT-3 yourself, so that the conversation proceeds according to the scenario you set.

For help with creating queries, visit the OpenAI website: https://beta.openai.com/docs/guides/completion


**Example query:**

```
Batman is a hero. A Human is a person who meets Batman on the street.
Human: Hi
Batman: Hello
Human:<INPUT>
Batman:
```

Preparing the above scenario will give you the opportunity to "talk to Batman":

```
BEGIN:
------------------------------
> what are you doing?
I am fighting crime.
```

**Tip:** when creating your query, use the placeholder ``<INPUT>`` for user input. It will be replaced with the text entered from the terminal.


## 3 - Custom completion

This feature allows you to prepare your own query for GPT-3, with the difference that the query must be specified during each loop run. 

The feature can be used for e.g. data analysis or to generate stories.

**Example query:**

```
>>>
Topic: Superman
Story: Superman is a comic superhero who saves people. Once upon a time, Superman had to save the Earth from an alien invasion.
    
Topic: Tony Stark
Story: 
```

**Result:**

```Tony Stark is a billionaire who creates technology. He is also the superhero Iron Man. Once, Tony Stark had to save the world from a giant robot.```


You can find more usage examples on the OpenAI website: https://beta.openai.com/examples


## 4 - Translate code to human language

This feature allows any code to be translated into human language.
You can enter any code to get an explanation of how it works.

**Example query:**
```
> if (a > 1) b = true;
```

**Result:**

```The code checks if the value of the variable a is greater than 1. If it is, the code sets the value of the variable b to true.```

## 5 - Translate into Linux command

The option allows you to generate any command for Linux based on the description.

**Example query:**

```
> create /home/user/file.txt, copy it to /home/tmp, then zip the files from /home/tmp to files.tar.gz
```

**Result:**
```
cp /home/user/file.txt /home/tmp
tar -czvf files.tar.gz /home/tmp
```

## 6 - Translate into Windows command

This feature allows you to generate any command for Windows (DOS + Powershell) based on the description.

**Example query:**

```
> create test directory on drive C:, copy files to it from directory D:\files, and finally move files from directory C:\test to drive E:\
```

**Result:**

```
DOS:
md C:\test
copy D:\files C:\test
move C:\test E:\

PowerShell:
New-Item -Path 'C:\test' -ItemType Directory
Copy-Item -Path 'D:\files' -Destination 'C:\test'
Move-Item -Path 'C:\test' -Destination 'E:\'
```

## 7 - Translate into Python code and other languages

Features **7 to 15** allow you to generate code based on the description of the action.

The following is an example query of use for Python:

```
> read all files in the ./test directory, pack them all, and save them to packed.zip
```

**Result:**

```
import os
import zipfile

def pack(dir, zip_file):
    for root, dirs, files in os.walk(dir):
        for file in files:
            zip_file.write(os.path.join(root, file))

with zipfile.ZipFile('packed.zip', 'w') as zip_file:
    pack('./test', zip_file)

```

The code generation for other languages is the same.

Here is an example for Bash:

**15 - Translate into Bash script**

**Example query:**

```
if /home/test exists, then copy all files from /home/tmp to it
```

**Result:**

```
if [ -d /home/test ]; then cp -r /home/tmp/* /home/test/; fi
```


## Get input from a STDIN

There is a separate script in the repository that takes input from STDIN and returns a single response from GPT-3. 

This can be used to connect I/O with other commands and programs.

**Example:**

```python3 ./gpt3-stdin.py```

Command in the terminal:

```echo "Hello" | python3 ./gpt3-stdin.py```

**Result:**

```Hello there! How are you doing today?```


## Getting input from a command line argument

There is a separate script in the repository that takes input from the command line argument and returns a single response from GPT-3. 

This can be used to connect I/O with other commands and programs.

**Example:**

```python3 ./gpt3-cmd.py```

Command in the terminal:

```
python3 ./gpt3-cmd.py "hello!" > ./output.txt
cat ./output.txt
```

**Result:**

```Hello! How are you doing today?```


## Moderation

The package includes a built-in moderation of responses returned by GPT-3, responsible for filtering inappropriate content. 

Moderation can be turned on or off using the parameter:


```is_moderation = True/False```

located in the file:

```./config.py```


## History storage

The application has the option of saving the entire history of conversations to .txt files.
To enable or disable saving to history use:

```store_history = True/False```

located in the file:

```./config.py```

By default, history is saved to the ```./history``` directory.


## Additional configuration

You can freely configure the operation of the application, specifying parameters such as the selected model (the default model is DaVinci), the maximum number of tokens and other options in the config file:

```
# config.py

is_moderation = False # enable or disable output moderation
store_history = True # enable or disable history storage
store_history_time = True # enable or disable timestamp in history files
history_path = "./history" # path to the history directory
temperature = 0.3 # default temperature
max_tokens = 1000 # max tokens in output
model = "text-davinci-002" # model
top_p = 1 # sampling threshold
frequency_penalty = 0.0 # model’s tendency to repeat predictions
presence_penalty = 0.0 # encourages the model to make novel predictions

# initial values
stop = ""
mode = "chat"
mode_time = 0
mode_place = 0
custom_time = ""
custom_place = ""
date_format = "%Y.%m.%d"
time_format = "%H:%M"
```

**The application is intended for personal home use.**

**Please note that if you choose to use it for commercial use, please report the use to the App Review procedure on the OpenAI website.**

___

## Changelog

**- 1.0.0** - Published first release. (2022-10-15)


## Credits
 
### GPT3-py is free to use but if you liked then you can donate project via BTC: 

**14X6zSCbkU5wojcXZMgT9a4EnJNcieTrcr**

or by PayPal:
 **[https://www.paypal.me/szczyglinski](https://www.paypal.me/szczyglinski)**


**Enjoy!**

MIT License | 2022 Marcin 'szczyglis' Szczygliński

https://github.com/szczyglis-dev/gpt3-py

https://szczyglis.dev

Contact: szczyglis@protonmail.com
