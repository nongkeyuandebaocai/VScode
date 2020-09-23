height=[1,8,6,2,5,4,8,3,7]
i=0
j=len(height)-1
max_area=0
while(i<j):
    if height[i]<height[j]:
        min_height=height[i]
        i=i+1
    else:
        min_height=height[j]
        j=j-1
    area=(j-i+1)*min_height
    max_area=max(max_area,area)
