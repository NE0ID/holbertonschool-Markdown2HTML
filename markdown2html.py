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

def part_conv(c, line, tag1, tag2):
    check = []
    for i in line:
        if i == c:
            if is_empty(check):
                newline = line.replace(c, "")
                newline += tag1
                check.append(tag1)
            else:
                newline += tag2
        newline += i
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
    l = None
    while line:
        count = 0
        if "#" in line:
            if "<p>" in check:
                close(check, new)
            h = parsing("#", line)
            newline = convert("#", line, "<h{}>".format(h), "</h{}>".format(h))
            new.write(newline)

        elif "-" in line:
            if "<p>" in check:
                close(check, new)
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
            if "<p>" in check:
                close(check, new)
            count = parsing("*", line)
            if count > 1:
                break
            l = "*"
            if is_empty(check):
                new.write("<ol>\n")
                check.append("<ol>")
            newline = convert("*", line, "<li>"," </li>")
            new.write(newline)

        else:
            if "<p>" not in check:
                new.write("<p>")
                check.append("<p>")
            if "\n" in line:
                line = convert("\n", line, "\n<br />\n", "")
            if "**" in line:
                line = part_conv("**", line, "<b>"," </b>")

            if "__" in line :
                line = part_conv("__", line, "<em>"," </em>")
            new.write(line)

        line = f.readline()
        if is_empty(check) is False:
            if line == "":
                close(check, new)
            elif l != None and l not in line:
                close(check, new)
    exit (0) 
