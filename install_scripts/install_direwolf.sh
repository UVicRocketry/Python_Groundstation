#!/bin/bash

set -e

apt-get update
apt-get install -y \
  git \
  cmake \
  g++ \
  libasound2-dev \
  libudev-dev \
  libgps-dev \
  libfftw3-dev \
  libpng-dev \
  libsdl2-dev \
  pulseaudio \
  wget \
  curl \
  make


cd /opt
git clone https://github.com/wb2osz/direwolf.git
cd direwolf
mkdir build && cd build
cmake ..
make -j$(nproc)
make install
make install-conf
echo "Direwolf installed successfully"
