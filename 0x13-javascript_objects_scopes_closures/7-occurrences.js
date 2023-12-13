#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce(function (count, element) {
    if (element === searchElement) {
      return count + 1;
    } else {
      return count;
    }
  }, 0);
};
