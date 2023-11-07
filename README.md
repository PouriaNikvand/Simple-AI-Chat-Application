# Simple-AI-Chat-Application
This is a casual breakdown of how I tackled the programming assignment for the Simple AI Chat Application during an interview. 😊

## Step 1: Let's Begin!
I started by creating a GitHub repository for the project and diving headfirst into the project requirements. This initial step was like putting on my detective hat to understand what I needed to do and what pieces were needed for the chat application.

## Step 2: Designing the Chat Magic 🪄
With a good grasp of what the project required, it was time to work my creative juices. I focused on designing the application and crafting an experience that meets the project's needs. Think of it like drawing a roadmap with key stops, and the stops in this journey were the vital API endpoints:

### Creating new interactions 🙌
### Fetching all interactions 🕵️
### Creating messages in interactions 🗨️
### Fetching all messages in interactions 📬
I started by brainstorming and sketching these essential components on my trusty notebook. If time allowed, I'd even take those doodles and turn them into a fancy visual representation using tools like draw.io.

In this creative process, I thought about some of the main characters in our chat app adventure:

## What we need to do this?
### Users: 🧑
With a user_id, we can find user objects that contain interaction lists and user info, like names.

### Interactions: 💬
Using interaction_id, we gather details about interactions, such as titles and creation timestamps.

### Messages: 📝
Messages come with message_id, message text, timestamps, and maybe some extra metadata, like transformed message content.

## How is the code structure? 
#### I kept things high-level during this phase due to time constraints, but here's what I planned to include:

### Adapters: 🛠️
Think of these as the bridges that connect us to databases holding user data or those magical AI-based models.

### Common: 🛠️
This is where I stored the tools and methods that made the development process smooth and easy.

### Entities: 🕴️
These are like the blueprints for Users, Interactions, Messages, and Settings, helping us create objects and validate data.

### Modules: 🤖
Here's where the AI-based modules worked their magic to power our chat app.

### Configs: 📂
I set up configuration files customized for where the app was running.

### Services: 🌐
This is where I defined interfaces for the services that the API relied on.

## Step 3: Making It Real 🌟
The implementation phase is where we turned our ideas into reality. Here's a sneak peek into what I did:

### Database: 📦
I chose MongoDB as our main storage solution. It handled two collections for this adventure. The first one stored interactions, with interaction_id as the key. The second collection held messages, with message_id as the key.

### Caching: 🕒
I also used Redis to store user and interaction data temporarily. Think of it as a way to quickly grab things we need.

I also introduced you to our main characters:

### User: 🧑
- user_id
- interaction_list
- And there was room for extra details if needed!
### Interaction: 💬
- interaction_id
- created_at
- updated_at
- settings
- message_list
### Message: 📝
- interaction_id
- message_id
- created_at
- role
- content
### Settings: ⚙️
- model_name
- role
- prompt

## Step 4: Go in production ⚙️
Additionally, I set up a Dockerfile and docker-compose and added a sample MongoDB instance to make things even more exciting!

## Step 5: Making It Pretty and Error-Free 🎨
Keeping our code looking sharp and free of mistakes is crucial. So, I used tools like "black" to keep it neat and "isort" to keep the imports in order. I also had linters, type checkers, and tools like pyright to ensure everything met coding standards.

## Step 6: Sharing Our Progress 📊
We're all about transparency here, so I exposed some simple metrics for Prometheus. You can check them out at the "/metrics" endpoint.

## Step 7: Swagger for Everyone! 📚
I even added Swagger documentation for the API. It's like a guidebook that helps users and developers understand what our endpoints do and how to use them.

And last but not least, remember, this project was a work in progress, and it took me approximately 8 hours to get this far. 😅🕒

Let me know if you have any questions or need more details! 🚀