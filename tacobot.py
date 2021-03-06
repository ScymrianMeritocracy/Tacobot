#!/usr/bin/python

import datetime
import os
import praw
import pytz
import ruamel.yaml

def updatecss(r, sub, conf):
    """Download, edit, and post a stylesheet."""
    # only (de)activate our block on the right day
    dow = getdow(conf["tz"])
    if dow == conf["days"][0]:
        page = r.subreddit(sub).wiki["config/stylesheet"]
        newcss = tacoify(page.content_md)
        page.edit(newcss, conf["reasons"][0])
    elif dow == conf["days"][1]:
        page = r.subreddit(sub).wiki["config/stylesheet"]
        newcss = untacoify(tacoify(page.content_md))
        page.edit(newcss, conf["reasons"][1])
    else:
        return

def getdow(tz):
    """Determine our dow, based on the given timezone."""
    # list mapping each dow to a name
    weekdays = [ "Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday" ]
    gmtnow = datetime.datetime.now(pytz.utc)
    mynow = gmtnow.astimezone(pytz.timezone(tz))
    return weekdays[mynow.weekday()]

def tacoify(css):
    """Uncomment our special block of CSS."""
    css = css.replace("/*START-TACOS{color:red}", "START-TACOS{color:red}")
    css = css.replace("END-TACOS{color:red}*/", "END-TACOS{color:red}")
    return css

def untacoify(css):
    """Comment out our special block of CSS."""
    css = css.replace("START-TACOS{color:red}", "/*START-TACOS{color:red}")
    css = css.replace("END-TACOS{color:red}", "END-TACOS{color:red}*/")
    return css

if __name__ == "__main__":
    # load subreddit options from file beside ourself
    mypath = os.path.dirname(os.path.realpath(__file__))
    myconf = open(mypath + "/sublist.yaml", "r")
    conf = ruamel.yaml.safe_load(myconf)
    myconf.close()

    # connect to reddit
    r = praw.Reddit()

    # check and change our list of subreddits
    for sub in conf["subs"]:
        updatecss(r, sub, conf)
