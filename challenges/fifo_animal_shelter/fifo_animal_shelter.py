class Animal:
    def __init__(self, value=None):
        self.value = None
        if value.lower() != 'cat' and value.lower() != 'dog':
            raise TypeError("must be a cat or dog")


class Dog(Animal):
    def __init__(self):
        super().__init__('dog')
        self.next = None


class Cat(Animal):
    def __init__(self):
        super().__init__('cat')
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.front = None

    def enqueue(self, Animal):
        new_animal = Animal

        if self.front == None:
            self.front = new_animal
            return

    # Values exist in queue
        current = self.front
    # Traverse the list
        while current:
            if current.next == None:
                current.next = new_animal
                return
            current = current.next

    def dequeue(self, pref=None):
        current = self.front

        if pref is None:
            return 'enter cat or dog'
        while current:
            if current.value == pref:
                self.front = current.next
                current.next = None
                return current.value
            current = current.next


shelter = AnimalShelter()
shelter.enqueue(Cat())
shelter.enqueue(Cat())
print(shelter.dequeue('cat'))
