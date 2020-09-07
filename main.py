from _config import *
from direct_redis import DirectRedis
from notion.client import NotionClient
import time
import slack as slackmodule
from functions import *

slack = slackmodule.WebClient(token=SLACK_AUTH_TOKEN)
notion = NotionClient(token_v2=NOTION_AUTH_TOKEN_V2)

