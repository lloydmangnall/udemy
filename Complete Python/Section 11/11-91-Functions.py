# if you find yourself rewriting the same lines of code over and over again in a program,
# you should consider creating a new function and calling the function over and over.

# python function are created using the 'def' keyword
# def python_food():
#     width = 80
#     text = 'Spam and eggs'
#     left_margin = (width - len(text)) // 2
#     print(' ' * left_margin, text)

# call the python_food() function
# python_food()
# print(python_food())  # all python function return a value or 'None'

def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep  # convert integers to strings
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end, file=file, flush=flush)  # to make the function operate identical to print()
    return " " * left_margin + text

# with open('centered', mode='w') as centered_file:
#     center_text('spam and eggs', file=centered_file)
#     center_text('spam, spam and eggs', file=centered_file)
#     center_text(12, file=centered_file)
#     center_text('spam, spam, spam and eggs', file=centered_file)
#     center_text('first', 'second', 3, 4, 'spam', sep=":", file=centered_file)

# s1 = center_text('spam and eggs')
# print(s1)
# s2 = center_text('spam, spam and eggs')
# print(s2)
# s3 = center_text(12)
# print(s3)
# s4 = center_text('spam, spam, spam and eggs')
# print(s4)
# s5 = center_text('first', 'second', 3, 4, 'spam', sep=":")
# print(s5)

# print("=" + str(12 * 3))
# print(sorted(['b', 'd', 'c', 'a']))

# printing the centered text to a file
with open('menu', 'w') as menu:
    s1 = center_text('spam and eggs')
    print(s1, file=menu)
    s2 = center_text('spam, spam and eggs')
    print(s2, file=menu)
    print(center_text(12), file=menu)
    print(center_text('spam, spam, spam and eggs'), file=menu)
    s5 = center_text('first', 'second', 3, 4, 'spam', sep=":")
    print(s5, file=menu)
