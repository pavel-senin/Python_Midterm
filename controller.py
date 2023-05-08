import function as f
import ui


def run():
    input_from_user = ''
    while input_from_user != '5':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            f.show()
        if input_from_user == '2':
            f.add()
        if input_from_user == '3':
            f.show()
            f.delete()
        if input_from_user == '4':
            f.show()
            f.edit()
        if input_from_user == '5':
            ui.goodbuy()
            break