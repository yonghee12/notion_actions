from datetime import datetime as dt
from config import *
from direct_redis import DirectRedis
from notion.client import NotionClient
import time
from slack_util import *


notion = NotionClient(token_v2=NOTION_AUTH_TOKEN_V2)
slack = SlackClient(SLACK_API_TOKEN, channel='notionbot_test')

table = notion.get_collection_view('https://www.notion.so/ryencatchers/9203baefcf1f491aab32d05bfcf0db90?v=9b8901b0915243a4957673ece8a4a83a')
rows = table.collection.get_rows()
row = rows[0]
row.__dir__()
row.get_all_properties()
row.damdangjahwagin
date = row.hyugail

def get_date_msg(date):
    return f"{date.year}년 {date.month}월 {date.day}일"

for row in rows:
    if row.damdangjahwagin:
        name, start, end = row.title, row.hyugail.start, row.hyugail.end
        header = f"{name}님의 휴가일은 {get_date_msg(start)}"
        footer = f"입니다." if end is None else f"부터 {get_date_msg(end)}까지입니다."
        slack.send(header + footer)