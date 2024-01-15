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
    elif op == "<p>":
        f.write("</p>\n")

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
        if "<p>" in check and "\n" in line:
                new.write("\n<br />\n")
        if "#" in line:
            if "<p>" in check:
                new.write("</p>")
                check.pop()
            h = parsing("#", line)
            newline = convert("#", line, "<h{}>".format(h), "</h{}>".format(h))
            new.write(newline)
        elif "-" in line:
            count = parsing("-", line)
            if count > 1:
                break
            if "<p>" in check:
                new.write("</p>")
                check.pop()
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
            if "<p>" in check:
                new.write("</p>")
                check.pop()
            l = "*"
            if is_empty(check):
                new.write("<ol>\n")
                check.append("<ol>")
            newline = convert("*", line, "<li>"," </li>")
            new.write(newline)
        elif "**" in line:
            if "<p>" in check:
                new.write("</p>")
                check.pop()
            newline = convert("**", line, "<b>"," </b>")
            new.write(newline)
        elif "__" in line :
            if "<p>" in check:
                new.write("</p>")
                check.pop()
            newline = convert("__", line, "<em>"," </em>")
            new.write(newline)
        elif "<p>" not in check:
            new.write("<p>")
            check.append("<p>")
        else:
            new.write(line)
        line = f.readline()
        if is_empty(check) is False:
            if line == "" or l not in line:
                close(check, new)
    exit (0) 
