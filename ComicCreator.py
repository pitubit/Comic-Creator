import kivy
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.graphics import Line

Builder.load_file("tool_box.kv")
Builder.load_file("drawing_space.kv")
Builder.load_file("general_options.kv")
Builder.load_file("status_bar.kv")
Builder.load_file("comicwidgets.kv")


class ComicCreator(AnchorLayout):
	pass
	
class ComicApp(App):
	def build(self):
		return ComicCreator()
		
if __name__ == "__main__":
	app = ComicApp()
	app.run()