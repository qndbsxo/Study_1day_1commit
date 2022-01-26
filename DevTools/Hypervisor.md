# Hypervisor

A hypervisor is a form of virtualization software used in Cloud hosting to divide and allocate the resource on various pieces of hardware. The program which provides partitioning, isolation or abstraction is called virtualization hypervisor. The hypervisor is hardware virtualization technique that allows multiple guest operating system(OS) to run on a single host system at the same time. A hypervisor is sometime also called a virtual machine manager(VMM)

# Type of Hypervisor -

## TYPE-1 Hypervisor:
The hypervisor runs directly on the underlying host system. It is also knowns as "Native Hypervisor" or "Bare metal hypervisor". It does not require any base server operating system. It has direct access to hardware resources. Examples of Type 1 hypervisors include VMware ESXi, Citrix XenServer and Microsoft Hyper-Vhypervisor.


- Pros: Such kind of hypervisors are very efficient because they have access to the physical hardware resources(like Cpu, Memory, Network, Physical storage).
This cause the empowerment the security because there is nothing any kind of the third party resources so that attacker could't compromise with anything.

- Cons: One problem with Type-1 hypervisor is that they usually need a dedicated separate machine to perform its operation and to instruct different VMs and control the host hardware resources.

# TYPE-2 Hypervisor
A Host operating system runs on the underlying host system. It is also known as "Hosted Hypervisor". Such kind of hypervisors doesn't run directly over the underlying hardware rather they run as an application in a Host system(physical machine). Basically, software installed on an operating system. Hypervisor asks the operating system to make hardware calls. Example of Type 2 hypervisor includes VMware Player or Parallels Desktop.
Hosted hypervisors are often found on endpoints like PCs. The type-2 hypervisor is are very useful for engineers, security analyst(for checking malware, or malicious source code and newly developed application)

# Pros & Cons of Type-2 Hypervisor:

`Pros`: Such kind of hypervisors allows quick and easy access to a quest Operating System alongside the host machine running. These hypervisors usually come with additional useful features for guest machine. Such tools enhance the coordination between the host machine and guest machine.

`Cons`: Here there is no direct access to the physical hardware resources so the efficiency of these hypervisors langs in performance as compared to the type-1 hypervisors, and potential security risks are also there an attacker can compromise the security weakness if there is access to the host operating system so he can also access the guest operating system.

# Choosing the right hypervisor:
Type1 hypervisors offer much better performance than type 2 ones because there's no middle layer, making them the logical choice for mission-critical applications and workloads. But that's not to say that hosted hypervisors don't have their place - they're much simpler to set up, so they're a good bet if, say, you need to deploy a test environment quickly. ONe of the best ways to determine which hypervisor meets your needs is to compare their performance metrics. These include CPU overhead, amount of maximum host and guest memory, and support for virtual processors. The following factors should be examined before choosing a suitable hypervisor:

1. Understand your needs: The company and its applications are the reason for the date centre (and your job). Besides your company's needs, you (and your co-workers in IT) also have your own needs. Needs for a virtualization hypervisor are:
   a. Flexibility 
   b. Scalability
   c. Usability
   d. Availability
   e. Reliability
   f. Efficiency
   g. Reliable support

2. The cost of a hypervisor: For many buyers. the toughest part of choosing a hypervisors is striking the right balance between cost and functionality. While a number of entry-level solutions are free, or practically free, the prices at the 

