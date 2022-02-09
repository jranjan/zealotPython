#!/bin/bash
#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: $0 -s service -t suite"
   echo -e "\t-s Service name for which tests need to be run"
   echo -e "\t-t Test suite type, possible values are [miniqual|qual|fullqual]"
   exit 1 # Exit script after printing help
}

while getopts "a:b" opt
do
   case "$opt" in
      a ) SERVICE="$OPTARG" ;;
      b ) SUITE="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

if [ -z "SERVICE" ] || [ -z "$parameterB" ] || [ -z "$parameterC" ]
then
   runall
   helpFunction
else;
  runone
fi


# Begin script in case all parameters are correct
echo "$parameterA"
echo "$parameterB"
echo "$parameterC"
