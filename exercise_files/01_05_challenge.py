#
## Python Essential Training (Ryan Mitchell) Chapter #1 Challenge
#

#
## Assignment: read the documentation on the termcolor library and experiment
## with "Hello, World!"
#

from ast import Index
import sys

from termcolor import colored, cprint

# text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
# print(text)
# cprint("Hello, World!", "green", "on_red")

# print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
# print_red_on_cyan("Hello, World!")
# print_red_on_cyan("Hello, Universe!")

# for i in range(10):
#     cprint(i, "magenta", end=" ")

# cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)

# # print(type(text))
# print("\n\n\n\n")

# text = colored("Hello, ", "red", attrs=["bold"])
# text += colored("World!", "blue", attrs=["underline"])
# # print(type(text))
# print(text)


# string = "Hello, World!"
# text = ""
# colours = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
# t_attr = "bold"
# index = 0

# # print(colours[0])
# # print(len(colours))

# for c in string:
#     text += colored(c, colours[index], attrs=[t_attr])
#     if index < len(colours) - 1:
#         index += 1
#     else:
#         index = 0
#     match t_attr:
#         case "bold":
#             t_attr = "underline"
#         case "underline":
#             t_attr = "blink"
#         case "blink":
#             t_attr = "bold"

# print(text)


def colorise(string):
    text = ""
    colours = ('grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
    t_attr = ('bold', 'underline', 'blink')
    a_index = 0
    c_index = 0

    for c in string:
        text += colored(c, colours[c_index], attrs=[t_attr[a_index]])
        
        if a_index < len(t_attr) -1:
            a_index += 1
        else:
            a_index = 0
        
        if c_index < len(colours) - 1:
            c_index += 1
        else:
            c_index = 0
        
    return text

print(colorise("Hello, World!"))
print(colorise("Python is Hard!"))
