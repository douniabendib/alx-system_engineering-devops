
## Specifics about this infrastructure:

# What is a server
Sever is computer program or device that provides a service to another computer program and its user, also known as client.

# What is the role of the domain name
Domain name serves as a human-readable and memorable label for identifying and accessing resources on the internet.

# What type of DNS record www is in www.foobar.com
The DNS record type for "www.foobar.com" is typically an "A" (Address) record.

# What is the role of the web server
Web server is software or hardware or both that handles HTTP requests from web browsers and delivers HTML content.

# What is the role of the application server
Application servers run and manage application providing the necessary runtime environemment for applications to execute.

# What is the role of the database
A database is an organized collection of data that enables simple and efficient storage, retrieval , and modification of data.

# What is the server using to communicate with the computer of the user requesting the website
This communication takes place over the internet, utilizing TCP/IP for data transmission and DNS for domain name resolution.


## The issues are with this infrastructure:
SPOF:
SPOFs are considered a significant vulnerability in any infrastructure and can lead to downtime, data loss and disruption of services.

Downtime when maintenance:
The most immediate and noticeable issue with a SPOF is the potential for downtime. If the single point of failure fails or experiences an issue, it can lead to a complete 
outage of the entire system, causing service interruptions and disrupting operations.

Cannot scale if too much incoming traffic:
The inability to scale when faced with a sudden influx of incoming traffic is a common challenge in managing web services and applications. It often leads to performance issues, service interruptions, and, in some cases, a poor user experience
