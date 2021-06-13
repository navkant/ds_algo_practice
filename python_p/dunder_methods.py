class Account:
    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Amount must be integer")
        if sum(self._transactions) < -100 and amount < 0:
            return "You cannot withdraw, balance in negative"
        self._transactions.append(amount)

    def __repr__(self):
        return 'Account({}, {})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)

    def __len__(self):
        return len(self._transactions)

    def __reversed__(self):
        return self._transactions[::-1]

    def __getitem__(self, position):
        return self._transactions[position]

    def __add__(self, other):
        owner = self.owner + '&' + other.owner
        amount = self.amount + other.amount
        acc = Account(owner, amount)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc

    @property
    def balance(self):
        return self.amount + sum(self._transactions)
