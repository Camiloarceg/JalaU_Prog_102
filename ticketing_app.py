import random
import string

class Strategy():
    def strategy(self):
        pass

class Stategy_fifo(Strategy):
    def strategy():
        for ticket in self.tickets:
            self.process_ticket(ticket)

class Stategy_filo(Strategy):
    def strategy():
        for ticket in reversed(self.tickets):
            self.process_ticket(ticket)
class Stategy_random(Strategy):
    def strategy():
        list_copy = self.tickets.copy()
        random.shuffle(list_copy)
        for ticket in list_copy:
            self.process_ticket(ticket)

def generate_id(lenght=8):
    return ''.join(random.choices(string.ascii_uppercase, k=lenght))

class SupportTicket:
    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport():
    def __init__(self, processing_strategy="fifo") -> None:
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!!")
            return
        Strategy.strategy(self)

    def process_ticket(self, ticket):
        print("============================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("============================")

app = CustomerSupport("random")

app.create_ticket("John Snow", "My computer make strange sounds!!!")
app.create_ticket("Sebastian Santos", "I can't upload any videos, help me!!!")
app.create_ticket("John Sena", "VScode doesn't work.")

app.process_tickets()