class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let k = 1

        while(true){
            let hours = 0
            for(let i =0; i < piles.length; i++){
                hours += Math.ceil(piles[i]/k)
            }
            if(hours <= h){
                return k
            }
            k++
        }
        
       
    }
}
