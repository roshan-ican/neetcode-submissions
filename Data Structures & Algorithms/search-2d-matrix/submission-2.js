class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    binarySearchRow(row, target) {
    let left = 0;
    let right = row.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (row[mid] === target) return true;
        else if (row[mid] < target) left = mid + 1;
        else right = mid - 1;
    }

    return false;
    }
     searchMatrix(matrix, target) {
    //  get the middle one and search
    if(target === 0) return false
    let low = 0 
    let high = matrix.length -1
    
    while(low <=high){
    let mid= Math.floor((low+high)/2)
    let row = matrix[mid]
    let first = row[0]
    let last = row[row.length -1]
    if(target >= first && target <=last){
       return this.binarySearchRow(row, target)
    }else if (target < first) {
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }
    return false
    
 }
}
