#!/bin/bash
set -xe

solar repo import /vagrant/solar-resources/examples/wordpress/wp_repo
solar resource create wp_docker wp_repo/docker
