from tools import get_current_time, roll_dice, generate_password, read_text_file


def execute_tool(user_input):
    text = user_input.lower()
    if "time" in text or "clock" in text:
        return get_current_time()
    if "dice" in text:
        return f"You rolled {roll_dice()}"
    if "password" in text:
        return generate_password()
    if "read file" in text:
        return read_text_file("data/notes.txt")
    return None
