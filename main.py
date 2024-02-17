import pygame
import pygame_gui
import math

pygame.init()

# Настройки экрана
window_size = (580, 700)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Калькулятор')

background_color = (30, 30, 30)
button_color = (45, 45, 45)
text_color = (255, 255, 255)
operation_button_color = (70, 130, 180)
control_button_color = (220, 20, 60)
special_button_color = (255, 215, 0)


manager = pygame_gui.UIManager(window_size, 'theme.json')
button_positions = [(x, y) for y in range(200, 601, 100) for x in range(50, 451, 100)]
button_texts = [
    "7", "8", "9", "+", "%",
    "4", "5", "6", "-", "√",
    "1", "2", "3", "*", "^",
    "C", "0", "=", "/", "(",
    ")", ".", "<-"
]
button_types = [
    "digit", "digit", "digit", "operation", "operation",
    "digit", "digit", "digit", "operation", "special",
    "digit", "digit", "digit", "operation", "special",
    "control", "digit", "control", "operation", "operation",
    "operation", "digit", "control"
]

buttons = [{"text": text, "pos": pos, "type": btype} for text, pos, btype in zip(button_texts, button_positions, button_types)]

input_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50, 100), (480, 50)), manager=manager)
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
            button_color = (200, 200, 200)

        # Отрисовка кнопки с выбранным цветом
        pygame.draw.rect(window, button_color, (button['pos'][0], button['pos'][1], 80, 80))
        font = pygame.font.Font(None, 36)
        text = font.render(button['text'], True, text_color)
        window.blit(text, (button['pos'][0] + 20, button['pos'][1] + 20))

    pygame.display.update()

pygame.quit()
