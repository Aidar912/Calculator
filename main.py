import pygame
import pygame_gui
import math

pygame.init()

# Настройки экрана
window_size = (580, 700)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Калькулятор')

background_color = (255, 255, 255)
button_color = (100, 180, 255)
text_color = (255, 255, 255)
operation_button_color = (0, 0, 255)
control_button_color = (252, 4, 4)
special_button_color = (255, 255, 0)


manager = pygame_gui.UIManager(window_size, 'theme.json')

buttons = [
    {"text": "7", "pos": (50, 200), "type": "digit"}, {"text": "8", "pos": (150, 200), "type": "digit"}, {"text": "9", "pos": (250, 200), "type": "digit"},
    {"text": "+", "pos": (350, 200), "type": "operation"}, {"text": "%", "pos": (450, 200), "type": "operation"},
    {"text": "4", "pos": (50, 300), "type": "digit"}, {"text": "5", "pos": (150, 300), "type": "digit"}, {"text": "6", "pos": (250, 300), "type": "digit"},
    {"text": "-", "pos": (350, 300), "type": "operation"}, {"text": "√", "pos": (450, 300), "type": "special"},
    {"text": "1", "pos": (50, 400), "type": "digit"}, {"text": "2", "pos": (150, 400), "type": "digit"}, {"text": "3", "pos": (250, 400), "type": "digit"},
    {"text": "*", "pos": (350, 400), "type": "operation"}, {"text": "^", "pos": (450, 400), "type": "special"},
    {"text": "C", "pos": (50, 500), "type": "control"}, {"text": "0", "pos": (150, 500), "type": "digit"}, {"text": "=", "pos": (250, 500), "type": "control"},
    {"text": "/", "pos": (350, 500), "type": "operation"}, {"text": "(", "pos": (450, 500), "type": "operation"},
    {"text": ")", "pos": (50, 600), "type": "operation"}, {"text": ".", "pos": (150, 600), "type": "digit"}, {"text": "<-", "pos": (450, 600), "type": "control"}
]

input_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50, 100), (380, 50)), manager=manager)
input_box.set_text('')

clock = pygame.time.Clock()
is_running = True




while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                x, y, w, h = button['pos'][0], button['pos'][1], 80, 80
                if x <= event.pos[0] <= x + w and y <= event.pos[1] <= y + h:
                    current_text = input_box.get_text()
                    if button['text'] == 'C':
                        input_box.set_text('')
                    elif button['text'] == '=':
                        try:
                            # Обработка ввода для вычисления результата
                            result = str(eval(current_text))
                            input_box.set_text(result)
                        except Exception as e:
                            input_box.set_text('Error')
                    elif button['text'] == '%':
                        try:
                            input_box.set_text(current_text + '%')
                            current_text = input_box.get_text()
                            current_text = current_text.replace('%', '/100')

                            result = str(eval(current_text))
                            input_box.set_text(result)
                        except Exception as e:
                            input_box.set_text('Error')
                    elif button['text'] == '<-':
                            current_text = input_box.get_text()[:-1]
                            input_box.set_text(current_text)

                    elif button['text'] == '√':
                        input_box.set_text(current_text + 'math.sqrt(')
                    else:
                        input_box.set_text(current_text + button['text'])

        manager.update(time_delta)

    window.fill(background_color)
    manager.draw_ui(window)

    for button in buttons:
        # Выбор цвета кнопки на основе ее типа

        if button["type"] == "operation":
            button_color = operation_button_color
        elif button["type"] == "control":
            button_color = control_button_color
        elif button["type"] == 'special':
            button_color = special_button_color
        else:
            button_color = (200, 200, 200)  # Дефолтный цвет для неопределенных типов

        # Отрисовка кнопки с выбранным цветом
        pygame.draw.rect(window, button_color, (button['pos'][0], button['pos'][1], 80, 80))
        font = pygame.font.Font(None, 36)
        text = font.render(button['text'], True, text_color)
        window.blit(text, (button['pos'][0] + 20, button['pos'][1] + 20))

    pygame.display.update()

pygame.quit()
