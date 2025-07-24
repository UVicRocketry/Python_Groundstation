FROM ubuntu:latest
LABEL authors="Kheph"
COPY install_scripts/install_direwolf.sh /usr/local/bin/install_direwolf.sh
RUN chmod +x /usr/local/bin/install_direwolf.sh
RUN /usr/local/bin/install_direwolf.sh
RUN apt-get update && apt-get install -y python3 python3-pip && apt-get install -y rtl-sdr
COPY /src /app/src
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --break-system-packages

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh
ENTRYPOINT ["/app/start.sh"]