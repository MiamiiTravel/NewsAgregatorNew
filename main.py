from random import random
from vk_api import VkApi



def write_msg(user_id, message=None, keyboard=None):
    vk.method('messages.send', {'user_id': user_id,
                                'random_id': random(),
                                'message': message,
                                'keyboard': keyboard})


def create_keybard(button_type='main_menu', labels=None):
    keyboard = VkKeyboard(one_time=True)
    if button_type == 'main_menu':
        keyboard.add_button(label='Новости', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(label='Управление подписками', color=VkKeyboardColor.PRIMARY)

    elif button_type == 'menu_subscriptions':
        keyboard.add_button(label='Категории', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button(label='Ключевые слова', color=VkKeyboardColor.DEFAULT)

    elif button_type == 'menu_category':
        keyboard.add_button(label='Добавить категорию', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button(label='Удалить категорию', color=VkKeyboardColor.NEGATIVE)

    elif button_type == 'menu_keyword':
        keyboard.add_button(label='Добавить ключевое слово', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button(label='Удалить', color=VkKeyboardColor.NEGATIVE)

    elif button_type == 'send_news':
        keyboard.add_button(label='Получить новости', color=VkKeyboardColor.POSITIVE)

    elif button_type == 'menu_back':
        keyboard.add_button(label='Назад', color=VkKeyboardColor.DEFAULT)

    elif button_type == 'mode':
        for label in range(len(labels)):
            if label <= 2:
                keyboard.add_button(label=labels[label], color=VkKeyboardColor.DEFAULT)
            elif label % 3 == 0:
                keyboard.add_line()
                keyboard.add_button(label=labels[label], color=VkKeyboardColor.DEFAULT)
            else:
                keyboard.add_button(label=labels[label], color=VkKeyboardColor.DEFAULT)

    return keyboard.get_keyboard()


def user(user_id):
    return vk.method('users.get', {'user_ids': user_id, 'fields': 'city'})


KEY = '-'
vk = VkApi(token=KEY)
longpoll = VkLongPoll(vk)


