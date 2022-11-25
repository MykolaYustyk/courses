'''
3. Реалізуйте класс Transaction. Його конструктор повинен приймати такі параметри:
- amount - суму на яку було здійснено транзакцію
- date - дату переказу
- currency - валюту в якій було зроблено переказ (за замовчуванням USD)
- usd_conversion_rate - курс цієї валюти до долара (за замовчуванням 1.0)
- description - опис транзакції (за дефолтом None)
Усі параметри повинні бути записані в захищені (_attr) однойменні атрибути.
Доступ до них повинен бути забезпечений лише на читання та за допомогою механізму property.
При чому якщо description дорівнює None, то відповідне property має повертати рядок "No description provided".
Додатково реалізуйте властивість usd, що має повертати суму переказу у доларах (сума * курс)
'''
class Transaction:
    
    def __init__(self, amount, date, currency='USD', usd_conversion_rate=1.0, discription=None):
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversation_rate = usd_conversion_rate
        self._discription = discription
        
    @property
    def amount(self):
        return self._amount
    
    @property
    def date(self):
        return self._date    
    
    @property
    def currency(self):
        return self._currency    
    
    @property
    def usd_conversation_rate(self):
        return self._usd_conversation_rate    
    
    @property
    def discription(self):
        if self.discription is None:
            print("No description provided")
        else:
            return self._discription
        
    @property
    def usd(self):
        if self.currency == "USD":
            return self.amount
        else:
            return self.amount * 1 / self.usd_conversation_rate
    
if __name__ == "__main__":
    trans1 = Transaction(200, '24.11.2022', "UAH", 37)
    print(f'{trans1.usd:.2f}')
