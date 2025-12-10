class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_indexes=[]
        s=[]
        result=[]
        answer=[]
        for string in list1:
            if string in list2:
                common_indexes.append((list1.index(string),list2.index(string)))
            else:
                pass

        for pair in common_indexes:
            s.append(sum(pair))

        min_sum=min(s)
        result=[ idx for idx,val in enumerate(s) if val==min_sum]
        common_indexes=[common_indexes[r] for r in result]

        for idx in common_indexes:
            answer.append(list1[idx[0]])
        return answer
        


          

        