#!/bin/bash

while read -r line
do
  echo "'$line'"
done < "user_agents.txt"
