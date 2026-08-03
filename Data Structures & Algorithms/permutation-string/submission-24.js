class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        let i = 0;
        let j = 0;
        let seen1 = {};
        let seen2 = {};

        for (let i = 0; i < s1.length; i++) {
            seen1[s1[i]] = (seen1[s1[i]] || 0) + 1;
        }
        for (let j = 0; j < s1.length; j++) {
            seen2[s2[j]] = (seen2[s2[j]] || 0) + 1;
        }

        let l = 0;
        for (let r = s1.length; r < s2.length; r++) {
            if (isEqual(seen1, seen2)) {
                return true;
            }
            seen2[s2[l]]--;
            if (seen2[s2[l]] === 0) {
                delete seen2[s2[l]];
            }
            l++;
            seen2[s2[r]] = (seen2[s2[r]] || 0) + 1;
        }
        return isEqual(seen1, seen2);
    }
}

function isEqual(a, b) {
    if (Object.keys(a).length !== Object.keys(b).length) return false;

    for (let key in a) {
        if (a[key] !== b[key]) return false;
    }
    return true;
}
