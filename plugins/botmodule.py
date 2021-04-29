from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

import MeCab
import pandas as pd
import re

@listen_to(r'.*')
def reply_bkb(message):
    TEXT = message.body['text']
    m = MeCab.Tagger()
    node = m.parseToNode(TEXT)
    raws = []
    features = []
    while node:
        try:
            feature = node.feature.split(',')[9]
        except IndexError:
            feature = node.surface.split(',')[0]
        raw = node.surface.split(',')[0]
        if feature != "*":
            features.append(feature)
            raws.append(raw)

        node = node.next

    print(features)

    features2 = []
    for feature in features:
        try feature[0]:
            if feature[0] in {"バ", "ビ", "ブ", "ベ", "ボ", "B", "b"}:
                tmp="B"
            elif feature[0] in {"カ", "キ", "ク", "ケ", "コ", "K", "k"}:
                tmp="K"
            else:
                tmp="O"

        except IndexError:
            tmp="O"
            
        features2.append(tmp)

    features2 = "".join(features2)

    p_bkb = re.compile(r'.*?B.{0,3}?K.{0,3}?B.*?')
    if p_bkb.match(features2):
        b1 = re.compile(r'.*?(B.{0,3}?)K.{0,3}?B.*?').match(features2).span(1)
        k1 = re.compile(r'.*?B.{0,3}?(K.{0,3}?)B.*?').match(features2).span(1)
        b2 = re.compile(r'.*?B.{0,3}?K.{0,3}?(B).*?').match(features2).span(1)

        b1_text = "".join(raws[b1[0]:b1[1]])
        k1_text = "".join(raws[k1[0]:k1[1]])
        b2_text = "".join(raws[b2[0]:b2[1]])

        message.reply("\n{}！\n{}！\n{}！\n\nBKB！ヒィア！！".format(b1_text, k1_text, b2_text))

    else:
        pass

# @respond_to(r'.*')
# def auto_reply(message):

# import MeCab
# mecab = MeCab.Tagger()
# text = "bkbと馬鹿！"
# node = mecab.parseToNode(text)
# features = []
# while node:
#     try:
#         feature = node.feature.split(',')[9]
#     except IndexError:
#         feature = node.surface.split(',')[0]
#     raw = node.surface.split(',')[0]
#     if feature != "*":
#         features.append(feature)
#
#     node = node.next
#
# print(features)
