import os

from dotenv import load_dotenv
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('YOUR_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('YOUR_CHANNEL_SECRET'))

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def generate_response(prompt, role="user"):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative "
                        "flair."},
            # {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    msg_from_system = generate_response(msg_from_user)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg_from_system)
    )


if __name__ == "__main__":
    app.run(debug=True)
