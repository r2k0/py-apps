#!/usr/bin/env python
import cli.app

@cli.app.CommandLineApp
def bm(app):
    pass

bm.add_param("-t","--tag",help="tag for bookmark",default=False,action="store_true")
bm.add_param("-l","--list",help="list all your bookmarks",default=False,action="store_true")
bm.add_param("-lt","--lstag",help="list all your tags",default=False,action="store_true")
bm.add_param("-s","--search",help="search for bookmark(s)",default=False,action="store_true")
bm.add_param("-st","--searchtag",help="search for bookmark(s) with specify tag",default=False,action="store_true")

if __name__ == "__main__":
    bm.run()
