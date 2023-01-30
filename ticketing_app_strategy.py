import random
import string
from abc import ABC, abstractmethod

def generate_id(lenght=8):
    return ''.join(random.choices(string.ascii_uppercase, k=lenght))

class SupportTicket:
    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, ticket_list):
        pass

class FIFOOrderingStrategy(TicketOderingStrategy):
    def create_ordering(self, ticket_list):
        return ticket_list.copy()

class FILOOrderingStrategy(TicketOderingStrategy):
    def create_ordering(self, ticket_list):
        list_copy = ticket_list.copy()
        list_copy.reverse()
        return list_copy

class RandomOrderingStrategy(TicketOderingStrategy):
    def create_ordering(self, ticket_list):
        list_copy = ticket_list.copy()
        random.shuffle(list_copy)
        return list_copy

class CustomerSupport:
    def __init__(self, processing_strategy: TicketOderingStrategy) -> None:
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!!")
            return
        
        ticket_list = self.processing_strategy.create_ordering(self.tickets)
        
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket):
        print("============================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("============================")

app = CustomerSupport(RandomOrderingStrategy())

app.create_ticket("John Snow", "My computer make strange sounds!!!")
app.create_ticket("Sebastian Santos", "I can't upload any videos, help me!!!")
app.create_ticket("John Sena", "VScode doesn't work.")

app.process_tickets()