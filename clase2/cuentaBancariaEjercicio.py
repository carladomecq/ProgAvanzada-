class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Fondos insuficientes")
        self.saldo -= cantidad


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def retirar(self, cantidad):
        if cantidad > self.saldo + self.limite:
            raise ValueError("Límite de crédito excedido")
        self.saldo -= cantidad


class CajaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, tasa_interes):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_intereses(self):
        self.saldo += self.saldo * self.tasa_interes


class CuentaDolares(CuentaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)