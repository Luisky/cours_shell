#!/bin/sh

# find with maxdepth is a GNU exclusive so we'll have to use ls this time
# sorry ShellCheck ! (SC2012)

tree_print() {
    echo "."
    nb_lines=$(ls | wc -l)
    i=0
    for file in *; do

        i=$((i+1))
        if [ $i -eq "$nb_lines" ]; then
            echo "└── $color ${file}"
        else
            echo "├── $color ${file}"
        fi


        if [ -d "${file}" ]; then
            nb_files=$(ls "$file" | wc -l)
            
            if [ "$nb_files" -gt 0 ]; then
                
                j=0
                for x in $(ls "${file}"); do

                    j=$((j+1))
                    if [ $j -eq "$nb_files" ]; then
                        echo "│   └── ${x}"
                    else
                        echo "│   ├── ${x}"
                    fi  
                done
            fi
        fi
    done
}

tree_print