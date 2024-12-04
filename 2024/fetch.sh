#!/bin/bash
if [ -f .env ]; then
    source .env
fi

set -euo pipefail
SCRIPT_DIR=$(realpath "$(dirname "$0")")

if [[ $# != 1 ]]; then
  echo "Please provide a 2-digit day number."
  echo "usage: $0 DD"
  exit 1
fi

if [[ ! "$1" =~ ^(0[1-9]|1[0-9]|2[0-5])$ ]]; then
  echo "Argument '$1' is not a valid day."
  exit 1
fi

if [[ -z "${AOC_SESSION-""}" ]]; then
  echo "No session token set in \$AOC_SESSION."
  exit 1
fi

URL="https://adventofcode.com/2024/day/$((10#$1))/input"
echo "$URL"
curl "$URL" --cookie "session=$AOC_SESSION" -s | tee "$SCRIPT_DIR/inputs/$1.in"