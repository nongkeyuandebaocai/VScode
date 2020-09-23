nums=[-1,0,1,2,-1,-4]
nums.sort()
list1=[]
for k in range(len(nums)-2):
    i,j=k+1,len(nums)-1
    if nums[k]>0:
        break
    if k>0 and nums[k]==nums[k-1]:
        continue
    while i<j:
        s=nums[i]+nums[j]+nums[k]
        if s>0:
            j=j-1
        elif s<0:
            i=i+1
        else:
            list1.append([nums[i],nums[j],nums[k]])
            i=i+1
            j=j-1
            while i<j and nums[i]==nums[i-1]:i=i+1
            while i<j and nums[j]==nums[j+1]:j=j-1
print(list1)
           
        
       
