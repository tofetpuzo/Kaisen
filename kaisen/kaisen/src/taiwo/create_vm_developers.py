# Idea is to return a json file with username, email and request for number of vms to be created, also cpu , the also need the ip address of the vm
# API_USERNAME: https://reqres.in/api/users?page=1
# {
#     "username": "raliat",
#     "email": "",
#     "request": input("Enter the number of VMs you want to create: "),
#     "cpu": input("Enter the number of CPUs you want: "),
#
#     "cloud resource" : "aws", "Azure", "GCP"{
#         "aws": {
#             "region": "us-east-1",
# subnets: {
#     "subnet1": {
#         "cidr": {
#             "ip_address": {},
#            "subnet_mask": {},
#     }
# "AZURE": {
#     "region": "us-east-1",
#     "subnets": {
#         "subnet1": {
#             "cidr": {
#                 "ip_address": {},
#                 "subnet_mask": {},
#             }
#     }
#
# }
# }
# Class
# 1. CreateVM
# 2. Name of the developer -> an api for users https://reqres.in/api/users?page=1
# 3. Email of the developer
# 4. Number of VMs to be created
# 5. Number of CPUs
# 6. Cloud Resource
# 7. Region
# 8. Subnets
# 9. CIDR
# 10. IP Address
# 11. Subnet Mask
# 12. AZURE
# 13. AWS
# 14. GCP
# 15. Create a VM
# 16. Get the IP Address of the VM
# 17. Get the Subnet Mask of the VM

# property , setter, getter, constructor


class CreateVMDevelopers:
    def __init__(
        self,
        username,
        email,
        request,
        cpu,
        cloud_resource,
        region,
        subnets,
        cidr,
        ip_address,
        subnet_mask,
    ):
        self.username = username
        self.email = email
        self.request = request
        self.cpu = cpu
        self.cloud_resource = cloud_resource
        self.region = region
        self.subnets = subnets
        self.cidr = cidr
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask
