# Cloud-computing-with-AWS

# Cloud computing

Cloud computing is a network of servers connected using the Internet. Its main function is to share information, resources, and software. The Internet acts as the invisible cable that connects everything. This includes all physical and virtual servers all over the globe.

Simply put, cloud computing is the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet (“the cloud”) to offer faster innovation, flexible resources, and economies of scale.

Cloud computing is the on-demand availability of computer system resources, especially data storage and computing power, without direct active management by the user. Large clouds often have functions distributed over multiple locations, each location being a data center.

## Benefits

### Examples

Pay as you go: cost effectiveness
Capex, opex: capital and operational expenditure
- A seasonal business will need flexibility to scale the use of resources as needed. When the business needs less resources it can scale back and save money on IT costs.

### AWS Global Infrastructure Map

- Normally, a company will use 3 availability zones.
- Example: Sparta Global uses London for computing resources, Ireland for databases and Ireland for networks.

### Cloud Models

- Public
- Private
- Hybrid

Example: the bank industry usually uses the hybrid model because they deal with highly sensitive information and they prefer to mantain control of these data. For other information that needs to have high availability they will use public services.

- Naming convention for the files that I create: eng110_sergio
- Instances should be turned off/terminated every day before 6pm (exceptionally 8pm maximum)
- Only use the Ireland region: eu-west-1/a/b/c
- AWS keys must not be shared with anyone.
- eng119.pem: move to .ssh folder in my machine

### Use of cloud services

- We have a monolith application available on premises/localhost/local data centre, that we want to deploy on cloud services.
- We create an VM instance, called EC2 in Amazon web services
- We need to SSH into the VM. For that we need a file.pem (chmod 400)
- We store the file in a .ssh folder (it is a private key)
- By default the ssh port is 22
- We have to create a security group to allow the required ports for some applications that run on especified ports (80 - 3000 for example)

### Cloud terminology

- storage: volume - EBS
- firewall: security group
- memory
- processing power

The client will give us the especifications according to 3 constrains:
- cost
- time
- power

### Steps to create a VM on AWS

- Create new EC2 instance on Ireland availability zone
- Step 1: Choose an Amazon Machine Image (AMI)
- Step 2: Choose the Ubuntu Server 18.04 LTS (HVM), SSD Volume Type Instance
- Select: Type t2.micro
- Step 3: Select: `Next: Configure Instance Details`
          Enable: `Auto-assign Public IP`
- Step 4: Add storage
- Step 5: Add tags: eng110_sergio
- Step 6: Configure security group: eng110_sergio_sg
- Select: type: SSH, Source: MyIP
- Add rule `HTTP`, Port range: 80, Source: anywhere
- Finally: click on Review and Launch
- Select an existing key pair: `Eng119`

### How to SSH into the VM

- Download the eng119.pem file and move it to our `.shh` folder
- Click on `Connect to instance`
- Click on `SSH client`
- Copy the SSH address: `ssh -i "eng119.pem" ubuntu@ec2-18-203-127-78.eu-west-1.compute.amazonaws.com`

### How to install nginx in our VM and access the nginx welcome web page

- sudo apt update/upgrade
- sudo apt install nginx
- Copy the VM Public IP address into my browser to access the nginx welcome page
- IP: `18.203.127.78`

![AWS diagram](aws_diagram.jpg)