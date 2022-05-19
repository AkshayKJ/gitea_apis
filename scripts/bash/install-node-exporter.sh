#!/bin/bash

wget https://github.com/prometheus/node_exporter/releases/download/v0.16.0-rc.1/node_exporter-0.16.0-rc.1.linux-amd64.tar.gz
tar xvfz node_exporter-0.16.0-rc.1.linux-amd64.tar.gz
mv node_exporter-0.16.0-rc.1.linux-amd64 node_exporter
cd node_exporter
./node_exporter