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

def using_line(line1, line2):
    if is_empty(line2):
        return line1
    return line2

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
        newline = line
        if "*" in line:
            count = parsing("*", line)
            if count != 2:
                break
            newline = part_conv("**", newline, "<b>", "<b>")
        if "_" in line:
            count = parsing("_", line)
            if count != 2:
                break
            newline = part_conv("__", newline, "<em>", "<em>")
        if "#" in line:
            h = parsing("#", line)
            newline = convert("#", newline, "<h{}>".format(h), "</h{}>".format(h))
            new.write(newline)

        elif "-" in line:
            count = parsing("-", line)
            if count > 1:
                break
            l = "-"
            if is_empty(check):
                new.write("<ul>\n")
                check.append("<ul>")
            newline = convert("-", newline, "<li>"," </li>")
            new.write(newline)

        elif "*" in line:
            count = parsing("*", line)
            if count != 1:
                break
            l = "*"
            if is_empty(check):
                new.write("<ol>\n")
                check.append("<ol>")
            newline = convert("*", line, "<li>"," </li>")
            new.write(newline)
        else:
            if is_empty(check):
                new.write("<p>")
                check.append("<p>")
            new.write(newline)
        line = f.readline()
        if line[0].islower():
            new.write("<br/>")
        if is_empty(check) is False:
            if line == "":
                close(check, new)
            elif l != None and l not in line:
                close(check, new)
    exit (0)
