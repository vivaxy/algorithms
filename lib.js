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
        console.log('isSameArray error:', array1, array2);
    }
    return result;
};

exports.expect = function(result, to) {
    var res = result === to;
    if (!res) {
        console.log('expect error:', result, to);
    } else {
        console.log(res);
    }
};
