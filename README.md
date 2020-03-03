Project summary:
================

Web Comic Downloader is a simple python project to download webcomics from the internet. Currently, it supports [TwoKinds](http://twokinds.keenspot.com/) and [Harpy Gee](https://www.harpygee.com/).

The WCDL Project was completed in less than one day, and only had a few basic requirements:

*   **Modularity:** Support for additional comics could be added later.
*   **Non-redundant:** The program keeps track of the already downloaded pages, and only checks and downloads new ones.

How to use:
===========

1.  From a terminal, navigate to directory containing `main.py`.
2.  In the terminal type `python main.py`.
3.  If python is not installed, Windows will automatically open the windows store to install.

*   If you're not prompted, you can download Python [here](https://www.python.org/downloads/).
*   Remember to check 'Automatically add python to PATH'.

5.  You should now see a menu like this:  
    ![](/public-images/projects/wcdl/main.png)
6.  Entering `a` will download all current pages of Twokinds, and Harpy Gee (Well over 1000 pages).

Challenges:
===========

This project was originally planned to be short, but sweet in terms of creation, however, there were one or two challenges to be overcome.

Downloading Twokinds
--------------------

The Twokinds page directory was nice and simple. Each page could be found at a numbered directory e.g. `pages/1`, `pages/2`, etc...

This meant that all I had to do was store a page number, navigate to the page, and find the image URL.

This was working great until about page 800 or so when suddenly there were 2 images URLs. One for the actual page I needed, and another or the concept sketch for that page. Changing `find` to `rfind` was a nice easy solution to that problem.

All in all, Twokinds was a nice simple comic to download.

Harpy Gee
---------

Harpy Gee was not nearly as simple as Twokinds. The first problem, the page directories were structured unpredictably. Usually involving the chapter name or number, then the page name. This meant that on top of storing and managing the page number, I also needed to do the same for the page URL.

One Random Page was encoded in `latin-1` instead of `utf-8` which caused me to implement quite a messy try-catch statement to switch to `latin-1` encoding on error.

Known Bugs
==========

*   Reset Configuration does nothing
*   After downloading Harpy Gee, the next page-URL erroneously gets stored as The Hive Works privacy policy.
