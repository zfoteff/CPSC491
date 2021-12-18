Software Design Architecture
====================

# Zoom mechanism
Levels of abstraction around architecture
* Context: Big picture, no details
* Containers: Seperately runnable, deployable application/s
* Components: Software services inside containers
    * Details responsibilities 
* Sequence: Communication and data flow
* Code (On-Demand): How do we implement the services in code
    * UML

# High Level Archtecture Patterns
Patterns are implemented to help increase scale of an application

* Layered: All architecture layers are segmented from each other and must be handled properly
    * Some layers can be oen or closed 
    * Open: Requests can pass through a layer if they are not needed
    * Closed: Requests cannot pass through layer without being processed
* Client - Server: Client's call on the server to (IMPORTANT)
    * Generally accomplished using HTTP request protocol
* Controller - Responder
    * Also known as Master/Replica
    * Similar to replication process of database
    * Backing up databases is implementation of this model
        * Must have 3 minimum backups 
* Microkernel
    * Also known as Plug and Play
    * Allows pogrammers to increase the functionality of their application with external additions. Gives users more customizability
* Microservices
    * Application is collection of smaller services that can be individaully called through an API
    * What makes this distinct from Client/Server architecture is that each service stores their data seperately from the main app and the other services 
        * Every service has their own architecture
        * May still be common data repositories to all the services
* Event-driven
    * Streams of events represent actions user takes, events are processed individually to create indended 
    * Event: Something that happens in the world
    * Publisher - Subscriber pattern
* Messaging/broker
    * Similar to the Event-driven architecture except messages are consumed from a topic of messages
    * Messages are pushed through the system on an event system, rather than waiting for a subscriber to consume the event on their own pace
    * Broker acts as its own server
    * Need to ensure the broker can handle millions of tiny packets of information a second, and route that data properly
        * Requires proper optimization of the subscription hash table
* Distributed / space-based / cloud computing
    * Newest architecture pattern in the modern age
    * Scale out instead of up
* Pipe Filter
    * Basic idea: View everything between service 1 and service 2 as a pipe
        * Transforms are placed in the middle of the flow to convert data from one from to another as it travels from point a to point b
        * Essentially comprised of multiple adaptors 

# Tips for constructing architectures
* Start abstract then zoom in
* Iterate
* Capture high-level reqs
* Some things must be planned from the start
    * Complience & Security 
    * Scale
    * Operations/Managabiltiy
* Go beyond reqs in thinking
    * Often don't implement right away, but be ready at any time
* Capture non-functional requirements
* Enable, don't dictate
* Avoid marketing: Don't let bullet points of a framework entice you if it does not fit the requirements of the project