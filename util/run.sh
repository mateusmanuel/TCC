#/bin/bash

TARGET_CLASS=$1
PATH_PROJECT=$2
SUBPATH_PROJECT=$3
TIME=1

for TIME in `seq 1 1 30`
do
    cd $PATH_PROJECT
    mvn clean compile

    $EVOSUITE -class $TARGET_CLASS -projectCP target/classes -Dsearch_budget=$TIME -Dalgorithm=STANDARD_GA -Doutput_variables=search_budget,TARGET_CLASS,Coverage,Total_Time

    rm -r src/test  
    mkdir -p src/test/java/$SUBPATH_PROJECT
    cp evosuite-tests/$SUBPATH_PROJECT/*.java src/test/java/$SUBPATH_PROJECT

    mvn clover:setup test clover:aggregate clover:save-history
done
