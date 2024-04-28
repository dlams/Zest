import os
from pathlib import Path


class ZestFontObject:
    def __init__(self, namespace: str, font_path: os.path):
        self.namespace = namespace
        self.font_path = font_path

    def __repr__(self):
        return f"ZestFontObject(namespace='{self.namespace}', font_path='{self.font_path})'"


class FontLoader:
    def load(self, *args, **kwargs):
        raise NotImplementedError


class DefaultFontLoader(FontLoader):
    def __init__(self):
        home = Path.home()
        self.path = os.path.join(home, ".local/share/fonts")
        if not os.path.isdir(self.path):
            raise OSError(f"No font folder found at {self.path}")

    def load(self, *args, **kwargs) -> list[ZestFontObject]:
        object_generator = lambda file: ZestFontObject(os.path.splitext(file)[0], os.path.join(self.path, file))
        font_list = os.listdir(self.path)
        return [object_generator(file) for file in font_list]

if __name__ == "__main__":
    loader = DefaultFontLoader()
    print(loader.load())
