# Hypervisor

A hypervisor is a form of virtualization software used in Cloud hosting to divide and allocate the resource on various pieces of hardware. The program which provides partitioning, isolation or abstraction is called virtualization hypervisor. The hypervisor is hardware virtualization technique that allows multiple guest operating system(OS) to run on a single host system at the same time. A hypervisor is sometime also called a virtual machine manager(VMM)

# Type of Hypervisor -

## TYPE-1 Hypervisor:
The hypervisor runs directly on the underlying host system. It is also knowns as "Native Hypervisor" or "Bare metal hypervisor". It does not require any base server operating system. It has direct access to hardware resources. Examples of Type 1 hypervisors include VMware ESXi, Citrix XenServer and Microsoft Hyper-Vhypervisor.


- Pros: Such kind of hypervisors are very efficient because they have access to the physical hardware resources(like Cpu, Memory, Network, Physical storage).
This cause the empowerment the security because there is nothing any kind of the third party resources so that attacker could't compromise with anything.

- Cons: One problem with Type-1 hypervisor is that they usually need a dedicated separate machine to perform its operation and to instruct different VMs and control the host hardware resources.


