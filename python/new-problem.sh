filename=`echo $1 | sed -e "s/-/_/g"`

if [ -z ${filename} ]
then
    echo "Filename required."
    exit 1
fi

echo "\"\"\"
https://leetcode.com/problems/${1}/


\"\"\"
"> "./problems/${filename}.py"
echo "
python3 -m unittest discover -s \"problems\" -p \"${filename}.py\"
"
