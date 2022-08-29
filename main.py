# This is a sample Python script.
import easyocr


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    reader = easyocr.Reader(['de','en'], gpu=True)
    for i in range(1,271):
        print(reader.readtext("Dokument_46/Dokument_46-"+f'{i:03}'+".jpg"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
