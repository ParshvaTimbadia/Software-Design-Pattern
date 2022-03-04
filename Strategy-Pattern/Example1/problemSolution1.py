import random
import string
from typing import List
from abc import ABC, abstractmethod


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = self.generate_id()
        self.customer = customer
        self.issue = issue

    def generate_id(self, length = 8) -> string:
        return ''.join(random.choices(string.ascii_uppercase, k=length))


class ProcessingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOProcessingStrategy(ProcessingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()

class LIFOProcessingStrategy(ProcessingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        listCopy = list.copy()
        return listCopy.reverse()

class RandomProcessingStrategy(ProcessingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        listCopy = list.copy()
        random.shuffle(listCopy)
        return listCopy



class CustomerSupport:
    tickets: List[SupportTicket] = []

    def generateTicket(self, customer:string,issue:string) -> None:
        self.tickets.append(SupportTicket(customer, issue))



    def processingOrder(self, strategy:ProcessingStrategy = FIFOProcessingStrategy()) -> None:

        processedTickets = strategy.create_ordering(self.tickets)
        for ticket in processedTickets:
           self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket) -> None:
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


app = CustomerSupport()

app.generateTicket("Parshva", "Phone not working")
app.generateTicket("Nemil", "Laptop not working")
app.generateTicket("Kinara", "Tablet not working")

app.processingOrder(RandomProcessingStrategy())



