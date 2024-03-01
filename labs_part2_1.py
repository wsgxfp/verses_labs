    def robots_way(our_list):
    m = len(our_list)
    final_list = []
    for i in range(m):
        if i % 2 == 0:
            final_list.extend(our_list[i])
        else:
            our_list[i].reverse()
            final_list.extend(our_list[i])
    return final_list


our_list = [[1, 5, 7, 10], [110, 2, 6, 32], [1, 2, 22, 43]]

print(robots_way(our_list))




#list_2.append(arr[j][i])

#list_2.append(arr-[j-1],-[i-1])


