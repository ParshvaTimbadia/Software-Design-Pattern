import random
import string


from typing import List

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

class CustomerSupport:
    tickets: List[SupportTicket] = []

    def generateTicket(self, customer:string ,issue:string) -> None:
        self.tickets.append(SupportTicket(customer, issue))



    def processingOrder(self, strategy:string = "fifo") -> None:

        if strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
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

app.processingOrder("random")



"""
The above method works fine. However, it introduces weak cohesion. Meaning its not focused on what it should be doing. Tomorrow if someone introduces a new strategy will result
in changing the class definition.
"""