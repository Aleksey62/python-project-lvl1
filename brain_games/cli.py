import prompt


name = prompt.string('May I know your name? ')


def welcome_user(name):
    print(f"Hello, {name}!")


welcome_user(name)