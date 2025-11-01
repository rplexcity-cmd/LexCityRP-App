
import webbrowser
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

SERVER_IP = "151.242.227.221:7777"
DISCORD_LINK = "https://discord.gg/Hy6jPvAZS3"

class LexCityApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=20, padding=50)
        layout.add_widget(Button(text="Entrar no Servidor", on_press=lambda x: webbrowser.open(f"samp://{SERVER_IP}")))
        layout.add_widget(Button(text="Entrar no Discord", on_press=lambda x: webbrowser.open(DISCORD_LINK)))
        layout.add_widget(Button(text="Site Oficial", on_press=lambda x: webbrowser.open("https://lexcityrp.com.br")))
        return layout

if __name__ == "__main__":
    LexCityApp().run()
