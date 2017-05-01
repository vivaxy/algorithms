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
    return JSON.stringify(array1) === JSON.stringify(array2);
};

exports.expect = function(result, to) {
    console.log(result === to);
};
