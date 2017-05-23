/**
 * @since 2017-05-01 09:43:09
 * @author vivaxy
 */

/**
 *
 * @param array1
 * @param array2
 * @returns {boolean}
 */
exports.isSameArray = function(array1, array2) {
    var result = JSON.stringify(array1) === JSON.stringify(array2);
    if (!result) {
        throw new Error(array1 + ' is not same as ', array2);
    }
    return result;
};

exports.expect = function(result, to) {
    var res = result === to;
    if (!res) {
        throw new Error('expect ' + result + ' to be ' + to);
    }
    return res;
};
