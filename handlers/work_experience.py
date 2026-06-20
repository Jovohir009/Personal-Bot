from utils.file_reader import read_file
from menus import work_menu, work_back_menu


def get_work_page():
    return {
        "text": "💼 Work Experience",
        "reply_markup": work_menu(),
    }


def get_vertex3d_page():
    return {
        "text": read_file("work/vertex3d.txt"),
        "reply_markup": work_back_menu(),
    }


def get_alifuz_page():
    return {
        "text": read_file("work/alifuz.txt"),
        "reply_markup": work_back_menu(),
    }


def get_freelance_page():
    return {
        "text": read_file("work/freelance.txt"),
        "reply_markup": work_back_menu(),
    }
