from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class CalculatorApp(App):
    def build(self):
        self.operators = set(['+', '-', '*', '/', 'sin', 'cos', 'tan', 'log'])
        self.last_was_operator = None

        self.layout = BoxLayout(orientation='vertical')

        self.result = TextInput(font_size=55, readonly=True, halign='right', multiline=False)
        self.layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+'],
            ['sin', 'cos', 'tan', 'log']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.layout.add_widget(h_layout)

        return self.layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        elif button_text == '=':
            try:
                self.result.text = str(eval(current))  # Simple eval for calculations
            except Exception as e:
                self.result.text = 'Error'
        elif button_text in self.operators:
            if current and (self.last_was_operator or current[-1] in self.operators):
                return
            if button_text in ['sin', 'cos', 'tan', 'log']:
                self.result.text = str(eval(f"math.{button_text}({current})"))  # Call math functions
            else:
                self.result.text += button_text
            self.last_was_operator = True
        else:
            self.result.text += button_text
            self.last_was_operator = False

if __name__ == '__main__':
    CalculatorApp().run()