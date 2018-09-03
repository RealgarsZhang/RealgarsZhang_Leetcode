def maxSubseq(merged_list,k):
        res = merged_list[:k]# here it should be a linked list!
        prog = k
        while prog<len(merged_list):
            res.append(merged_list[prog])
            for i in range(k+1):
                if i==k or res[i]<res[i+1]:
                    res.pop(i)
                    break
            prog +=1
                    
        return res
    
def merge(nums1,nums2):
        merged_list = []
        p1 = 0
        p2 = 0
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]>nums2[p2]:
                merged_list.append(nums1[p1])
                p1 += 1
            elif nums1[p1]<nums2[p2]: 
                merged_list.append(nums2[p2])
                p2 += 1
            else:
                p1_start = p1
                p2_start = p2
                while p1<len(nums1) and p2<len(nums2) and nums1[p1] == nums2[p2]:
                    p1 += 1
                    p2 += 1
                    
                if p1==len(nums1) or (p2<len(nums2) and nums1[p1]<nums2[p2]):
                    p2 = p2_start
                    while p2<len(nums2) and nums2[p2] == nums2[p2_start]:
                        p2+=1
                        
                    merged_list += nums2[p2_start:p2]
                    
                    p1 = p1_start
                    
                else:
                    p1 = p1_start
                    while p1<len(nums1) and nums1[p1] == nums1[p1_start]:
                        p1+=1
                        
                    merged_list += nums1[p1_start:p1]
                    
                    p2 = p2_start
        if p1<len(nums1):
            merged_list += nums1[p1:]
        if p2<len(nums2):
            merged_list += nums2[p2:]
        
        return merged_list

def listComp(list1,list2):
    for i in range(len(list1)):
        if list1[i]<list2[i]:
            return -1
        elif list1[i]>list2[i]:
            return 1
    
    return 0

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0]*k
        for i in range(0,k+1):
            if i<=len(nums1) and k-i<=len(nums2):
                list1 = maxSubseq(nums1,i)
                list2 = maxSubseq(nums2,k-i)
                temp = merge(list1,list2)
                if listComp(temp,res)>0:
                    res = temp
                    #print list1
                    #print list2
        return res
  
