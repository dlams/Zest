from font_loader import ZestFontObject
from src.ui_interface import ZestUIInterface, ZestComponentPosition, ZestComponentSize

class ZestTextObject(ZestUIInterface):
    def __init__(self, position: ZestComponentPosition, size: ZestComponentSize, content: str, font: ZestFontObject):
        super().__init__(position=position, size=size)
        self.content = content
        self.font = font

    def get_content(self) -> str:
        return self.content

    # TODO WIP draw (make ZestScreenObject || ZestUIObject)
    def draw(self):
        raise NotImplementedError

    def __repr__(self):
        return f"{self.__class__.__name__}({self.position}, {self.size}, {self.content}, {self.font})"