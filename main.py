from typing import Tuple
 
 
class CoffeeOrder: 
    # Базовые цены
    BASE_PRICES = {
        "espresso": 200,
        "americano": 250,
        "latte": 300,
        "cappuccino": 320,
    }
    
    # Размер
    SIZE_MULTIPLIERS = {
        "small": 1.0,
        "medium": 1.2,
        "large": 1.4,
    }
    
    # Доплаты(молоко)
    MILK_PRICES = {
        "none": 0,
        "whole": 30,
        "skim": 30,
        "oat": 60,
        "soy": 50,
    }
    
    # Сироп
    SYRUP_PRICE = 40
    
    # Лёд
    ICE_PRICE = 20
    
    # Лимиты
    MAX_SUGAR = 5
    MAX_SYRUPS = 4
    
    def __init__(
        self,
        base: str,
        size: str,
        milk: str = "none",
        syrups: Tuple[str, ...] = (),
        sugar: int = 0,
        iced: bool = False,
    ):
        """
        Создаёт заказ
        
        Args:
            base: Тип кофе (espresso, americano, latte, cappuccino)
            size: Размер (small, medium, large)
            milk: Тип молока (none, whole, skim, oat, soy)
            syrups: Список названий сиропов
            sugar: Количество порций сахара (0-5)
            iced: Добавить лёд
            
        Raises:
            ValueError: При некорректных параметрах
        """
        # Валидация base
        if not base:
            raise ValueError("Base cannot be empty")
        if base not in self.BASE_PRICES:
            raise ValueError(f"Invalid base: {base}")
        
        # Валидация size
        if not size:
            raise ValueError("Size cannot be empty")
        if size not in self.SIZE_MULTIPLIERS:
            raise ValueError(f"Invalid size: {size}")
        
        # Валидация milk
        if milk not in self.MILK_PRICES:
            raise ValueError(f"Invalid milk type: {milk}")
        
        # Валидация syrups
        if len(syrups) > self.MAX_SYRUPS:
            raise ValueError(f"Too many syrups (max {self.MAX_SYRUPS})")
        
        # Валидация sugar
        if sugar < 0 or sugar > self.MAX_SUGAR:
            raise ValueError(f"Sugar must be between 0 and {self.MAX_SUGAR}")
        
        # Параметры
        self.base: str = base
        self.size: str = size
        self.milk: str = milk
        self.syrups: Tuple[str, ...] = syrups
        self.sugar: int = sugar
        self.iced: bool = iced
        
        # Рассчет цены
        self.price: float = self._calculate_price()
        
        # Сборка описания
        self.description: str = self._generate_description()
    
    def _calculate_price(self) -> float:
        """
        Рассчитывает итоговую цену заказа.
        
        Формула: (Цена * размер) + молоко + 
                 (количество сиропов * цена) + лёд
        
        Returns:
            float: Итоговая цена
        """
        # Базовая цена с учётом размера
        base_price = self.BASE_PRICES[self.base] * self.SIZE_MULTIPLIERS[self.size]
        
        # Доплата за молоко
        milk_price = self.MILK_PRICES[self.milk]
        
        # Доплата за сиропы
        syrup_price = len(self.syrups) * self.SYRUP_PRICE
        
        # Доплата за лёд
        ice_price = self.ICE_PRICE if self.iced else 0
        
        total = base_price + milk_price + syrup_price + ice_price
        
        return round(total, 2)
    
    def _generate_description(self) -> str:
        """
        Генерирует читабельное описание заказа
        
        Формат: "<size> <base> [with <milk> milk] [+syrup list] [(iced)] [<sugar> tsp sugar]"
        Элементы со значениями по умолчанию не включаются
        
        Returns:
            str: Описание заказа
        """
        parts = [self.size, self.base]
        
        if self.milk != "none":
            parts.append(f"with {self.milk} milk")
        
        if self.syrups:
            syrup_list = ", ".join(self.syrups)
            parts.append(f"+{syrup_list}")
        
        if self.iced:
            parts.append("(iced)")
        
        if self.sugar > 0:
            parts.append(f"{self.sugar} tsp sugar")
        
        return " ".join(parts)
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление заказа.
        
        Returns:
            str: Описание или строка с ценой
        """
        if self.description:
            return f"{self.description} — {self.price}"
        return f"Order: {self.price}"
 
 
def main() -> None:
    """Проверка"""
    
    print("=== Coffee Order System ===\n")
    
    # Базовый заказ 
    print("Базовый заказ:")
    order = CoffeeOrder(
        base="latte",
        size="medium",
        milk="oat",
        syrups=("vanilla", "caramel"),
        sugar=2,
        iced=True
    )
    
    # Проверка правильности типов
    print(f"Order: {order}")
    print(f"\nТипы полей:")
    print(f"  base: {type(order.base).__name__} = {order.base}")
    print(f"  size: {type(order.size).__name__} = {order.size}")
    print(f"  milk: {type(order.milk).__name__} = {order.milk}")
    print(f"  syrups: {type(order.syrups).__name__} = {order.syrups}")
    print(f"  sugar: {type(order.sugar).__name__} = {order.sugar}")
    print(f"  iced: {type(order.iced).__name__} = {order.iced}")
    print(f"  price: {type(order.price).__name__} = {order.price}")
    print(f"  description: {type(order.description).__name__}")
    
    # Проверка непустой цены
    print(f"\nЦена > 0: {order.price > 0}")
    
    # Проверка опций
    print(f"\nНаличие опций:")
    print(f"  milk == 'oat': {order.milk == 'oat'}")
    print(f"  syrups содержит 2 элемента: {len(order.syrups) == 2}")
    print(f"  sugar == 2: {order.sugar == 2}")
    print(f"  iced == True: {order.iced == True}")
 
 
if __name__ == "__main__":
    main()