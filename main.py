from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

# Groq AI kaliti va manzili
API_KEY = "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"
URL = "https://api.groq.com/openai/v1/chat/completions"

class JarvisCore(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        
        # Chat oynasi
        self.scroll = ScrollView(size_hint_y=0.8)
        self.chat_history = Label(
            text="Jarvis tayyor, ser.\n", 
            size_hint_y=None, 
            halign='left', 
            valign='top', 
            font_size='18sp'
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        self.add_widget(self.scroll)

        # Yozish paneli
        self.input_area = BoxLayout(size_hint_y=0.2)
        self.input_box = TextInput(hint_text="Buyruq...", multiline=False)
        self.btn = Button(text=">>", size_hint_x=0.2)
        self.btn.bind(on_release=self.send_message)
        self.input_area.add_widget(self.input_box)
        self.input_area.add_widget(self.btn)
        self.add_widget(self.input_area)

    def send_message(self, *args):
        msg = self.input_box.text
        if msg:
            self.chat_history.text += "\nSiz: " + msg
            self.input_box.text = ""
            try:
                res = requests.post(URL, json={
                    "model": "llama-3.3-70b-versatile",
                    "messages": [{"role": "user", "content": msg}]
                }, headers={"Authorization": "Bearer " + API_KEY}, timeout=10)
                reply = res.json()['choices'][0]['message']['content']
                self.chat_history.text += "\nJarvis: " + reply
            except:
                self.chat_history.text += "\nXatolik yuz berdi."

class MainApp(App):
    def build(self):
        return JarvisCore()

if __name__ == "__main__":
    MainApp().run()
