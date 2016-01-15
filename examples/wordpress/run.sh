#!/bin/bash
set -xe

solar resource create nodes templates/nodes count=1
solar repo import /vagrant/solar-resources/examples/wordpress/wp_repo
solar resource create wp_docker wp_repo/docker
