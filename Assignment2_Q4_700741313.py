Sample_List: [1,2,3,3,3,3,4,5]
uniquelist = []
def unqlist(Sample_List):
    for i in Sample_List:
        if i not in uniquelist:
            uniquelist.append(i)
    return uniquelist
print(unqlist([1,2,3,3,3,3,4,5]))