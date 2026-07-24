class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    // [ { pos: 1, time: 3 }, { pos: 4, time: 3 } ] __cars
    carFleet(target, position, speed) {

        const cars = []
        for(let i = 0; i < position.length; i++){
            let pos = position[i]
            let spd =  speed[i]
            let time = (target - pos) / spd
            cars.push({pos, time})
        }
        cars.sort((a,b)=> b.pos - a.pos)
        let fleet = 0
        let maxTime = 0
        for(let i = 0; i < cars.length; i++){
            if(cars[i].time > maxTime){
                maxTime = cars[i].time
                fleet+=1
            }
        }
        return fleet
    }
}
