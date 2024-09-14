class VirtualMachine:
    def __init__(self, name, memory, cpu):
        self.name = name
        self.memory = memory
        self.cpu = cpu

    def _start(self):
        print(f"Starting {self.name} VM")

    def stop(self):
        print(f"Stopping {self.name} VM")

    def restart(self):
        self.stop()
        self.start()

    def ip_address(self):
        print(f"IP address of {self.name} VM is")

    # def __str__(self):
    #     return f"{self.name} VM has {self.memory} memory and {self.cpu} cpu"

    def __repr__(self) -> str:
        return f"{self.name} VM has {self.memory} memory and {self.cpu} cpu"

    def log(self):
        print(f"Log of {self.name} VM")


# initialize the object
vm1 = VirtualMachine("VM1", 4, 2)
vm2 = VirtualMachine("VM2", 8, 4)
vm3 = VirtualMachine("VM3", 16, 8)

print(vm1)


class ProvisionVirtualMachine(VirtualMachine):
    def __init__(self, name, memory, cpu, os):
        super().__init__(name, memory, cpu)
        self.os = os


# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction
