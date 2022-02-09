#!/bin/bash



helpFunction()
{
   echo ""
   echo "Usage: $0 -s service -t suite"
   echo -e "\t-s Service name for which tests need to be run"
   echo -e "\t-t Test suite type, possible values are [miniqual|qual|fullqual]"
   exit 1 # Exit script after printing help
}

while getopts "s:t" opt
do
   case "$opt" in
      s ) SERVICE="$OPTARG" ;;
      t ) SUITE="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

if [ -z "SERVICE" ]
then
   echo '!!! Service parameter is not provided !!!'
   helpFunction
fi

if [ -z "SUITE" ]
then
  SUITE='miniqual'
fi

python3 ./labs/ideas/ratifier/cli.py run --service $SERVICE --suite SUITE
