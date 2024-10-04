# list
list = [1,2,3,4,5,6,7,8,9,2,3,4,5,4,4,]

print('type is   :', type(list),list)
print('index   2 :',list[2])
print('index  -1 :',list[-1])
print('index  2: :',list[2:])
print('index  :2 :',list[:2])
print('index 2:5 :',list[2:5])

print('-'*20)

variable = [1,'ram',[2,4,6]]
print('type of 1       :',type(variable[0]))
print('type of ram     :',type(variable[1]))
print('type of [2,4,6] :',type(variable[2]))
print('index   [2][1]  :',variable[2][1])

print('-'*30)

print(list)
print('list count 4  :',list.count(4))
print('find 5 index  :',list.index(5))
print('list lenth    :',len(list))
print('max value     :',max(list))
print('min value     :',min(list))
list.append(" Sam" )
list2=["Sara", "Anitha"]
list.extend(list2)
print('append extend :',list)
list.insert(0,'kumar')
print('0 index inset : ',list)
list.clear()

print('-'*30)

nums=[23,45,647,34,657,2453,163,56,87879]
print(nums)
nums.sort()
print('\nnumbers sort    :',nums)
nums.sort(reverse=True)
print('sort reverse    :',nums)
str=['blue','orangre','apple','red'] # only str
str.sort(key=len)
print('string sort key :',str)