#/usr/bin/env bash -e

VENV=venv

if [ ! -d "$VENV" ]
then

    PYTHON=`which python3`

    if [ ! -f $PYTHON ]
    then
        echo "could not find Python 3"
    fi
    $PYTHON -m venv $VENV

fi

. $VENV/bin/activate

pip install -r requirements.txt
