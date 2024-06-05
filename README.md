
This in-depth tutorial focuses on the core components of the next-generation SDN (NG-SDN) architecture, including:

* Advanced data plane programming and control via P4 and P4Runtime
* Robust configuration using YANG, OpenConfig, and gNMI
* The Stratum switch OS
* The ONOS SDN controller

The sessions are organized into a series of practical, hands-on exercises that
demonstrate how to build a leaf-spine data center fabric based on IPv4, using P4, 
Stratum, and ONOS. These exercises are intended for those with an intermediate 
understanding of the P4 language and a basic knowledge of Java and Python. The 
exercises will cover key concepts such as:

* Utilizing Stratum APIs (P4Runtime, gNMI, OpenConfig, gNOI)
* Integrating ONOS with devices programmed with custom P4 programs
* Developing ONOS applications to implement complex control plane logic
  (bridging, routing, ECMP, etc.)
* Testing with bmv2 in Mininet
* Conducting PTF-based P4 unit tests

## System requirements

1. Download a pre-packaged VM with all included; **OR**
2. Manually install Docker and other dependencies.

All exercises can be executed by installing the following dependencies:

* Docker v1.13.0+ (with docker-compose)
* make
* Python 3
* Bash-like Unix shell
* Wireshark (optional)

## Get this repo or pull latest changes

To work on the exercises you will need to clone this repo:

    cd ~
    git clone -b advanced https://github.com/opennetworkinglab/ngsdn-tutorial

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

