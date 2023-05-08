import file_operation
import Note
import ui

number = 6  # сколько знаков ћ»Ќ»ћ”ћ может быть в тексте заметки


def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Note added')


def show():
    logic = True
    array = file_operation.read_file()
    for notes in array:
        logic = False
        print(Note.Note.map_note(notes))
    if logic == True:
        print('No note found')


def delete():
    id = input('Input id of the needed note: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            array.remove(notes)
            print('Note deleted')
    if logic == True:
        print('Note not found')
    file_operation.write_file(array, 'a')

def edit():
    id = input('Input id of the needed note: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic == False
            note = ui.create_note(number)
            Note.Note.set_title(notes, note.get_title())
            Note.Note.set_body(notes, note.get_body())
            Note.Note.set_date(notes)
            print('Note changed')
    if logic == True:
        print('Note not found')
    file_operation.write_file(array, 'a')