# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:
import os
path = os.getcwd() + '/Psets/ps5'
os.chdir(path)

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime, tzinfo
import pytz

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

#  : NewsStory
class NewsStory(object):
    # Initializing the class
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    # Creating getter functions
    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
        
    def get_link(self):
        return self.link
        
    def get_pubdate(self):
        return self.pubdate

    

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError
    
# PHRASE TRIGGERS

# Creating dictionary of punctuation for constant time lookup
punc = {}
for p in string.punctuation:
    punc[p] = True
# Function that checks for punctuation
def ispunc(char):
    try:
        return punc[char]
    except(KeyError):
        return False

    
# Problem 2
#  : PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        text = ''
        # looping over the string once to check for punc and lowering  char
        for c in phrase:
            if not ispunc(c):
                text += c.lower() 
        self.phrase = text

    def is_phrase_in(self, text):
        # Lowering text and spliting by phrase to get list
        phrase = ''
        # looping over the string once to check for punc and lowering  char
        for c in text:
            if ispunc(c):
                phrase += ' '
            else:
                phrase += c.lower() 
        # Collapsing whitespace
        phrase = ' '.join(phrase.split())
        # Spliting list by phrase
        ls = phrase.split(self.phrase)

        # Checking phrase is in list and contains the word without any leading/trailing char
        if len(ls) > 1:
            for pair in range(0, len(ls), 2):
                    # if valid string then it takes the ls value else it takes a space
                    i1 = ls[pair][-1:] if len(ls[pair]) > 1 else ' '
                    i2 = ls[pair + 1][0] if len(ls[pair + 1]) > 1 else ' '
            if i1 == ' ' and i2 == ' ':
                return True
        return False

    # Defining print function for error checking
    def __str__(self):
        return self.phrase

# Problem 3
#  : TitleTrigger
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
#  : DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, pubtime):
        pubtime = datetime.strptime(pubtime, '%d %b %Y %H:%M:%S').replace(tzinfo=pytz.timezone("EST"))
        pubtime = pubtime.replace(tzinfo = pytz.timezone("EST"))
        self.pubtime = pubtime


# Problem 6
#  : BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, time):
        return self.pubtime > time.get_pubdate().replace(tzinfo = pytz.timezone("EST"))

class AfterTrigger(TimeTrigger):
    def evaluate(self, time):
        return self.pubtime < time.get_pubdate().replace(tzinfo = pytz.timezone("EST"))


# COMPOSITE TRIGGERS

# Problem 7
#  : NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trig = trigger

    # This evaluate function uses evaluate function of object type being passed in
    def evaluate(self,  story):
        return not self.trig.evaluate(story)

# Problem 8
#  : AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trig1 = trigger1
        self.trig2 = trigger2

    # This evaluate function uses evaluate function of object type being passed in
    def evaluate(self, story):
        return self.trig1.evaluate(story) and self.trig2.evaluate(story)

# Problem 9
#  : OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trig1 = trigger1
        self.trig2 = trigger2

    # This evaluate function uses evaluate function of object type being passed in
    def evaluate(self, story):
        return self.trig1.evaluate(story) or self.trig2.evaluate(story)



#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # Problem 10
    my_stories = []

    for s in stories:
        for t in triggerlist:
            if t.evaluate(s):
                my_stories.append(s)
                break

    return my_stories

val_trigs = {
    'TITLE': (1, TitleTrigger),
    'DESCRIPTION': (1, DescriptionTrigger),
    'AFTER': (1, AfterTrigger),
    'BEFORE': (1, BeforeTrigger),
    'NOT': (1, NotTrigger),
    'AND': (2, AndTrigger),
    'OR': (2, OrTrigger)
}
#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    trigger_dict = {}
    trigger_list = []

    def triggerList(line):
        # Initializing variables for readability
        action = line[0]
        keyword = line[1]
        # Appending added trigger to the trigger list for ADD lines
        if action == 'ADD':
            for i in range(1, len(line)):
                trigger_list.append(trigger_dict[line[i]])
        # Appending new triggers to trigger dict
        else:
            # Checking trigger def is valid
            if val_trigs.get(keyword) is not None:
                # creating a opject for the type of trig and adding to dict
                if val_trigs.get(keyword)[0] == 1:
                    trigger_dict[action] = val_trigs.get(keyword)[1](line[2])
                else:
                    trigger_dict[action] = val_trigs.get(keyword)[1](line[2], line[3])

    for line in lines:
        trig = line.split(',')
        triggerList(trig)
    
    return trigger_list

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Nba")
        t2 = DescriptionTrigger("Suns")
        t3 = DescriptionTrigger("Giannis")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        triggerlist = read_trigger_config('triggers.txt')
        print(triggerlist)
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

           # print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

