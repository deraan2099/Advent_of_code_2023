import re
import os

#Star1
numbers = []
regex = "(\d)"
with open(os.getcwd()+"/day1/input1.rtf") as infile:
    for line in infile:
        re_groups = re.findall(regex,line)
        numbers += [int(re_groups[0]+re_groups[-1])]
print(sum(numbers))

#Star2
file_path = os.getcwd()+"/day1/input1.rtf"
test_file = os.getcwd()+"/day1/test.rtf"
valuesa = []
numbers2 = []
regex2 = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
conv_dict = {"one":"1", "two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
with open(file_path) as infile:
    for line in infile:
        #print(line)
        re_groups = re.findall(regex2,line)
        first = conv_dict[re_groups[0]] if re_groups[0].isalpha() else re_groups[0]
        last = conv_dict[re_groups[-1]] if re_groups[-1].isalpha() else re_groups[-1]
        valuesa += [first+last]
        numbers2 += [int(first+last)]
print(sum(numbers2))

