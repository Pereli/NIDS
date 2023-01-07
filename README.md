# Overview
This IDS uses machine learning to analyze network traffic and identify potential malicious activity or policy violations. It was trained on a dataset of over 2.5 million data points, including both normal and attack traffic from a simulated network environment.

[UNSW-NB15 Sydney University](https://research.unsw.edu.au/projects/unsw-nb15-dataset)

[Moustafa Nour and Jill Slay research](https://ieeexplore.ieee.org/abstract/document/7348942)


# Models & Evaluation
Supervised models and neural networks was used in this project, aswell as feature importance for presentation purposes.
evaluated using precision, recall, f1-score and accuracy metrics, 
Accuracy went from 0.92 to 0.99990 in the best model on the test set.

# Deployment
The IDS can be used as a complementary feature of a firewall, detecting and alerting on any threats that the firewall may have missed.

# Conclusion
Overall, this machine learning intrusion detection system project has provided valuable insights and experience. While the final accuracy is good, I recognize that there are limitations to this project that could potentially impact its performance in a real-world scenario. For example, I did not have the opportunity to test the system in a production environment or evaluate it with data outside of my dataset. Moving forward, I plan to consider alternative approaches that may address these limitations and improve the robustness of the system.


# References

Papers:

https://www.tandfonline.com/doi/abs/10.1080/19393555.2015.1125974

https://ieeexplore.ieee.org/abstract/document/7948715

https://link.springer.com/chapter/10.1007/978-3-319-59439-2_5

https://arxiv.org/abs/2011.09144

https://link.springer.com/chapter/10.1007/978-3-030-72802-1_9

Posts & Articles:

https://www.kaggle.com/code/carlkirstein/unsw-nb15-modelling-97-7#list-tab

https://medium.com/@subrata.maji16/building-an-intrusion-detection-system-on-unsw-nb15-dataset-based-on-machine-learning-algorithm-16b1600996f5

https://www.kaggle.com/code/khairulislam/unsw-nb15-eda

https://medium.com/@shailvestein/network-intrusion-detection-system-using-machine-learning-ea59a7fd0bb4

https://medium.com/@mangeshchoudhari/application-of-machine-learning-in-network-intrusion-detection-systems-48490ec6740e