print("SUBSCRIPTION MANAGER")
from collections import deque

class SubscriptionManager:
    def __init__(self):
        
        self.undo_stack = []
        
        
        self.subscription_queue = deque()
        
        
        self.services = []

    
    def add_service(self, service_name):
        self.services.append(service_name)
        print(f"Service {service_name} added to available services.")

    
    def remove_service(self, service_name):
        if service_name in self.services:
            self.services.remove(service_name)
            print(f"Service {service_name} removed from available services.")
        else:
            print(f"Service {service_name} not found.")

    
    def subscribe(self, user, service_name):
        if service_name in self.services:
            self.subscription_queue.append((user, service_name))
            self.undo_stack.append(('unsubscribe', user, service_name))
            print(f"User {user} subscribed to {service_name}.")
        else:
            print(f"Service {service_name} is not available.")

    
    def process_subscriptions(self):
        if self.subscription_queue:
            user, service_name = self.subscription_queue.popleft()
            print(f"Processing subscription: {user} to {service_name}.")
        else:
            print("No subscriptions to process.")

    
    def undo_last_action(self):
        if self.undo_stack:
            action, user, service_name = self.undo_stack.pop()
            if action == 'unsubscribe':
                self.unsubscribe(user, service_name)
        else:
            print("No actions to undo.")

    
    def unsubscribe(self, user, service_name):
        print(f"User {user} unsubscribed from {service_name}.")

    
    def show_services(self):
        if self.services:
            print("Available services:")
            for service in self.services:
                print(f"- {service}")
        else:
            print("No services available.")
    
    
    def show_queue(self):
        if self.subscription_queue:
            print("Pending subscriptions:")
            for user, service in self.subscription_queue:
                print(f"- {user} to {service}")
        else:
            print("No pending subscriptions.")


def show_menu():
    print("\n1. Add Service")
    print("2. Remove Service")
    print("3. Subscribe to a Service")
    print("4. Process Subscriptions")
    print("5. Undo Last Action")
    print("6. Show Available Services")
    print("7. Show Pending Subscriptions")
    print("8. Exit")

def main():
    manager = SubscriptionManager()
    
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            service_name = input("Enter the service name to add: ")
            manager.add_service(service_name)
        
        elif choice == '2':
            service_name = input("Enter the service name to remove: ")
            manager.remove_service(service_name)
        
        elif choice == '3':
            user = input("Enter the user name: ")
            service_name = input("Enter the service name: ")
            manager.subscribe(user, service_name)
        
        elif choice == '4':
            manager.process_subscriptions()
        
        elif choice == '5':
            manager.undo_last_action()
        
        elif choice == '6':
            manager.show_services()
        
        elif choice == '7':
            manager.show_queue()
        
        elif choice == '8':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__=="__main__":
  main()