FROM ubuntu:latest
LABEL authors="Kheph"

# Install essentials early so they're available for debugging
RUN apt-get update && apt-get install -y \
    bash \
    dos2unix \
    python3 \
    python3-pip \
    rtl-sdr \
    && rm -rf /var/lib/apt/lists/*

# Copy and fix the install script
COPY install_scripts/install_direwolf.sh /usr/local/bin/install_direwolf.sh
RUN dos2unix /usr/local/bin/install_direwolf.sh \
    && chmod +x /usr/local/bin/install_direwolf.sh \
    && /usr/local/bin/install_direwolf.sh

# Copy application code
COPY /src /app/src
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --break-system-packages

# Copy start script
COPY start.sh /app/start.sh
RUN dos2unix /app/start.sh && chmod +x /app/start.sh

ENTRYPOINT ["/app/start.sh"]
