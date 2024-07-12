import requests
import os

def send_line_notify(message, token):
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': message}
    requests.post(line_notify_api, headers=headers, data=data)

if __name__ == "__main__":
    import sys
    token = os.getenv('LINE_NOTIFY_TOKEN')
    message = sys.argv[1]
    send_line_notify(message, token)


"""
Pythonで細かいとこ記述するなら
import requests
import os
from datetime import datetime

def send_line_notify(message, token):
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': message}
    requests.post(line_notify_api, headers=headers, data=data)

def main():
    token = os.getenv('LINE_NOTIFY_TOKEN')
    now = datetime.now()
    message_schedule = {
        20: 'Atcoderのコンテストまであと1時間です。',
        20.5: 'Atcoderのコンテストまであと30分です。',
        20.75: 'Atcoderのコンテストまであと15分です。',
        20.8333: 'Atcoderのコンテストまであと10分です。',
        20.9167: 'Atcoderのコンテストまであと5分です。'
    }

    for key, message in message_schedule.items():
        if now.hour + now.minute / 60 == key:
            send_line_notify(message, token)
            break

if __name__ == "__main__":
    main()

"""