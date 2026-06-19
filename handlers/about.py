# handlers/about.py

from utils.file_reader import read_file
from menus import about_menu, main_menu


def get_about_page():
    return {"text": read_file("about.txt"), "reply_markup": about_menu()}


def get_cv_page():
    cv_link = read_file("cv_link.txt").strip()

    return {
        "text": "📄 View My CV",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "📄 Open CV", "url": cv_link}],
                [{"text": "⬅ Back", "callback_data": "about"}],
            ]
        },
    }


def get_main_page():
    return {
        "text": "👋 Welcome to Artificial Support Bot!\n\nExplore my profile, projects and experience.",
        "reply_markup": main_menu(),
    }
