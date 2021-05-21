FROM python:3.8-slim

# SSH password
ENV SSH_PASSWD "root:PythonAzureDevOpsContainerized!"

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
COPY sshd_config /etc/ssh/

# Install needed packages for SSH
RUN apt-get update \
    && apt-get install -y --no-install-recommends dialog \
    && apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "$SSH_PASSWD" | chpasswd \
    && chmod +x /app/init_container.sh

EXPOSE 8000 2222

# Run the bash script to start Flask
ENTRYPOINT [ "/app/init_container.sh" ]


