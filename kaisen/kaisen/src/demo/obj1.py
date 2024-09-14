class ProvisionVirtualMachine:
    def __init__(self, name, memory, cpu, os):
        self.name = name
        self.memory = memory


c = ProvisionVirtualMachine("VM1", 4, 2, "Ubuntu")
print(c)
