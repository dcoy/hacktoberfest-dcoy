#!usr/bin/env python
#-*- coding: utf-8 -*-

class Meeseeks(object):
    def __init__(self):
        self.live()

    def live(self):
        print "I'm Mr. Meeseeks, Look at me!"

class MeeseeksBox(object):
    def click(self):
        meeseeks = Meeseeks()

if __name__ == '__main__':
    meeseeksbox = MeeseeksBox()
    meeseeksbox.click()
