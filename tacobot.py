#!/usr/bin/python

import datetime
import os
import praw
import pytz
import yaml

def updatecss(rsub, conf):
    """Download, edit, and post a stylesheet."""
    # only (de)activate our block on the right day
    dow = getdow(conf["tz"])
    if dow == conf["days"][0]:
        print "tacoifying"
        oldcss = rsub.get_stylesheet()["stylesheet"]
        todays_css = tacoify(oldcss)
    elif dow == conf["days"][1]:
        print "detacoifying"
        oldcss = rsub.get_stylesheet()["stylesheet"]
        todays_css = untacoify(tacoify(oldcss))
    else:
        print "did nothing"
        return
    rsub.set_stylesheet(todays_css)

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
    # load configuration options from file beside ourself
    mypath = os.path.dirname(os.path.realpath(__file__))
    myconf = open(mypath + "/tacoconf.yaml", "r")
    conf = yaml.safe_load(myconf)
    myconf.close()

    # connect to reddit
    r = praw.Reddit(user_agent=conf["useragent"])
    r.config.decode_html_entities = True
    r.login(username=conf["username"], password=conf["password"])

    # check and change our list of subreddits
    for sub in conf["subs"]:
        rsub = r.get_subreddit(sub)
        updatecss(rsub, conf)
