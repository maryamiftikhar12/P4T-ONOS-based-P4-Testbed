We build our SDN experimental setup and application development stack by combining free and open-source components. Our main computing resource was a Huawei server equipped with a powerful Intel(R) Xeon(R) Silver 4210 processor, 32 GB RAM and 2TB SAS storage. We installed  VMware ESXi version 7.0 U2 hypervisor in the server to build virtualization infrastructure.
The main P4-based topology in this tutorial has been accessed remotely through an ONOS controller. For this process, 2 different virtual machines were set up. P4 and Mininet were installed on the first machine, while ONOS was installed on the second virtual machine.
The Mininet version 2.3.1 and BMv2 components were hosted on VM1 with 16 GB of RAM and 8 vCPUs. The VM2 is given 8 GB of RAM along with 8 vCPUs and is used to install ONOS instance. VM1 is given more memory because Mininet topology with several switches were needed to be run on it.
The P4 program is compiled for the BMv2 simple_switch target using the command $make p4-build. For this, an open source P4_16 compiler (p4c) is used.
Leaf 1 is programmed using P4Runtime Shell, an interactive Python CLI that can be used to connect to a P4Runtime server and can run P4Runtime commands. For example, it can be used to create, read, update, and delete flow table entries. We recommend that you download the Docker image (~142MB) and use it, but you can also build the image directly with:
$git clone https://github.com/p4lang/p4runtime-shell
$cd p4runtime-shell
$docker build -t p4lang/p4runtime-sh .
Finally, when connecting to a P4Runtime server, a mastership election ID is provided to write state, such as the pipeline config and table entries. To connect the P4Runtime Shell to leaf1 and push the pipeline configuration obtained before, used the following command:
$util/p4rt-sh --grpc-addr 10.3.12.139:50001 --config p4src/build/p4info.txt,p4src/build/bmv2.json --election-id 0,1
In our case, the ONOS VM had specific IP 10.3.12.139 however the P4 and Mininet contained IP 10.3.12.140.
When the P4RT shell started, we used the following P4Runtime-sh commands to enable connectivity from VM 2 (IP: 10.3.12.140):
te = table_entry['IngressPipeImpl.l2_exact_table'](action='IngressPipeImpl.set_egress_port')
te.match['hdr.ethernet.dst_addr'] = '00:00:00:00:00:1A'
te.action['port_num'] = '3'
te.insert()
te = table_entry['IngressPipeImpl.l2_exact_table'](action='IngressPipeImpl.set_egress_port')
te.match['hdr.ethernet.dst_addr'] = '00:00:00:00:00:1B'
te.action['port_num'] = '4'
te.insert()
It's now time to start an emulated network of stratum_bmv2 switches. To start the topology, used the following command:
$make start
This command will start two Docker containers, one for mininet and one for ONOS.
Added an NDP entry to h1, mapping h2's IPv6 address (2001:1:1::b) to its MAC address (00:00:00:00:00:B):
mininet> h1 ip -6 neigh replace 2001:1:1::B lladdr 00:00:00:00:00:B dev h1-eth0
And vice versa, add an NDP entry to h2 to resolve h1's address
YANG, OpenConfig, and gNMI are used for network configuration on ONOS VM 1: 10.3.12.139 to access p4 based mininet topology on ONOS UI.
$ util/gnmi-cli --grpc-addr 10.3.12.140:50001:50001 get /
$ util/gnmi-cli --grpc-addr 10.3.12.140:50001:50001 get / | util/oc-pb-decoder | less
$ util/gnmi-cli --grpc-addr 10.3.12.140:50001 get \/interfaces/interface[name=leaf1-eth3]/config
$ util/gnmi-cli --grpc-addr 10.3.12.140:50001:50001 \--interval 1000 sub-sample \/interfaces/interface[name=leaf1-eth3]/state/counters/in-unicast-pkts

