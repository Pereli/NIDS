# Feature Description

1.  srcip	(Source IP Address)  
    This feature identifies the IP address of the computer from which the packet transfer began. IP                                         address is a unique address assigned for a computer or any network-based device in any network.
    
2.  sport	(Source Port number) 
    This is the port number at the source end. Port number is a logical address in an operating system.                                     Port number identifies which process the network is communicating with.
    
3.  dstip	(Destination IP Address) - This feature identifies the destination Computer IP address.
4.  dsport	(Destination Port Number) - This feature identifies the port number at destination end.

5.  proto	(Protocol of Communication)
    For a successful transfer of data, both source and destination should follow some common rules like                                     what should be the shape of network packets, what should be the transfer rate, what will indicate                                       the end of communication etc. These all rules are set with a protocol. Thus, features define what                                       protocol each computer involved in communication have used.
    
6.  state - Indicates to the network state according to the protocol used. If state is not used then (-) is added.
7.  dur -	Total duration of communication
8.  bytes -	Source to destination transaction bytes
9.  dbytes -	Destination to Source transaction bytes
10. sttl - Source time to live. Time to live defines the duration for which the sent packet will be valid in network
11. dttl	- Destination time to live
12. sloss	- Source packets retransmitted or dropped
13. dloss	- Destination packets retransmitted or dropped

14. service	- http, ftp, smtp, ssh, dns, ftp-data ,irc  and (-) if not used service. These services make use of protocols stated earlier      in order to carry out predefined tasks that each service performs

15. Sload	- Source transfer rate in bits/sec
16. Dload	- Destination transfer rate in bits/sec
17. Spkts	- Source to destination packet count
18. Dpkts	- Destination to source packet count

19. swin	- Source TCP window advertisement value. A TCP window advertisement determines the maximum amount of data that can be sent         before the sender must wait for an acknowledgement from the receiver.

20. dwin - Destination TCP window advertisement value
21. stcpb	- Source TCP base sequence number. All bytes in a TCP connection are numbered, beginning at a randomly chosen initial sequence    number (ISN). The sequence number is the byte number of the first byte of data in the TCP packet sent.

22. dtcpb	- Destination TCP base sequence number.
23. smeansz	- Mean of the low packet size transmitted by the source
24. dmeansz	- Mean of the low packet size transmitted by the destination
25. trans_depth	- Represents the pipelined depth into the connection of http request/response transaction. HTTP requests and responses      can be pipelined on a connection. Pipelining allows a client to make multiple requests without waiting for each response, allowing a    single TCP connection to be used much more efficiently, with much lower elapsed time.

26. res_bdy_len	- Actual uncompressed content size of the data transferred from the server’s http service.
27. Sjit -	Source jitter (mSec). Jitter is a variation in delay of received packets. It is measure of time synchronization.
28. Djit	- Destination jitter (mSec)
29. Stime	- Start time of communication. This is Unix epoch time representation.
30. Ltime	- Last time or end time of communication.
31. Sintpkt	- Source interpacket arrival time (mSec)
32. Dintpkt	- Destination interpacket arrival time (mSec)
33. tcprtt	- TCP connection setup round-trip time, the sum of ’synack’ and ’ackdat’. These two are indications in TCP connection that      the desired packet have been received by the receiver.

34. synack - TCP connection setup time, the time between the SYN and the SYN_ACK packets.
35. ackdat - TCP connection setup time, the time between the SYN_ACK and the ACK packets.
36. is_sm_ips_ports - If source and destination IP addresses equal and port numbers are equal then, this variable takes value 1 else 0
37. ct_state_ttl - No. for each state (6) according to specific range of values for source/destination time to live (10) (11).
38. ct_flw_http_mthd - No. of flows that has methods such as Get and Post in http service.
39. is_ftp_login - If the ftp session is accessed by user and password then 1 else 0.
40. ct_ftp_cmd - No of flows that has a command in ftp session.
41. ct_srv_src - No. of connections that contain the same service and source IP address in 100 connections according to the last time       (Ltime).
42. ct_srv_dst - No. of connections that contain the same service and destination IP address in 100 connections according to the last       time (Ltime).
43. ct_dst_ltm - No. of connections of the same destination IP address in 100 connections according to the last time (Ltime).
44. ct_src_ ltm - No. of connections of the same source IP address in 100 connections according to the last time (Ltime).
45. ct_src_dport_ltm - No of connections of the same source IP address and the destination port (dsport) in 100 connections according to    the last time (Ltime).
46. ct_dst_sport_ltm - No of connections of the same destination IP address and the source port (sport) in 100 connections according to     the last time (Ltime).
47. ct_dst_src_ltm - No of connections of the same source IP and the destination IP address in in 100 connections according to the last     time (Ltime).