#!/usr/bin/env python
# -*- coding: utf-8 -*-

#C:\my-python-modulesに配置


#絶対パス利用のため呼び出す
import io
import sys
import os
import twitter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

__version__ = '1.3.1'

# Consumer Key
CK = 'ここにConsumer Keyを書く'
# Consumer Secret
CS = 'ここにConsumer Secretを書く'
# Access Token
AT = 'ここにAccess Tokenを書く'
# Accesss Token Secert
AS = 'ここにAccesss Token Secertを書く'


MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')


#OAuthクラスのインスタンス
def setup_auth():
    if not os.path.exists(MY_TWITTER_CREDS):
        twitter.oauth_dance(
            "My App Name", CK, CS, MY_TWITTER_CREDS)

    oauth_token, oauth_secret = twitter.read_token_file(MY_TWITTER_CREDS)
    return twitter.OAuth(
        oauth_token, oauth_secret, CK, CS)


#Twitterクラスのインスタンス
def twitter_instance(**kwargs):
    return twitter.Twitter(auth=setup_auth(), **kwargs)


#TwitterStreamクラスのインスタンス
def twitter_stream(**kwargs):
    return twitter.TwitterStream(auth=setup_auth(), **kwargs)
