/**
 * @since 2017-05-01 09:43:09
 * @author vivaxy
 */

/**
 *
 * @param {String[]|Number[]|Number[][]} array1
 * @param {String[]|Number[]|Number[][]} array2
 * @returns {boolean}
 */
exports.expectToBeSameArray = function(array1, array2) {
    var result = JSON.stringify(array1) === JSON.stringify(array2);
    if (!result) {
        throw new Error('`' + array1 + '` is not same as `' + array2 + '`');
    }
    return result;
};

/**
 *
 * @param {String[]|Number[]|Number[][]} array1
 * @param {String[]|Number[]|Number[][]} array2
 * @returns {Boolean}
 */
exports.expectToBeSameSet = function(array1, array2) {
    var throwError = function() {
        throw new Error('`' + array1 + '` is not the same set as `' + array2 + '`');
    };
    if (array1.length !== array2.length) {
        throwError();
    }
    var sortNumber = function(prev, next) {
        return prev - next;
    };
    var sortedArray1 = array1.sort(sortNumber);
    var sortedArray2 = array2.sort(sortNumber);
    var result = JSON.stringify(sortedArray1) === JSON.stringify(sortedArray2);
    if (!result) {
        throwError();
    }
    return result;
};

exports.expect = function(result, to) {
    var res = result === to;
    if (!res) {
        throw new Error('expect `' + result + '` to be `' + to + '`');
    }
    return res;
};
