#!/bin/bash

_term() { 
  echo "Caught SIGTERM, waiting 10 seconds"
  sleep 10
  kill -TERM "$child" 2>/dev/null
}

trap _term SIGTERM

/sbin/munged -F &

child=$!
wait "$child"