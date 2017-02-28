#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import io
import sys
import twitter
import os
import re    #正規表現ライブラリ
import urllib.request     #短縮URL展開用
from secret import twitter_instance

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pattern_violent = u".*馬鹿|バカ|阿保|アホ|あほ|死ね|氏ね|カス|クソ|キモい|ブス|殺す|雑魚|消えろ"

pattern_url = r"blog\.esuteru\.com|twitter\.com/htmk73([/?].*)?$|ja-jp\.facebook\.com/pages/%E3%81%AF%E3%81%A1%E3%81%BE%E8%B5%B7%E7%A8%BF/131806350359370|ch\.esuteru\.com|www\.youtube\.com/user/hatimaki73/|blog\.esuteru\.com\.2-t\.jp|jin115\.com|twitter\.com/jin115([/?].*)?$|yaraon-blog\.com|twitter\.com/yarare_kanrinin([/?].*)?$|hamusoku\.com|twitter\.com/hamusoku([/?].*)?$|blog\.livedoor\.jp/insidears/‎|twitter\.com/news_vip_blog‎([/?].*)?$|blog\.livedoor\.jp/dqnplus|twitter\.com/2chdqnplus([/?].*)?$|alfalfalfa\.com|twitter\.com/alfalfafafa([/?].*)?$|pokemon-matome\.net|twitter\.com/matome_pokemon([/?].*)?$|damage0\.blomaga\.jp|twitter\.com/damagezero([/?].*)?$|yusaani\.com|twitter\.com/yusa_yusaani([/?].*)?$|otakomu\.jp|twitter\.com/otakomu([/?].*)?$|^https?://matome\.naver\.jp|girlschannel\.net|ameblo\.jp/seek202/‎|^https?://ln\.is|matomatome\.jp|hosyusokuhou\.jp|lite-ra\.com|cinesoku\.net|otapol\.jp|www\.akb48matomemory\.com|big-celeb\.jp|healthpress\.jp|tocana\.jp|mess-y\.com|biz-journal\.jp|www\.premiumcyzo\.com|www\.menscyzo\.com|www\.cyzowoman\.com|www\.cyzo\.com"

#ツイート内に攻撃的な発言が含まれているか
def violent_search1(name, text):
    matchOB = re.search(pattern_violent, text)
    if matchOB is not None:
        statuses = tw.statuses.user_timeline(
            screen_name = name,
            count = 200,
            exclude_replies = False,
            include_rts = False,)
        for stat in statuses:
            violent_search2(name, stat["text"])
            cnt = 0
            if violent_search2 == 1:
                cnt += 1
                #3回攻撃的な発言を検出したら書き出し
                if cnt >= 1:
                    fout.writelines("@" + name + ", " + u"攻撃的な発言 https://twitter.com/" + name + "\r")
   
            
def violent_search2(name,text):
    matchOB = re.search(pattern_violent, text)
    if matchOB is not None:
        return 1
        

#ツイート内に信頼性の低いURLが含まれているか
def url_search(name, url):
    if url != "null":
        matchOB = re.search(pattern_violent, url)    #URLが見つからなかったらNoneTypeが入る
        if matchOB is not None:
            fout.writelines("@" + name + ", " + u"信頼性の低いURL https://twitter.com/" + name + "\r")
            

st1 = input(u"攻撃的な発言をするアカウントをリストアップしますか？ Y/N : ")
st2 = input(u"信頼性の低いURLを投稿するアカウントをリストアップしますか？ Y/N : ")
   
            
tw = twitter_instance()

#TL200件取得
statuses = tw.statuses.home_timeline(
    count = 200,
    trim_user = False,
    include_entities = True,
    exclude_replies = False,)


fout = open("result.txt", "w")


for stat1 in statuses:
    if st1 == "Y":
        violent_search1(stat1["user"]["screen_name"], stat1["text"])
        #短縮元URLの入っているentitiesはリストの中に辞書が入っている
    if st2 == "Y":
        entities = stat1["entities"]["urls"]
        for stat2 in entities:
            url_search(stat1["user"]["screen_name"], stat2["expanded_url"])

fout.close()
