/**
 * @since 2017-04-28 13:40:04
 * @author vivaxy
 * @see https://leetcode.com/problems/encode-and-decode-tinyurl

 TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

 Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

 */

/**
 * @see https://leetcode.com/submissions/detail/101412106/
 *
 * Encodes a URL to a shortened URL.
 *
 * @param {string} longUrl
 * @return {string}
 */
var encode = function(longUrl) {
    return longUrl;
};

/**
 * Decodes a shortened URL to its original URL.
 *
 * @param {string} shortUrl
 * @return {string}
 */
var decode = function(shortUrl) {
    return shortUrl;
};

/**
 * Your functions will be called as such:
 * decode(encode(url));
 */

var test = require('ava');
test('encode-and-decode-tinyurl', function(t) {
    var url = 'https://leetcode.com/problems/design-tinyurl';
    t.is(url, decode(encode(url)));
});
