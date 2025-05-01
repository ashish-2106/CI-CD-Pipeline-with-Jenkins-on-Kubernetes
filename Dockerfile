# Base image
FROM jenkins/jenkins:lts

# Switch to root user to install packages
USER root

# Install Python3 and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Go back to Jenkins user
USER jenkins
