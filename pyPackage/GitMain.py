import json
import os
from datetime import datetime

COMMIT_MESSGE = datetime.today().strftime("Interest Update : %Y/%m/%d/%H:%M")


def add():
    os.system("git add about/interest.md")


def commit():
    os.system(f"""git commit -m \"{COMMIT_MESSGE}\"   """)


def push():
    os.system("git push")
