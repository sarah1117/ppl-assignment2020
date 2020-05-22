import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import cairo

r1=0
r2=0
r3=0
lw=0.5

class MouseButtons:
    
    Left = 1
    Right = 3

class Window(Gtk.Window):
	def __init__(self):
		super(Window, self).__init__()
		self.set_title("Paint application")
		self.set_default_size(800,600)

		mainMenu = Gtk.MenuBar.new()
		fileMenu = Gtk.MenuItem.new_with_label("File")
		brushSize = Gtk.MenuItem.new_with_label("Brush Size")
		brushColour = Gtk.MenuItem.new_with_label("Brush Colour")

		fileMenu1 = Gtk.Menu.new()
		brushSize1 = Gtk.Menu.new()
		brushColour1 = Gtk.Menu.new()

		fileMenu.set_submenu(fileMenu1)
		brushSize.set_submenu(brushSize1)
		brushColour.set_submenu(brushColour1)

		mainMenu.append(fileMenu)
		mainMenu.append(brushSize)
		mainMenu.append(brushColour)
		
		save = Gtk.MenuItem.new_with_label("Save")
		clear = Gtk.MenuItem.new_with_label("Clear")
		fileMenu1.append(save)
		fileMenu1.append(clear)

		px3 = Gtk.MenuItem.new_with_label("3Px")
		px5 = Gtk.MenuItem.new_with_label("5Px")
		px7 = Gtk.MenuItem.new_with_label("7Px")
		px9 = Gtk.MenuItem.new_with_label("9Px")
		brushSize1.append(px3)
		brushSize1.append(px5)
		brushSize1.append(px7)
		brushSize1.append(px9)
		px3.connect('activate',self.on_smenu)
		px5.connect('activate',self.on_smenu)
		px7.connect('activate',self.on_smenu)
		px9.connect('activate',self.on_smenu)

		black = Gtk.MenuItem.new_with_label("Black")
		red = Gtk.MenuItem.new_with_label("Red")
		green = Gtk.MenuItem.new_with_label("Green")
		blue = Gtk.MenuItem.new_with_label("Blue")
		brushColour1.append(black)
		brushColour1.append(red)
		brushColour1.append(green)
		brushColour1.append(blue)   
		black.connect('activate',self.cchange)
		red.connect('activate',self.cchange)
		green.connect('activate',self.cchange)
		blue.connect('activate',self.cchange)
		
		self.connect("destroy",Gtk.main_quit)
		darea=Gtk.DrawingArea()
		darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)       
		self.coords = []
                     
		darea.connect("button-press-event", self.on_button_press)
		hb = Gtk.HeaderBar()
		hb.pack_start(mainMenu)
		box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		box.pack_start(hb, False, False, 10)
		box.pack_start(darea, True, True, 10)
		self.add(box)
		self.show_all()

	def on_button_press(self, w, e):
		left=1
		right=3
		if e.type == Gdk.EventType.BUTTON_PRESS and e.button == MouseButtons.Left:
            		self.coords.append([e.x, e.y])
		if e.type == Gdk.EventType.BUTTON_PRESS and e.button == MouseButtons.Right:
			cr = w.get_property('window').cairo_create()
			cr.set_source_rgb(r1, r2, r3)
			cr.set_line_width(lw)
			for i in range(len(self.coords)-1):
				cr.move_to(self.coords[i][0], self.coords[i][1])
				cr.line_to(self.coords[i+1][0],self.coords[i+1][1]) 
				cr.stroke()
			del self.coords[:]
	def on_smenu(self, widget):
		m=widget.get_label()
		global lw
		if m == "3Px":
			lw =1
		elif m=="5Px":
			lw =2
		elif m=="7Px":
			lw =3
		else:
			lw=4
	def cchange(self,widget):
		m=widget.get_label()
		global r1,r2,r3
		if m == "Blue":
			r1=0.2
			r2=0.23
			r3=0.9
		elif m=="Red":
			r1=0.9
			r2=0.1
			r3=0.1
		elif m=="Green":
			r1=0.4
			r2=0.9
			r3=0.4
		else:
			r1=0
			r2=0
			r3=0
		

				  

            		
			   
Window()

Gtk.main()
