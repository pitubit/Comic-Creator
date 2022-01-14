
import kivy
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from comicwidgets import StickMan

class ToolButton(ToggleButton):
	def on_touch_down(self, touch):
		ds = self.parent.drawing_space
		if self.state == "down" and ds.collide_point(touch.x, touch.y):
			(x, y) = ds.to_local(touch.x, touch.y)
			self.draw(ds, x, y)
			return True
		return super().on_touch_down(touch)
		
	def draw(self, ds, x, y):
		pass


class ToolStickMan(ToolButton):
	def draw(self, ds, x, y):
		sm = StickMan(width=98, height=98)
		sm.center = x, y
		ds.add_widget(sm)
		
class ToolCircle(ToolButton):
	def draw(self, ds, x, y):
		circle = Line(circle=(x,y,34))
		ds.bind(circle)
		
class ToolLine(ToolButton):
	def draw(self, ds, x, y):
		pass







