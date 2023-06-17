from src.keyboard import KeyBoard

if __name__ == '__main__':
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    print(kb.language)
    print(kb.language)
    kb.change_lang()
    print(kb.language)
    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    print(kb.language)
