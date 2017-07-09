Tacobot
=======

The tacobot is a simple reddit bot for enabling special weekly CSS styles in a subreddit. Ideal if you celebrate, say, taco Tuesday.

Requirements
------------

 * [PRAW 4.0.0+](https://praw.readthedocs.io/en/latest/index.html)
 * [pytz](http://pytz.sourceforge.net/)
 * [ruamel.yaml](https://yaml.readthedocs.io/en/latest/index.html)

Setup
-----

Copy the example configurations to files called `praw.ini` and `sublist.yaml` (which are expected to be in the same directory as the bot), and edit at least the stuff in caps to suit your needs. Note that the `client_id` and `client_secret` values are obtained in your [account preferences](https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps). The account used must be a moderator with configuration privileges in the sub(s) given, and the time zone should be a name from the [IANA database](http://www.iana.org/time-zones).

Usage
-----

Add the desired special CSS to your stylesheet, enclosed by Tacobot delimiters, like so:

    START-TACOS{color:red}
    #header { background-color: green !important; }
    END-TACOS{color:red}

Preview to make sure it validates. Anything that does can be added between the delimiters. When it's good, comment out that section and save the stylesheet:

    /*START-TACOS{color:red}
    #header { background-color: green !important; }
    END-TACOS{color:red}*/

Multiple blocks placed in the stylesheet are functional. Tacobot will remove or add back the comment markers on its configured days. Note that the minimized form of the delimiters (no spaces/semicolons) is expected.

Run Tacobot from your crontab at midnight in the time zone you configured:

    0 8 * * * /home/me/tacobot/tacobot.py
