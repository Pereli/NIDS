# Info

This IDS could be used as a complementary feature of a firewall, detecting and eliminating any thread that the firewall have missed.

This dataset recorded the behavior of normal as well as attack network packets. They created a simulation environment using IXIA perfectstorm tool with 3 servers, one of which was configured to generate attack network traffic while other two behaved as normal users. The tcpdump tool was installed on one of the routers on non attack server side to capture 100 GB of the raw traffic in form of pcap files.


Total 2,540,043 data points  in 4 csv
Each csv file has 49 columns in total, 
with 47 features and 2 columns for class labels

 - two formats:
 1. non-attack or attack (0 or 1) `Label`
 2. type of attack `attack_cat`


In our heatmap of correlation we can see the next correlations:
- sbytes, sloss
- dpkts, dbytes, dloss
- sttl, ct_state_ttl, label
- swin, dwin
- stime, dtime
- tcprtt, synack, ackdat
- ct_srv_src, ct_dst_src_ltm, ct_srv_dst
- ct_dst_ltm, ct_src_ltm, ct_src_dport_ltm, ct_dst_sport_ltm



Feature description :

 	No.     Name 	        Type 	    Description
0 	1 	    srcip 	        nominal 	Source IP address
1 	2 	    sport 	        integer 	Source port number
2 	3 	    dstip 	        nominal 	Destination IP address
3 	4 	    dsport 	        integer 	Destination port number
4 	5 	    proto 	        nominal 	Transaction protocol
5 	6 	    state 	        nominal 	Indicates to the state and its dependent proto...
6 	7 	    dur 	        Float 	    Record total duration
7 	8 	    sbytes 	        Integer 	Source to destination transaction bytes
8 	9 	    dbytes 	        Integer 	Destination to source transaction bytes
9 	10 	    sttl 	        Integer 	Source to destination time to live value
10 	11 	    dttl 	        Integer 	Destination to source time to live value
11 	12 	    sloss 	        Integer 	Source packets retransmitted or dropped
12 	13 	    dloss 	        Integer 	Destination packets retransmitted or dropped
13 	14 	    service         nominal 	http, ftp, smtp, ssh, dns, ftp-data ,irc and ...
14 	15 	    Sload 	        Float 	    Source bits per second
15 	16 	    Dload 	        Float 	    Destination bits per second
16 	17 	    Spkts 	        integer 	Source to destination packet count
17 	18 	    Dpkts 	        integer 	Destination to source packet count
18 	19 	    swin 	        integer 	Source TCP window advertisement value
19 	20 	    dwin 	        integer 	Destination TCP window advertisement value
20 	21 	    stcpb 	        integer 	Source TCP base sequence number
21 	22 	    dtcpb 	        integer 	Destination TCP base sequence number
22 	23 	    smeansz         integer 	Mean of the ?ow packet size transmitted by the...
23 	24 	    dmeansz         integer 	Mean of the ?ow packet size transmitted by the...
24 	25 	    trans_depth     integer     Represents the pipelined depth into the connec...
25 	26 	    res_bdy_len     integer     Actual uncompressed content size of the data t...
26 	27 	    Sjit 	        Float 	    Source jitter (mSec)
27 	28 	    Djit 	        Float 	    Destination jitter (mSec)
28 	29 	    Stime 	        Timestamp 	record start time
29 	30 	    Ltime 	        Timestamp 	record last time
30 	31 	    Sintpkt 	    Float 	    Source interpacket arrival time (mSec)
31 	32 	    Dintpkt 	    Float 	    Destination interpacket arrival time (mSec)
32 	33 	    tcprtt 	        Float 	    TCP connection setup round-trip time, the sum ...
33 	34 	    synack 	        Float 	    TCP connection setup time, the time between th...
34 	35 	    ackdat 	        Float 	    TCP connection setup time, the time between th...
35 	36 	    is_sm_ips_ports Binary 	    If source (1) and destination (3)IP addresses ...
36 	37 	    ct_state_ttl 	Integer 	No. for each state (6) according to specific r...
37 	38 	    ct_flw_http_mthd Integer 	No. of flows that has methods such as Get and ...
38 	39 	    is_ftp_login 	Binary 	    If the ftp session is accessed by user and pas...
39 	40 	    ct_ftp_cmd 	    integer 	No of flows that has a command in ftp session.
40 	41 	    ct_srv_src 	    integer 	No. of connections that contain the same servi...
41 	42 	    ct_srv_dst 	    integer 	No. of connections that contain the same servi...
42 	43 	    ct_dst_ltm 	    integer 	No. of connections of the same destination add...
43 	44 	    ct_src_ ltm 	integer 	No. of connections of the same source address ...
44 	45 	    ct_src_dport_ltm integer 	No of connections of the same source address (...
45 	46 	    ct_dst_sport_ltm integer 	No of connections of the same destination addr...
46 	47 	    ct_dst_src_ltm 	integer 	No of connections of the same source (1) and t...
47 	48 	    attack_cat 	    nominal 	The name of each attack category. In this data...
48 	49 	    Label 	        binary 	    0 for normal and 1 for attack records