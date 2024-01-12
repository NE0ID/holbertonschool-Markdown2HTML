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

def nextline(f, line):
    line = f.readline()
    return(line)

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
    count = 0
    while line:
        if "#" in line:
            h = parsing("#", line)
            newline = convert("#", line, "<h{}>".format(h), "</h{}>".format(h))
            new.write(newline)
        elif "-" in line:
            count = parsing("-", line)
            if count > 1:
                break
            if is_empty(check):
                new.write("<ul>\n")
                check.append("<ul>")
            if is_empty(check) is False:
                newline = convert("-", line, "<li>"," </li>")
                new.write(newline)
                if not nextline(f, line) or "-" not in nextline(f, line):
                    new.write("</ul>\n")
                    check.pop(0)
        else:
            new.write("<p>")
            if "\n" in line:
                new.write("\n<br />\n")
            new.write(line)
            new.write("</p>")
        line = f.readline()
    exit (0) 
