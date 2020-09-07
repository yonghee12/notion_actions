from _config import *


def send_slack(client, channel, message):
    response = client.chat_postMessage(channel=SLACK_CHANNELS.get(channel), text=message)
    assert response["ok"]
