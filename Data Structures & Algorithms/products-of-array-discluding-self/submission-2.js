class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        	let mult_value = 1;
	let zero_count = 0;

	for (let i of nums) {
		if (i === 0) {
			zero_count++;
		} else {
			mult_value *= i;
		}
	}

	if (zero_count >= 2) {
		return new Array(nums.length).fill(0); // If there are 2+ zeros, all products are zero
	}

	let res = [];
	for (let i of nums) {
		if (zero_count === 1) {
			res.push(i === 0 ? mult_value : 0); // Only the zero position gets the product
		} else {
			res.push(mult_value / i);
		}
	}

	return res;

    }
}
