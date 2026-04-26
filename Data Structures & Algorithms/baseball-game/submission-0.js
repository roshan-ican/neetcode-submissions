class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations) {
        	let records = []

	for(let i = 0; i < operations.length; i++){
     
		if(!isNaN(operations[i])){
			records.push(Number(operations[i]))
		}
		else{
			if (operations[i] === "+"){
                records.push(records[records.length - 1] + records[records.length - 2])
			} 
			else if (operations[i] === "D"){
                records.push(records[records.length - 1] * 2)
			}
			else if (operations[i] === "C"){
                records.pop()
			}
			
		}
	}
	return records.reduce((a, b) => a + b, 0)
    }
}