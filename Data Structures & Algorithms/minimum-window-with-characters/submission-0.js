class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
    if (t.length > s.length) return "";

    const need = {};
    for (let char of t) {
        need[char] = (need[char] || 0) + 1;
    }

    let have = {};
    let needCount = Object.keys(need).length;
    let haveCount = 0;

    let res = [-1, -1];
    let resLen = Infinity;
    let l = 0;

    for (let r = 0; r < s.length; r++) {
        const char = s[r];
        have[char] = (have[char] || 0) + 1;

        if (char in need && have[char] === need[char]) {
            haveCount++;
        }

        // Contract from the left while the window is valid
        while (haveCount === needCount) {
            // Update result if smaller
            if ((r - l + 1) < resLen) {
                res = [l, r];
                resLen = r - l + 1;
            }

            // Shrink from left
            have[s[l]]--;
            if (s[l] in need && have[s[l]] < need[s[l]]) {
                haveCount--;
            }
            l++;
        }
    }

    const [start, end] = res;
    return resLen === Infinity ? "" : s.slice(start, end + 1);
}
}
