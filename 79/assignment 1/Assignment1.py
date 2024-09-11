class Node:
    def __init__(self, patient_id,name,age,patient_problem):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.patient_problem = patient_problem
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, patient_id,name,age,patient_problem):
        new_node = Node(patient_id,name,age,patient_problem) #new node is object of Node class (for 1 patient)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def search(self,patient_id):
        current = self.head
        while current is not None:
            if current.patient_id == patient_id:
                return current
            current = current.next
        return None


    def delete(self,patient_id):
        current=self.head
        prev=None
        while current and current.patient_id != patient_id:
            prev=current
            current=current.next
        if current is None:
            print(f"Patient with ID {patient_id} not found")
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        print(f"Patient with ID {patient_id} deleted")

        def schedule_to_front(self,patient_id):
            if self.head is None or self.patient_id == patient_id:
                print(f"Patient with ID {patient_id} is already at front or list is empty")
                return

            current = self.head
            prev= None

            while current is not None and current.patient_id != patient_id:
                prev=current
                current=current.next

            if current is None:
                print(f"Patient with ID {patient_id} is not found")
                return
            if prev:
                prev.next = current.next

            current.next = self.head
            self.head = current
            print(f"Patient with ID {patient_id} moved to first")

        def display(self):
            current = self.head
            while current is not None:
                print(f"Patient with id:{current.patient_id},Name {current.name},Age{current.age},Patient problem:{current.patient_problem}")
                current=current.next
class Hospital_Management:
    def __init__(self):
        self.list=LinkedList()

    def menu(self):
        print("\n Welcome to Hospital Management \n 1.Add Patient \n 2.Search Patient \n 3.Delete Patient \n 4.Move to front Patient \n 5.Display \n 6.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            self.add_patient()
        elif ch==2:
            self.search_patient()
        elif ch==3:
            self.delete_patient()


    def add_patient(self):
        patient_id = int(input("Enter patient id:"))
        name = input("Enter patient name:")
        age = int(input("Enter patient age:"))
        patient_problem = input("Enter patient problem:")
        self.list.add(patient_id, name, age, patient_problem)
        print("Patient added successfully")

    def search_patient(self):
        patient_id = int(input("Enter patient id:"))
        patient=self.list.search(patient_id)
        if patient:
            print(f"Patient found ID:{patient.patient_id},name{patient.name},age{patient.age},patient_problem:{patient.patient_problem}")
        else:
            print(f"Patient id ,{patient_id} not found")

    def delete_patient(self):
        patient_id = int(input("Enter patient id:"))
        self.list.delete(patient_id)
        print("Patient deleted successfully")

    def move_to_front(self):
        patient_id = int(input("Enter patient id:"))
        self.list.schedule_to_front(patient_id)
        print("Patient deleted successfully")

if __name__=="__main__":
    h=Hospital_Management()
    h.menu()

