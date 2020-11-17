# InstituteChatbot
An intra-network chatbot made with focus on aiding professional communication within educational institutes

## Requirements 
- Docker - For running parallel inter-communicating processes
- RASA - Chatbot development framework

## Steps to run the program
### 1. Train the bot
` docker run --user 1000 -v $(pwd):/app rasa/rasa:1.10.8-full train `

### 2. Run server network
#### Create a network
` docker network create netw `

#### Start action server (first time)
` docker run --user 1000 -d -v $(pwd)/actions:/app/actions --net netw --name action-server rasa/rasa-sdk:2.0.0a1 `

#### Start action server
` docker start action-server `

#### Start rasa server
` docker run --user 1000 -it -v $(pwd):/app -p 5005:5005 --net netw rasa/rasa:1.10.8-full run -m models --enable-api --cors "*" --debug `
