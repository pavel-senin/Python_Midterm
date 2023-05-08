import Note


def create_note(number):
    title = check_len_text_input(
        input('Input name of the note: '), number)
    body = check_len_text_input(
        input('Input description: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nNotes. Functions:\n\n1 - output all notes\n2 - add note\n3 - delete note\n4 - edit note\n5 - exit\n\nInput number of function: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Text length must be longer than {n} symbols\n')
        text = input('Input text: ')
    else:
        return text


def goodbuy():
    print("Program finished")