# menus.py


def main_menu():
    return {
        "inline_keyboard": [
            [{"text": "👨 About Me", "callback_data": "about"}],
            [{"text": "🚀 Projects", "callback_data": "projects"}],
        ]
    }


def about_menu():
    return {
        "inline_keyboard": [
            [{"text": "📄 Open CV", "callback_data": "show_cv"}],
            [{"text": "⬅ Back", "callback_data": "back_main"}],
        ]
    }


def projects_menu():
    return {
        "inline_keyboard": [
            [{"text": "🏥 MRMS", "callback_data": "project_mrms"}],
            [{"text": "📦 IMS", "callback_data": "project_ims"}],
            [{"text": "🚗 Car Rental", "callback_data": "project_car_rental"}],
            [{"text": "💻 GitHub", "callback_data": "github"}],
            [{"text": "🌐 Portfolio", "callback_data": "portfolio"}],
            [{"text": "⬅ Back", "callback_data": "back_main"}],
        ]
    }


def project_back_menu():
    return {
        "inline_keyboard": [
            [{"text": "⬅ Back to Projects", "callback_data": "back_projects"}]
        ]
    }
