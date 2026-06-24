impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> Vec<i32> {
        let mut maj:HashMap<i32, i32> = HashMap::new();
        let mut res = Vec::new();
        let times = nums.len() / 3;

        for &num in &nums {
            if maj.contains_key(&num){
                maj.insert(num, maj[&num] + 1);
            } else{
                maj.insert(num, 1);
            }
        }
        for (key, value) in &maj {
            if *value > times as i32{
                res.push(*key)
            }
        }
        return res
    }
}
