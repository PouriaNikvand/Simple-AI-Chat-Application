# Simple-AI-Chat-Application
This is a Simple AI Chat Application for an interview

Here I explain how I work step by step.

## Reading the assignment and init the Project

here I created a GitHub repository and check the project requirements.

## Design

As the project described what it needs and described the services, I decided to design a simple project.
For this I read the requirements and start to get proper design based on endpoints and how chat apps works. 
note that the project contains these Deliverable API Endpoints:
- Create a new interaction.
- Fetch all interactions.
- Create a message on an interaction.
- Fetch all messages in an interaction.

here I design on my notebook and if i had enough time I will move it to draw.io


### first, we think about what objects are we working with and how it seems to be a chat application:
- Users : using user_id we can have the user objects that contains list of interactions and user infos like name etc.
- Interactions : using interaction_id we can have the meta infos about interactions this could be information like e title and creation timestamp etc.   
- messages : messages that contain message_id, massage string, infos like massage timestamp, also any metadata like any kind of array of transformed string of message etc.   


### second, sample design of the project and what it needed
In this project because of short time we do not discuss details.
- adapters : proper interface for connecting to database of users or object stores that contains any ai based models
- common : common tools and methods that casually we use
- entities : entities interfaces for Users, interactions, Messages, Settings 
- modules : for AI based modules that takes the main process in chat app  
- configs : proper configs based on where the app is running on
- services : for service interface that api uses

## Implementation

### database: 
Choosing mongodb as a main storage and handling two collection for this use case
first collection is used for interactions that the _id in collection is interaction_id, second collection is 
for messages that the _id is the message_id 
#### caching:
we can cache users and interactions for short term using redis database 
### entities:
designing User, Interaction, Message, Settings interfaces for using as a proper object and data validator
#### User:
- user_id
- interaction_list
- (here also we can have the metadata and any details of the user)
#### Interaction:
- interaction_id
- created_at
- updated_at
- settings
- message_list
#### Message:
- interaction_id
- message_id
- created_at
- role
- content
#### Settings:
- model_name
- role
- prompt

## docker
Dockerfile and docker-compose is prepared and also, sample mongodb added to docker-compose

## styling & typecheck
In this project I use black and isort for proper reformation of code and style
Also using lint, typecheck, pyright for checking standards

## exposing metrics
Simple metrics are exposing for prometheus and it's prepared on /metrics path

## adding Swagger for API
It's just prepared as an empty page

Still under development ...

The approximate time for this project was about 8 hours