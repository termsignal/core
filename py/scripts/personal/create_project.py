import sys
import urllib.parse
import random
import base64
# import emoji module
import emoji
from emoji.core import emojize
import emojis


class addtoomni():
    def __init__(self) -> None:
        # addtoomni.request(self)
        pass

        # @classmethod
    def emojiz(self):
        emoji_alll = emojis.db.get_tags()
        random_emoji = random.choice(list(emoji_alll))
        choice = emoji.emojize(random_emoji)
        c = emojis.db.get_emojis_by_tag(choice)
        single = []
        for i in c:
            single.append(i)
        if len(single[0].emoji) > 1:
            addtoomni.emojiz(self)
        return single[0].emoji

    # @classmethod
    def request(self, em, title, chapter, body):
        project = "&project=" + em + urllib.parse.quote(title)
        action = "&name=" + \
            addtoomni.emojiz(self) + urllib.parse.quote(chapter)
        note = "&note=" + urllib.parse.quote(body)
        whole = project + action + note
        # print("omnifocus:///add?" + whole)
        return "omnifocus:///add?" + whole

    # if __name__ == '__main__':
    #     addtoomni()

# addtoomni()
