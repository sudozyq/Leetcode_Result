class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> nums3;
        int length;
        
        /// 如果两数组为空返回错误
        if(nums1.size() == 0 && nums2.size() == 0)
            return -1;
        /// 如果其中一个数组为空返回另一个的中间值
        else if(nums1.size() == 0)
            return (nums2[(nums2.size() - 1) / 2] + nums2[nums2.size() / 2]) / 2;
        else if(nums2.size() == 0)
            return (nums1[(nums1.size() - 1) / 2] + nums1[nums1.size() / 2]) / 2;
        
        
        for (vector<int>::iterator i = nums1.begin(), j = nums2.begin(); ;)
        {
            if(i == nums1.end())
            {
                while(j != nums2.end())
                {
                    nums3.push_back(*j);
                    j++;
                }
                break;
            }
            else if(j == nums2.end())
            {
                while(i != nums1.end())
                {
                    nums3.push_back(*i);
                    i++;
                } 
                break;
            }
            
            if(*i < *j)
            {
                nums3.push_back(*i);
                i++;
            }
            else
            {
                nums3.push_back(*j);
                j++;
            }
        }
        
        return (nums3[(nums3.size() - 1) / 2] + nums3[nums3.size() / 2]) / 2;
        
    }
};