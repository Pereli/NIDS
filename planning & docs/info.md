# Info

This IDS could be used as a complementary feature of a firewall, detecting and eliminating any thread that the firewall have missed.

This dataset recorded the behavior of normal as well as attack network packets. They created a simulation environment using IXIA perfectstorm tool with 3 servers, one of which was configured to generate attack network traffic while other two behaved as normal users. The tcpdump tool was installed on one of the routers on non attack server side to capture 100 GB of the raw traffic in form of pcap files.


Total 2,540,043 data points  in 4 csv
Each csv file has 49 columns in total, 
with 47 features and 2 columns for class labels

 - two formats:
 1. non-attack or attack (0 or 1) `Label`
 2. type of attack `attack_cat`

