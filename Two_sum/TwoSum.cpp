class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /// 将{nums[i] : i} 加入map
        /// 如果匹配到了target - nums[i]在map中，说明此时nums[i] + 内部匹配值 = target
        /// 返回这对key
        map<int, int> m;
        vector<int> result;
        for (int i = 0; i < nums.size(); ++i)
        {
            m[nums[i]] = i;
        }
        for(int i = 0; i < nums.size(); ++i)
        {
            int t = target - nums[i];
            if (m.count(t) && m[t] != i)
            {
                result.push_back(i);
                result.push_back(m[t]);
                break;
            }
        }
        return result;
    }      
};