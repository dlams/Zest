class ZestEditImmutableObject(Exception):
    ...


class ZestComponentPosition:
    def __init__(self, y: int = 0, x: int = 0, position_tuple: tuple = (0, 0), is_mutable: bool = True):
        self.y, self.x = y, x
        self.is_mutable = is_mutable
        if isinstance(position_tuple, tuple) and position_tuple != (0, 0):
            if len(position_tuple) != 2:
                raise ValueError("position_tuple should be a 2-tuple")
            self.y, self.x = position_tuple

    def __add__(self, other):
        if not self.is_mutable:
            raise ZestEditImmutableObject(f"You can't update position")
        if isinstance(other, tuple) and len(other) != 2:
            dy, dx = other
            return ZestComponentPosition(self.y + dy, self.x + dx)
        if isinstance(other, ZestComponentPosition):
            return ZestComponentPosition(self.y + other.y, self.x + other.x)
        raise ValueError("ZestComponentPosition's targeted object must be 2-tuple or ZestComponentPosition")

    def __repr__(self) -> str:
        return f"ZestComponentPosition(y={self.y}, x={self.x})"


class ZestComponentSize:
    def __init__(self, height: int = 0, width: int = 0, size_tuple: tuple = (0, 0), is_mutable: bool = True):
        self.height, self.width = height, width
        self.is_mutable = is_mutable
        if isinstance(size_tuple, tuple) and size_tuple != (0, 0):
            if len(size_tuple) != 2:
                raise ValueError("size_tuple should be a 2-tuple")
            self.y, self.x = size_tuple

    def __add__(self, other):
        if not self.is_mutable:
            raise ZestEditImmutableObject(f"You can't edit size")
        if isinstance(other, tuple) and len(other) == 2:
            dy, dx = other
            return ZestComponentSize(self.height + dy, self.width + dx)
        if isinstance(other, ZestComponentSize):
            return ZestComponentSize(self.height + other.height, self.width + other.width)
        raise ValueError("ZestComponentSize's targeted object must be 2-tuple or ZestComponentSize")

    def __repr__(self) -> str:
        return f"ZestComponentSize(height={self.height}, width={self.width})"


class ZestUIInterface:
    def __init__(self, position: ZestComponentPosition, size: ZestComponentSize):
        self.position = position
        self.size = size
