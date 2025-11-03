class Version(int):
    def __new__(cls, major: int, minor: int, patch: int):
        return super().__new__(cls, (major << 16) | (minor << 8) | patch)
    
    def __repr__(self) -> str:
        return f"Version(major={self.major}, minor={self.minor}, patch={self.patch})"
    
    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"
    
    @property
    def major(self) -> int:
        return (self >> 16) & 0xff
    
    @property
    def minor(self) -> int:
        return (self >> 8) & 0xff

    @property
    def patch(self) -> int:
        return self & 0xff
    
version = Version(1, 5, 0)