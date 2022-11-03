from abc import ABC, abstractmethod
import math
from operator import length_hint

class UIElement(ABC):

    @abstractmethod
    def render(self):
        pass

class Spacer(UIElement):
    def __init__(self, length = 1) -> None:
        self.length = length

    def render(self):
        return " " * self.length

class Line(UIElement):
    def __init__(self, length, symbol="-") -> None:
        self.length = length
        self.symbol = symbol

    def render(self):
        return self.symbol * self.length

class Text(UIElement):
    def __init__(self, text) -> None:
        self.text = text

    def render(self):
        return self.text

class FancyText(Text):
    def __init__(self, text, symbol="="):
        super().__init__(text)
        self.symbol = symbol

    def render(self):
        return self.symbol + self.symbol.join([char for char in self.text]) + self.symbol

class UIStackElement(UIElement):    
    def __init__(self, *elements) -> None:
        self.elements = elements

class HorizontalStack(UIStackElement):
    def __init__(self, *elements):
        super().__init__(elements)

    def render(self):
        return "".join([el.render() for el in self.elements[0]])

class VerticalStack(UIStackElement):
    def __init__(self, *elements) -> None:
        super().__init__(elements)

    def render(self):
        return "\n".join([el.render() for el in self.elements[0]])

class Box(UIStackElement):
    def __init__(self, width, *elements) -> None:
        super().__init__(elements)
        self.width = width

    def render(self):
        boxTopBottomBorder = HorizontalStack(Text("+"), Line(self.width - 2, "="), Text("+")).render()
        elementsStrings = [boxTopBottomBorder]
        for element in self.elements[0]:
            borderSeperator = Text("|").render()
            elementPreContent = borderSeperator
            elementContent = element.render()
            elementAfterContent = borderSeperator
            elementStringWidth = len(elementPreContent) + len(elementAfterContent) + len(elementContent)

            if(elementStringWidth > self.width): 
                elementContent = elementContent[0:(self.width - elementStringWidth)]
            elif(elementStringWidth < self.width): 
                elementContent += Spacer(self.width - len(elementContent) - 2).render()

            elementsStrings.append(elementPreContent + elementContent + elementAfterContent)

        elementsStrings.append(boxTopBottomBorder)

        return "\n".join(elementsStrings)

class ProgressBar(UIElement):
    def __init__(self, length, progress):
        self.length = length
        self.progress = progress

    def render(self):
        loadingContentLength = self.length - 2
        return f"[{Line(math.ceil(loadingContentLength * self.progress), '=').render() + Line(math.floor(loadingContentLength * (1 - self.progress)), '-').render()}]"


# ui = Box(19,
#     FancyText("WELCOME!"),
#     Spacer(),
#     Text("Loading packages:THIS SHOULD NOT BE SHOWN IN THE BOX"),
#     HorizontalStack(
#         Line(3),
#         Spacer(),
#         Text("cowsay")
#     ),
#     HorizontalStack(
#         Line(3),
#         Spacer(),
#         Text("lolcat")
#     ),
#     HorizontalStack(
#         Line(3, symbol=">"),
#         Spacer(),
#         Text("whoami"),
#         Text("...")
#     ),
#     Spacer(),
#     HorizontalStack(
#         Spacer(),
#         ProgressBar(15, 0.4),
#         Spacer()
#     )
# )

# print(ui.render())
ui = Box(19,
    FancyText("WELCOME!"),
    Spacer(),
    Text("Loading packages:THIS SHOULD NOT BE SHOWN IN THE BOX"),
    HorizontalStack(
        Line(3),
        Spacer(),
        Text("cowsay")
    ),
    HorizontalStack(
        Line(3),
        Spacer(),
        Text("lolcat")
    ),
    HorizontalStack(
        Line(3, symbol=">"),
        Spacer(),
        Text("whoami"),
        Text("...")
    ),
    Spacer(),
    HorizontalStack(
        Spacer(),
        ProgressBar(15, 0.4),
        Spacer()
    )
)

print(ui.render())