from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def right(self):
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def down(self):
        pass


class Control(IControl):
    def top(self):
        print("Movendo para cima...")

    def right(self):
        print("Movendo para a direita...")

    def left(self):
        print("Movendo para a esquerda...")

    def down(self):
        print("Movendo para baixo...")


class NewControl:
    def move_top(self):
        print("New Control: Movendo para cima...")

    def move_right(self):
        print("New Control: Movendo para a direita...")

    def move_left(self):
        print("New Control: Movendo para a esquerda...")

    def move_down(self):
        print("New Control: Movendo para baixo...")


class ControlAdapter(IControl):
    def __init__(self, new_control: NewControl):
        self.new_control = new_control

    def top(self):
        self.new_control.move_top()

    def right(self):
        self.new_control.move_right()

    def left(self):
        self.new_control.move_left()

    def down(self):
        self.new_control.move_down()


new_control = NewControl()
control = ControlAdapter(new_control)
control.top()
