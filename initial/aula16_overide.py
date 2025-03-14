from typing import override, overload

class Base:
    @staticmethod
    def log_status() -> None:
        print("test")

class Sub(Base):
    @override
    def log_status() -> None:  # Okay: overrides Base.log_status
       print("override")

    @override
    def done(self) -> None:  # Error reported by type checker
        ...


Sub.log_status()