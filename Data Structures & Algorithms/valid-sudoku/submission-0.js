class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
            // get the rows
    // get the cols
    // get the sub-grid
    const rows = Array.from({ length: 9 }, () => new Set());
    const cols = Array.from({ length: 9 }, () => new Set());
    const subgrids = Array.from({ length: 9 }, () => new Set());
    
    for(let i = 0; i < 9; i++){
        for(let j = 0; j < 9; j++){
            let num = board[i][j]
            if(num === ".") continue
            
            if(rows[i].has(num)) return false
            rows[i].add(num)
            
            if(cols[j].has(num)) return false
            cols[j].add(num)
            
            let boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3)
            if (subgrids[boxIndex].has(num)) return false;
            subgrids[boxIndex].add(num);
        }
    }
    return true
    }
}
