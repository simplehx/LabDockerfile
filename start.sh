#!/bin/bash
jupyter-lab --allow-root &
/usr/sbin/sshd -D
