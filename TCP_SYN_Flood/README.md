## Basic TCP-SYN Flood

### This folder shows how to implement a TCP_SYN Flood.

+-----------+                          +--------+                          +------------------+
|  Attacker |                          | Target |                          | Resource Allocated|
+-----------+                          +--------+                          +------------------+

      |                                      |                                       |
      | ----------- SYN -------------------> |                                       |
      |                                      | -- Allocates half-open connection --->||
      |                                      |                                       ||
      |                                      | <----------- SYN-ACK ---------------- ||
      |                                      |                                       ||
      |  (Attacker never sends ACK)          |                                       ||
      |                                      |                                       ||
      | ----------- SYN -------------------> |                                       ||
      |                                      | -- Allocates another half-open conn ->|||
      |                                      | <----------- SYN-ACK ---------------- |||
      |                                      |                                       |||
      |                                      |                                       |||
      | ----------- SYN -------------------> |                                       |||
      |                                      | -- Allocates another half-open conn ->||||
      |                                      | <----------- SYN-ACK ---------------- ||||
      |                                      |                                       ||||
      |                                      |                                       ||||
... (Repeated many times)                    |                                       ||||


###Executing Files:

#### syn_flooding.py:

Download the code and then
**python3 syn_flooding.py**
