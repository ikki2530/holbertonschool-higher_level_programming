#!/usr/bin/python3


def text_indentation(text):
    delims = "?.:"
    for c in delims:
        text = str(c + '&\n\n').join(s.strip() for s in text.split(c))
        #for s in text.split(c):
            #print(s.strip())
        #print("---"*20)
        print(text)
        print("----"*20)
