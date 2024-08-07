#!/usr/bin/bash

name=$1
hello(){
        echo "hiiii $1"
        echo "script name:$0"
        echo "number of arguments: $#"
        echo "all arguments are : $@"
}
echo "before calling function,checking name:$1"
echo "number of arguments: $#"
echo "all arguments are : $@"

hello $1
