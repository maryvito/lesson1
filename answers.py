def get_answer(question):
    answers = {'привет': 'И тебе привет!',
        'как дела': 'Лучше всех', 
        'пока': 'Увидимся', }
    return answers.get(question)

def ask_user():
    try:
        while True:
            user_input = input("Скажи что-нибудь! ")
            print(get_answer(user_input))

            if user_input == "Пока!":
                print("Ну пока")
                break
    except KeyboardInterrupt:
        print("Пока!")
    




if __name__ == "__main__":
    ask_user()
