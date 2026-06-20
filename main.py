# main.py

from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os

from utils.telegram import telegram_request

from handlers.about import get_about_page, get_cv_page, get_main_page

from handlers.projects import (
    get_projects_page,
    get_mrms_page,
    get_ims_page,
    get_car_rental_page,
    get_github_page,
    get_portfolio_page,
)

from handlers.work_experience import (
    get_work_page,
    get_vertex3d_page,
    get_alifuz_page,
    get_freelance_page,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Artificial Support Bot Running"}


def edit_message(chat_id, message_id, page):
    telegram_request(
        BOT_TOKEN,
        "editMessageText",
        {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": page["text"],
            "reply_markup": page["reply_markup"],
        },
    )


@app.post("/webhook")
async def telegram_webhook(request: Request):

    data = await request.json()

    print(data)

    # CALLBACK BUTTONS
    if "callback_query" in data:

        callback_query = data["callback_query"]

        callback_id = callback_query["id"]
        callback_data = callback_query["data"]

        chat_id = callback_query["message"]["chat"]["id"]
        message_id = callback_query["message"]["message_id"]

        telegram_request(
            BOT_TOKEN, "answerCallbackQuery", {"callback_query_id": callback_id}
        )

        # ABOUT

        if callback_data == "about":
            edit_message(chat_id, message_id, get_about_page())

        elif callback_data == "show_cv":
            edit_message(chat_id, message_id, get_cv_page())

        # WORK EXPERIENCE

        elif callback_data == "work_experience":
            edit_message(chat_id, message_id, get_work_page())

        elif callback_data == "work_vertex3d":
            edit_message(chat_id, message_id, get_vertex3d_page())

        elif callback_data == "work_alifuz":
            edit_message(chat_id, message_id, get_alifuz_page())

        elif callback_data == "work_freelance":
            edit_message(chat_id, message_id, get_freelance_page())

        elif callback_data == "back_work":
            edit_message(chat_id, message_id, get_work_page())

        # PROJECTS

        elif callback_data == "projects":
            edit_message(chat_id, message_id, get_projects_page())

        elif callback_data == "project_mrms":
            edit_message(chat_id, message_id, get_mrms_page())

        elif callback_data == "project_ims":
            edit_message(chat_id, message_id, get_ims_page())

        elif callback_data == "project_car_rental":
            edit_message(chat_id, message_id, get_car_rental_page())

        elif callback_data == "github":
            edit_message(chat_id, message_id, get_github_page())

        elif callback_data == "portfolio":
            edit_message(chat_id, message_id, get_portfolio_page())

        elif callback_data == "back_projects":
            edit_message(chat_id, message_id, get_projects_page())

        # GLOBAL BACK

        elif callback_data == "back_main":
            edit_message(chat_id, message_id, get_main_page())

        return {"status": "ok"}

    # NORMAL MESSAGES

    if "message" in data:

        chat_id = data["message"]["chat"]["id"]

        telegram_request(
            BOT_TOKEN,
            "sendMessage",
            {
                "chat_id": chat_id,
                "text": get_main_page()["text"],
                "reply_markup": get_main_page()["reply_markup"],
            },
        )

    return {"status": "ok"}
