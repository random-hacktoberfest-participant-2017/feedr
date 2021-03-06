import sys
import feedparser

from colorama import init
from colorama import Back, Style, Fore


init(autoreset=True)


def rss_print(title, link, date, description, option):
    print(Back.RED + "Title:" + Style.RESET_ALL + " " + title)
    print(Back.YELLOW + "Date :" + Style.RESET_ALL + " " + date)
    print(Back.YELLOW + "Link :" + Style.RESET_ALL + " " + link)
    if option == 1:
        print(Back.YELLOW + "Description :" + Style.RESET_ALL + " " + description)


def get_rss(limit, option):
    """
    Get rss data from url,
    print single entry to show latest news, else give index number
    """
    rss_data = feedparser.parse(URL)
    try:
        for i in range(0, limit):
            title = rss_data.entries[i].title
            link = rss_data.entries[i].link
            date = rss_data.entries[i].published if 'published' in rss_data.entries[i] else ""
            description = rss_data.entries[i].description if 'description' in rss_data.entries[i] else ""
            print(Back.CYAN + str(i + 1) + "\t")
            rss_print(title, link, date, description, option)
    except:
        print(Fore.RED + """Either the feed is invalid, or
            the feed doesn't contain many titles.""")


def menu():
    print("""What do you wish to do now? \n1. Get the latest issue.
          \n2. Get the titles of the latest 5 issues.""")
    opt = int(raw_input('Option: '))
    if opt == 1:
        get_rss(1, 1)
    elif opt == 2:
        get_rss(5, 2)
    else:
        print("Not a valid choice")
        exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify some rss link")
    else:
        URL = sys.argv[1]
        menu()
