#!/bin/bash

SSH_KEY="${1}"
LOG="${2}"

SCRIPT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
now="date +%Y-%m-%d_%H:%M:%S"

echo "$(${now}): cd into ${SCRIPT_PATH}" | tee -a ${LOG}
cd "${SCRIPT_PATH}"

echo "$(${now}) pulling from git" | tee -a ${LOG}
GIT_SSH_COMMAND="ssh -i ${SSH_KEY}" git pull 2>&1 | tee -a ${LOG}

echo "$(${now}) doing update" | tee -a ${LOG}
venv/bin/python gen.py 2>&1 | tee -a ${LOG}

echo "$(${now}) commiting" | tee -a ${LOG}
git add data/ && git commit -m "data update" 2>&1 | tee -a ${LOG}

echo "$(${now}) git status:" | tee -a ${LOG}
git status 2>&1 | tee -a ${LOG}

echo "$(${now}) git push" | tee -a ${LOG}
GIT_SSH_COMMAND="ssh -i ${SSH_KEY} "git push 2>&1 | tee -a ${LOG}

echo "$(${now}) done! :)" | tee -a ${LOG}
