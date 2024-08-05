//https://leetcode.com/problems/partition-labels/description/

/**
 * @param {string} s
 * @return {number[]}
 */
 var partitionLabels = function(s) {
  const last = {

  };


  for (let i = 0; i < s.length; i++) {
    last[s[i]] = i;
  }
  

  const partitions = [];
  let partition = [];
  let end = 0;

  for (let i = 0; i < s.length; i++) {
    partition.push(s[i]);
    end = Math.max(end, last[s[i]]);

    if (i === end) {
      partitions.push(partition);
      partition = [];
    }
  }
 
  

  return partitions.map(group => group.length)

};


console.log(partitionLabels("ababcbacadefegdehijhklij"))
