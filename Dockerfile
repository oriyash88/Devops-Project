# Use the official Node.js 16.14 image as the base image
FROM node:16.14

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install 

# Copy the code from your host to your current location
COPY . .

# Set the command to run your React app
CMD ["npm", "start"]
