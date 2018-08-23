import java.util.*;


class Solution {
    
    class Sortbynum implements Comparator<int[]>
    {
    // Used for sorting in ascending order of
    // roll number
        public int compare(int[] a, int[] b)
        {
        return a[0] - b[0];
        }
   }
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        
        ArrayList<int[]> index_list = new ArrayList<int[]>();
        for (int i =0;i<n;i++){
            int[] temp = new int[2];
            temp[0] = nums[i];
            temp[1] = i;
            index_list.add( temp );
        }
        Collections.sort(index_list,new Sortbynum());
        int l =0;
        int r = n-1;
        while (index_list.get(l)[0]+index_list.get(r)[0]!=target){
            if (index_list.get(l)[0]+index_list.get(r)[0]<target)
                l += 1;
            else
                r -= 1;
        }
        int[] res = {index_list.get(l)[1],index_list.get(r)[1]};
        return res;       
        
        
    }
}
