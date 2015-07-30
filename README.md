Tacobot
=======

The tacobot is a simple reddit bot for enabling special weekly CSS styles in a subreddit. Ideal if you celebrate, say, taco Tuesday.

Requirements
------------

 * [PRAW](https://praw.readthedocs.org/)
 * [pytz](http://pytz.sourceforge.net/)
 * [PyYAML](http://pyyaml.org/)

Setup
-----

Copy the example configuration to a file called `tacoconf.yaml` (which is expected to be in the same directory as the bot), and edit at least the stuff in caps to suit your needs. The account used must be a moderator with configuration privileges in the sub(s) given, and the time zone should be a name from the [IANA database](http://www.iana.org/time-zones).

The tacobot optionally supports PRAW's [praw-multiprocess](http://praw.readthedocs.org/en/latest/pages/multiprocess.html) program. Set `multiprocess` to `true` in the configuration to enable this functionality.

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
