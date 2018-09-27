import re
from pprint import pprint
# with open('text.txt', 'r') as read_file:
#     for line in read_file:
#         line = line.rstrip()
#         if re.search('peculiar', line):
#             print(line)

            # ||

# with open('text.txt', 'r') as read_file:
#     for line in read_file:
#         line = line.rstrip()
#         if line.find("peculiar") >= 0 :
#             print(line)

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# test_string = "asd 9 asdf 34 asdf.l. 23 asli"
# results = re.findall('[0-9]+', test_string)        # figure out all the matching instances and list all the items matched
# pprint(results)


# match but extract what I want -> extract only those items which matches with regex in `()`
# test_string = "From prakanad@in.ibm.com Sat June 26 2018"
# results = re.findall('^From (\S+@\S+)', test_string)
# pprint(results)


# find out the domain name from the above string
test_string = "From prakanad@in.ibm.com Sat June 26 2018"
results = re.findall('@(\S+) ', test_string)
pprint(results)