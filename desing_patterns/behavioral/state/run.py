print("O State é um padrão de projeto comportamental que permite que um objeto altere seu comportamento quando seu estado interno muda. Parece como se o objeto mudasse de classe.")

from abc import ABC, abstractmethod


class Pedido:
    def __init__(self) -> None:
        self.state = Order()
        print("Pedido feito!")
        print()
        self.state.pedding()
        self.state.approve()
        self.state.pedding()
        self.state.reject()
        self.state.pedding()
        self.state.approve()
        self.state.reject()
    


class Order:
    def __init__(self) -> None:
        self.state = PaymentPendding(self)

    def pedding(self) -> None:
        print("Tentando execultar pedding")
        self.state.pendding()
        print("Estado atual: ", self.state)
        print()

    def approve(self) -> None:
        print("Tentando execultar approve")
        self.state.approve()
        print("Estado atual: ", self.state)
        print()

    def reject(self) -> None:
        print("Tentando execultar reject")
        self.state.reject()
        print("Estado atual: ", self.state)
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pendding(self) -> None: ...
    
    @abstractmethod
    def approve(self) -> None: pass
    
    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPendding(OrderState):
    def pendding(self) -> None:
        print("Pagamento já pendente, não pode fazer nada.")
    
    def approve(self) -> None: 
        self.order.state = PaymentApproved(self.order)
        print("Pagamento Aprovado.")
    
    def reject(self) -> None: 
        self.order.state = PaymentRejected(self.order)
        print("Pagamento Recusado.")


class PaymentApproved(OrderState):
    def pendding(self) -> None:
        self.order.state = PaymentPendding(self.order)
        print("Pagamento Recusado!")
    
    def approve(self) -> None:
        print("Pagamento já está aprovado, não pode fazer nada.")
    
    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Pagamento Recusado.")


class PaymentRejected(OrderState):
    def pendding(self) -> None:
        print("Pagamento já recusado, não pode fazer nada.")
    
    def approve(self) -> None:
        print("Pagamento já recusado, não posso recusar novamente.")
    
    def reject(self) -> None:
        print("Pagamento já recusado, não posso recusar novamente.")


print()
if __name__ == "__main__":
    pedido = Pedido()
