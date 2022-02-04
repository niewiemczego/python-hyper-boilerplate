from colored import fg, bg, attr

def log_color(text: str, user_color: str) -> str:
    return fg(user_color) + f"{text}" + attr('reset')

def color(text: str) -> str:
    return fg("#7a6e96") + f"{text}" + attr('reset')

def info_log(text: str, basic_info: bool = True):
    if basic_info:
        print(f'[{color("python-bot-hyper-boilerplate")}] {log_color(text, 11)}')
    else:
        print(f'[{color("python-bot-hyper-boilerplate")}] {log_color(text, 24)}')

def success_log(text: str):
    print(f'[{color("python-bot-hyper-boilerplate")}] {log_color(text, 40)}')

def error_log(text: str):
    print(f'[{color("python-bot-hyper-boilerplate")}] {log_color(text, 9)}')
