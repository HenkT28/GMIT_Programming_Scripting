# https://stackoverflow.com/questions/17645327/python-3-3-how-to-grab-every-5th-word-in-a-text-file

textInput = """\
I'm trying to have my program grab every fifth word from a text file and
place it in a single string. For instance, if I typed "Everyone likes to
eat pie because it tastes so good plus it comes in many varieties such
as blueberry strawberry and lime" then the program should print out
"Everyone because plus varieties and." I must start with the very first
word and grab every fifth word after. I'm confused on how to do this.
Below is my code, everything runs fine except the last 5 lines."""

everyfive = ' '.join(word for i,word in enumerate(textInput.split()) if not i%5)

# or more succinctly
everyfive = ' '.join(textInput.split()[::5])

print(repr(everyfive))