#!/usr/bin/python3

""" 
    Markdown2HTML
"""
import sys
import os

def parsing(c, line):

    h = 0
    for i in line:
        if i == c:
            h += 1
        else:
            break
    return (h)

def convert(c, line, tag1, tag2):
    line = line.replace(c, "")
    line = line.replace("\n", "")
    newline = tag1
    newline += line
    newline += tag2
    newline += "\n"
    return newline

def close(stack, f):
    op = stack.pop()
    if op == "<ul>":
        f.write("</ul>\n")
    elif op == "<ol>":
        f.write("</ol>\n")

def is_empty(li):
    if li:
        return False
    return True

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print ("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit (1)
    elif os.path.exists(sys.argv[1]) == False:
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit (1)
    f = open(sys.argv[1], "r")
    new = open(sys.argv[2], "a")
    check = []

    line = f.readline()
    while line:
        count = 0
        if "#" in line:
            h = parsing("#", line)
            newline = convert("#", line, "<h{}>".format(h), "</h{}>".format(h))
            new.write(newline)
        elif "-" in line:
            count = parsing("-", line)
            if count > 1:
                break
            l = "-"
            if is_empty(check):
                new.write("<ul>\n")
                check.append("<ul>")
            newline = convert("-", line, "<li>"," </li>")
            new.write(newline)
        elif "*" in line:
            count = parsing("*", line)
            if count > 1:
                break
            l = "*"
            if is_empty(check):
                new.write("<ol>\n")
                check.append("<ol>")
            newline = convert("*", line, "<li>"," </li>")
            new.write(newline)
        elif "**" in line:
            count = parsing("*", line)
            if count < 2 or count > 2:
                break
            newline = convert("**", line, "<b>"," </b>")
            new.write(newline)
        else:
        #    new.write("<p>")
        #    if "\n" in line:
        #        new.write("\n<br />\n")
            new.write(line)
        #    new.write("</p>")
        line = f.readline()
        if is_empty(check) is False:
            if line == "" or l not in line:
                close(check, new)
    exit (0) 
