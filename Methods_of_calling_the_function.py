def send_email(message, recipient, *, sender="university.help@gmail.com"):
    valid_endings = (".com", ".ru", ".net")
    if "@" not in sender or not sender.endswith(valid_endings) or \
            "@" not in recipient or not recipient.endswith(valid_endings):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email("Привет, как дела?", "student@gmail.com")

send_email("Тестовое сообщение", "student@gmail")

send_email("Тест", "university.help@gmail.com")

send_email("Уведомление", "recipient@mail.com", sender="custom.sender@example.com")

