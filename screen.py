import turtle
import tkinter as tk


class Screen():
    """
    Defines a root, canvas, screen.
    """
    def __init__(self):
        self.__root = tk.Tk()
        self.__canvas = turtle.ScrolledCanvas(self.__root, width=1000, height=600)
        self.__canvas.pack()
        self.__screen = turtle.TurtleScreen(self.__canvas)
        self.__turtle = turtle.RawTurtle(self.__screen)
        self.__ship = turtle.RawTurtle(self.__screen)
        self.__screen.setworldcoordinates(-500,-500,500,500)
        self.build_ship()

    def get_root(self):
        return self.__root

    def get_canvas(self):
        return self.__canvas

    def get_screen(self):
        return self.__screen

    def get_turtle(self):
        return self.__turtle

    def get_ship(self):
        return self.__ship

    def build_ship(self):
        ship = self.get_ship()
        ship.color("purple")
        ship.shape("triangle")
    """
    Defines a constant movement, moreso, uses 'ontimer' to call move_ship. What it means is every 10ms it will
    re-check move_ship, which creates the key-based movement"""
    def constant_movement(self):
        self.__ship.penup()
        self.__ship.forward(1)
        self.move_ship()
        self.__screen.ontimer(self.constant_movement(), 10)

    """" Uses the 'listen' function to await for orders from the user. It reacts accordingly."""
    def move_ship(self):
        self.__screen.listen()
        self.__screen.onkeypress(lambda: self.__ship.setheading(90), "Up")
        self.__screen.onkeypress(lambda: self.__ship.setheading(180), 'Left')
        self.__screen.onkeypress(lambda: self.__ship.setheading(0), 'Right')
        self.__screen.onkeypress(lambda: self.__ship.setheading(270), 'Down')

### Regarding speed, down will be speed-1, up will be speed +1. game will be the one to do this, not gui.
### TDL - makes it so it loops on those edges
if __name__ == '__main__':
    scr = Screen()
    root = scr.get_root()
    turt = scr.get_turtle()
    scr.constant_movement()
        # scr.get_screen().listen()
    root.mainloop()