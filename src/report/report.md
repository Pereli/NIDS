
# Introduction
As cyber attacks continue to increase in frequency and sophistication, it is crucial for businesses to have strong defenses in place to protect their sensitive data and systems. While firewalls serve as a first line of defense, they can often be bypassed by attackers. That's where an intrusion detection system (IDS) comes in. An IDS uses machine learning techniques to analyze network activity and identify suspicious activity that may indicate a potential threat. In this project, I developed an IDS using machine learning to provide additional support to a firewall, with the goal of increasing the success rate in detecting threats.

# Models
I tested several machine learning models in order to find the most effective approach for our IDS. These models included Regression, Boosting, Random Forest and Neural Networks.



# Most Impactful Variables
The top feature importance variables were:

- sttl: Source to destination time to live value, a measure of the time a packet can remain in the network before being discarded. This could be useful for detecting packets that are attempting to remain in the network for longer than usual, which could be a sign of an attempt to infiltrate the network.

- ct_state_ttl: A combination of the "state" and "ttl" functions, indicating the number of connections in specific states (such as "INT") according to specific ranges of values for source/destination time to live. This could be useful for detecting connections in certain states that may be unusual or potentially malicious.

- Rate: A sudden increase could indicate DoS attack.

- Dload: High unusual dload could indicate someone is trying to send data as quickly as possible for example trying to install malware.

- These features account for about half of the total relevance of the data.

# Conclusions
My results showed that machine learning is a powerful tool for detecting and preventing cybersecurity threats, and is increasingly relevant in today's digital landscape.

By implementing an IDS using machine learning, companies can greatly enhance their ability to defend against cyber attacks and protect their critical assets. This technologies has the potential to revolutionize the way we think about cybersecurity.

# Business solutions
- Cybersecurity threats: An IDS can help protect a company's network and data from cyber attacks by detecting and alerting the company to any suspicious activity.

- Data breaches: An IDS can help prevent data breaches by alerting the company to any unauthorized access to sensitive information.

- Compliance: An IDS can help a company ensure compliance with industry regulations and standards related to cybersecurity.

- Reputation: A successful data breach or cyber attack can harm a company's reputation and lead to a loss of customer trust. An IDS can help prevent these types of incidents from occurring.
