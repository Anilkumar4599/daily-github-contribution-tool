\# Day 72 - AWS Services Cheat Sheet for Beginners



\## 1. Purpose



This cheat sheet provides a simple introduction to commonly used AWS services.



The objective is to understand:



\- What each AWS service does

\- When it is used

\- A simple real-world example

\- How services can work together



This document is designed for beginners who are starting their AWS and DevOps learning journey.



\---



\## 2. AWS Services at a Glance



| AWS Service | Simple Meaning | Common Use |

|---|---|---|

| EC2 | Virtual server | Run applications |

| S3 | Cloud storage | Store files, images, backups |

| RDS | Managed database | Store application data |

| VPC | Private network | Isolate and connect AWS resources |

| IAM | Access control | Manage users and permissions |

| CloudWatch | Monitoring | Monitor resources and applications |

| SNS | Notifications | Send alerts and messages |

| Lambda | Serverless computing | Run code without managing servers |

| ELB | Load balancing | Distribute traffic |

| Auto Scaling | Automatic capacity | Add/remove EC2 instances |

| Route 53 | DNS service | Manage domain names |

| CloudFront | Content delivery | Deliver content faster |

| ECR | Container image registry | Store Docker images |

| ECS | Container service | Run containers |

| EKS | Managed Kubernetes | Run Kubernetes workloads |



\---



\# 3. Detailed Beginner Explanation



\## 3.1 Amazon EC2



\### What is it?



EC2 provides virtual servers in AWS.



\### Simple example



Instead of purchasing a physical server, a company can create an EC2 virtual server in AWS.



\### Common uses



\- Application servers

\- Web servers

\- Development environments

\- Test environments



\### Easy way to remember



\*\*EC2 = Computer/Server in the cloud\*\*



\---



\## 3.2 Amazon S3



\### What is it?



S3 is used to store files and objects.



\### Simple example



A company can store:



\- Reports

\- Images

\- Videos

\- Backup files

\- Application files



\### Easy way to remember



\*\*S3 = Storage\*\*



\---



\## 3.3 Amazon RDS



\### What is it?



RDS is a managed relational database service.



\### Simple example



An application may store customer or transaction information in an RDS database.



\### Easy way to remember



\*\*RDS = Managed Database\*\*



\---



\## 3.4 Amazon VPC



\### What is it?



VPC provides a logically isolated network environment in AWS.



\### Simple example



A company can create a private network for its application servers and databases.



\### Easy way to remember



\*\*VPC = Network\*\*



\---



\## 3.5 AWS IAM



\### What is it?



IAM controls who can access AWS resources and what they are allowed to do.



\### Simple example



A developer may be allowed to view EC2 instances but not delete production resources.



\### Easy way to remember



\*\*IAM = Identity and Access\*\*



\---



\## 3.6 Amazon CloudWatch



\### What is it?



CloudWatch is used for monitoring AWS resources and applications.



\### Example



Monitor:



\- CPU utilization

\- Network activity

\- Logs

\- Application metrics

\- Alarms



\### Easy way to remember



\*\*CloudWatch = Monitoring\*\*



\---



\## 3.7 Amazon SNS



\### What is it?



SNS is a notification service.



\### Example



A CloudWatch alarm detects high CPU usage and sends a notification through SNS.



\### Easy way to remember



\*\*SNS = Notifications\*\*



\---



\## 3.8 AWS Lambda



\### What is it?



Lambda allows code to run without managing a traditional server.



\### Example



A Lambda function can automatically process a file when it is uploaded to S3.



\### Easy way to remember



\*\*Lambda = Run code without managing servers\*\*



\---



\## 3.9 Elastic Load Balancing



\### What is it?



A load balancer distributes incoming traffic across multiple servers.



\### Example



Three EC2 servers are running the same application.



The load balancer distributes customer requests between them.



\### Easy way to remember



\*\*ELB = Distribute traffic\*\*



\---



\## 3.10 Auto Scaling



\### What is it?



Auto Scaling can automatically increase or decrease the number of servers based on demand.



\### Example



Normal traffic:



2 EC2 servers



High traffic:



4 EC2 servers



After traffic decreases:



2 EC2 servers



\### Easy way to remember



\*\*Auto Scaling = Automatically adjust capacity\*\*



\---



\## 3.11 Amazon Route 53



\### What is it?



Route 53 is AWS's DNS service.



\### Example



A user enters:



www.example.com



Route 53 helps direct the request to the appropriate AWS resource.



\### Easy way to remember



\*\*Route 53 = DNS\*\*



\---



\## 3.12 Amazon CloudFront



\### What is it?



CloudFront is a content delivery network (CDN).



It helps deliver content to users from locations closer to them.



\### Example



A company has users in India, Singapore, and Europe.



CloudFront can help deliver website content efficiently from edge locations.



\### Easy way to remember



\*\*CloudFront = Faster content delivery\*\*



\---



\## 3.13 Amazon ECR



\### What is it?



ECR is a container image registry.



It can store Docker container images.



\### Easy way to remember



\*\*ECR = Store container images\*\*



\---



\## 3.14 Amazon ECS



\### What is it?



ECS is a container orchestration service for running containers on AWS.



\### Easy way to remember



\*\*ECS = Run containers\*\*



\---



\## 3.15 Amazon EKS



\### What is it?



EKS is a managed Kubernetes service.



It allows organizations to run Kubernetes workloads on AWS.



\### Easy way to remember



\*\*EKS = Managed Kubernetes\*\*



\---



\# 4. Example ATM Application Architecture



Consider a simple ATM surveillance application running in AWS.



Possible architecture:



```text

&#x20;                   Internet

&#x20;                      |

&#x20;                      v

&#x20;                Route 53

&#x20;                      |

&#x20;                      v

&#x20;               CloudFront / ELB

&#x20;                      |

&#x20;             +--------+--------+

&#x20;             |                 |

&#x20;             v                 v

&#x20;           EC2-01           EC2-02

&#x20;             |                 |

&#x20;             +--------+--------+

&#x20;                      |

&#x20;                      v

&#x20;                     RDS

&#x20;                      |

&#x20;                      v

&#x20;                     S3



Monitoring:

EC2 / Application

&#x20;      |

&#x20;      v

CloudWatch

&#x20;      |

&#x20;      v

SNS

&#x20;      |

&#x20;      v

Support Team

