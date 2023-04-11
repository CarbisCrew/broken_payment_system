from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int
    count: int

    @property
    def sum(self) -> int:
        return self.price*self.count