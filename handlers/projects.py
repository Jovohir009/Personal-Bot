# handlers/projects.py

from utils.file_reader import read_file
from menus import projects_menu, project_back_menu


def get_projects_page():
    return {"text": "🚀 My Projects", "reply_markup": projects_menu()}


def get_mrms_page():
    return {
        "text": read_file("projects/project_mrms.txt"),
        "reply_markup": project_back_menu(),
    }


def get_ims_page():
    return {
        "text": read_file("projects/project_ims.txt"),
        "reply_markup": project_back_menu(),
    }


def get_car_rental_page():
    return {
        "text": read_file("projects/project_car_rental.txt"),
        "reply_markup": project_back_menu(),
    }


def get_github_page():
    github_url = read_file("github.txt").strip()

    return {
        "text": "💻 GitHub Profile",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "Open GitHub", "url": github_url}],
                [{"text": "⬅ Back", "callback_data": "projects"}],
            ]
        },
    }


def get_portfolio_page():
    portfolio_url = read_file("portfolio.txt").strip()

    if portfolio_url.lower() == "coming soon":
        return {
            "text": "🌐 Portfolio Website\n\nComing Soon 🚀",
            "reply_markup": project_back_menu(),
        }

    return {
        "text": "🌐 Portfolio Website",
        "reply_markup": {
            "inline_keyboard": [
                [{"text": "Open Portfolio", "url": portfolio_url}],
                [{"text": "⬅ Back", "callback_data": "projects"}],
            ]
        },
    }
