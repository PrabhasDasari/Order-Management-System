from abc import ABC, abstractmethod
from model.user import User
from model.product import Product

class IOrderManagementRepository(ABC):
    @abstractmethod
    def createOrder(self, user: User, products: list):
        pass

    @abstractmethod
    def cancelOrder(self, userId: int, orderId: int):
        pass

    @abstractmethod
    def createProduct(self, user: User, product: Product):
        pass

    @abstractmethod
    def createUser(self, user: User):
        pass

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def getOrderByUser(self, user: User):
        pass