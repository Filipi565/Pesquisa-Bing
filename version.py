class Version(int):
    def __new__(cls, major: int, minor: int, patch: int):
        return super().__new__(cls, (major << 16) | (minor << 8) | patch)
    
    @property
    def major(self) -> int:
        return (self >> 16) & 0xff
    
    @property
    def minor(self) -> int:
        return (self >> 8) & 0xff

    @property
    def patch(self) -> int:
        return self & 0xff
    
version = Version(1, 0, 0)