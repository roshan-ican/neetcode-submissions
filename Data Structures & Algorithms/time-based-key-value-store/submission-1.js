class TimeMap {
    constructor() {
        this.keyStore = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        if (!this.keyStore.has(key)){
            this.keyStore.set(key, [])
        }
        this.keyStore.get(key).push([timestamp, value]);
    }
      
    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        if(!this.keyStore.has(key)){
            return ""
        }
        const arr = this.keyStore.get(key)
        let left = 0
        let n = arr.length -1
        let right = n

        let res = ""
        while (left <= right){
            let mid = Math.floor((left + right)/2)
            if(arr[mid][0] === timestamp){
                return arr[mid][1]
            }
              else if (arr[mid][0] < timestamp) {
                res = arr[mid][1];
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
        
    }
}
