filename=`echo $1 | sed -e "s/-/_/g"`
echo "\"\"\"
https://leetcode.com/problems/${1}/description/


\"\"\"
"> "./problems/${filename}.py"
echo "
python3 -m unittest discover -s \"problems\" -p \"${filename}.py\"
"
