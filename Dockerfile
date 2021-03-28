FROM python:3.8-slim

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
RUN chmod +x /app/init_container.sh

EXPOSE 8000

# Run the bash script to start Flask
ENTRYPOINT [ "/app/init_container.sh" ]


