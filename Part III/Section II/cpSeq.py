# Shallow copy
# Share same Object reference code

v1 = [0, 0]
v2 = [0, 0]
line1 = [v1, v2]
print("line1[0]::{} and line1[1]::{}\nline1::{}".format(hex(id(line1[0])), hex(id(line1[1])), line1))

line2 = line1.copy()
print('line1 is line2: {}'.format(line1 is line2))
print('line1::{} and line2::{}'.format(hex(id(line1)),hex(id(line2))))
print("line1[0]::{} == line2[0]::{} \nline1[1]::{} == line2[1]::{}".format( \
    hex(id(line1[0])), 
    hex(id(line1[1])),
    hex(id(line2[0])), 
    hex(id(line2[1]))
))

# Affect line1 will refelect line2
line1[0][0] = 100 
print("line1::{} and lin2:{}\nline1::{} and line2::{}".format(line1,line2, hex(id(line1)), hex(id(line2))))





# Deep Copy
# Create new reference Object Under the Hood

v1 = [0, 0]
v2 = [0, 0]
line1 = [v1, v2]
import copy
line3 = copy.deepcopy(line1)
print('line1 is line3: {}'.format(line1 is line3))
print('line1::{} and line3::{}'.format(hex(id(line1)),hex(id(line3))))
print("line1[0]::{} == line3[0]::{} \nline1[1]::{} == line3[1]::{}".format( \
    hex(id(line1[0])), 
    hex(id(line1[1])),
    hex(id(line3[0])), 
    hex(id(line3[1]))
))

#line1 will not refelect line3
line1[0][0] = 100 
print("line1::{} and line3:{}\nline1::{} and line3::{}".format(line1,line3, hex(id(line1)), hex(id(line3))))



colors = (('crimson','ruby'),'brick','scarlet','maroon')
pseduo_colors_1 = copy.deepcopy(colors)  
print("is colors and pseduo colors share same object {}".format(colors is pseduo_colors_1))  # <<True
print("{} and id::{}".format(colors,hex(id(colors))))
print("{} and id::{}".format(pseduo_colors_1,hex(id(pseduo_colors_1))))

# In tuples, share same ref even deep copy, anyway we can't mutate. Optimization purpose