To develop P4T, NGSDN tutorial (https://github.com/opennetworkinglab/ngsdn-tutorial/) is used as a reference. We followed some of its exercises, 
and then implemented our own topology. Additionally, we made some changes in the gNMI CLI 
to remotely access the ONOS controller. This testbed leverages the power of P4-based BMv2
switches and Mininet and provides a comprehensive but simplified platform to simulate 
SDN-based network topology.

* Advanced data plane programming and control via P4 and P4Runtime
* Robust configuration using YANG, OpenConfig, and gNMI
* The Stratum switch OS
* The ONOS SDN controller

## System requirements

1. Download a pre-packaged VM with all included; **OR**
2. Manually install Docker and other dependencies.

The following components are required for manual Docker installation:

* Docker v1.13.0 and later (with docker-compose)
* Python 3
* Bash-like Unix shell
* Wireshark (optional)

We build our SDN experimental setup and application development stack by combining free and
open-source components. Our main computing resource was a Huawei server outfitted with a powerful
Xeon processor. We used 32 GB of RAM at our disposal to execute memory-intensive operations and 
allocated to two virtual machines (VMs) developed for our testing. The Mininet and BMv2 components 
were hosted in a single VM1 with 16 GB of RAM. The VM2 was given 10 GB of RAM and was used to install 
ONOS instances. The server included SAS storage with a 2TB storage capacity for data storage. We also
assigned a 200 GB virtual hard disk drive (VHDD) for specialized storage and virtualization requirements. 
To develop and administer our network emulations, we used Mininet version 2.3.1. The Linux distribution 
we used was Ubuntu 20.04.5. As our major computing resource, we used an Intel(R) Xeon(R) Silver 4210 CPU, 
equipping the system with 6 virtual CPUs (vCPUs) to efficiently spread processing workloads. Our virtualization 
infrastructure was built on VMware ESXi version 7.0 U2, a solid platform that provided us with advanced 
virtualization capabilities, boosting the efficiency of our tests even further. This extensive experimental 
setup gave us the computational capacity and resources we needed to conduct our research efficiently.

## Get this repo or pull latest changes

To work on the exercises you will need to clone this repo:

    cd ~  git clone -b advanced https://github.com/opennetworkinglab/ngsdn-tutorial

If the `ngsdn-tutorial` directory is already present, make sure to update its
content:

    cd ~/ngsdn-tutorial
    git pull origin advanced

## Download / upgrade dependencies

Upgrade the dependencies to the latest version using the
following command:

    cd ~/ngsdn-tutorial
    make deps

## Repo structure

This repo is structured as follows:

 * `p4src/` P4 implementation
 * `yang/` Yang model used in exercise 2
 * `app/` custom ONOS app Java implementation
 * `mininet/` Mininet script to emulate a 2x2 leaf-spine fabric topology of
   `stratum_bmv2` devices
 * `util/` Utility scripts
 * `ptf/` P4 data plane unit tests based on Packet Test Framework (PTF)

## Tutorial commands

To facilitate working on the exercises, A set of make-based commands are provided
to control the different aspects of the tutorial. Commands will be introduced in
the exercises, here's a quick reference:

| Make command        | Description                                            |
|---------------------|------------------------------------------------------- |
| `make deps`         | Pull and build all required dependencies               |
| `make p4-build`     | Build P4 program                                       |
| `make p4-test`      | Run PTF tests                                          |
| `make start`        | Start Mininet and ONOS containers                      |
| `make stop`         | Stop all containers                                    |
| `make restart`      | Restart containers clearing any previous state         |
| `make onos-cli`     | Access the ONOS CLI (password: `rocks`, Ctrl-D to exit)|
| `make onos-log`     | Show the ONOS log                                      |
| `make mn-cli`       | Access the Mininet CLI (Ctrl-D to exit)                |
| `make mn-log`       | Show the Mininet log (i.e., the CLI output)            |
| `make app-build`    | Build custom ONOS app                                  |
| `make app-reload`   | Install and activate the ONOS app                      |
| `make netcfg`       | Push netcfg.json file (network config) to ONOS         |

## Exercises

Click on the exercise name to see the instructions:

 1. [P4Runtime basics](./EXERCISE-1.md)
 2. [Yang, OpenConfig, and gNMI basics](./EXERCISE-2.md)
 3. [Using ONOS as the control plane](./EXERCISE-3.md)
 4. [Enabling ONOS built-in services](./EXERCISE-4.md)
 5. [Implementing IPv4 routing with ECMP](./EXERCISE-5.md)

