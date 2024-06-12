// Iterative function to print all distinct subsets of `S`
function findPowerSet(S) {
    // `N` stores the total number of subsets
    const N = Math.pow(2, S.length);
    const s = new Set();
  
    // sort the set
    S.sort((a, b) => a - b);
  
    // generate each subset one by one
    for (let i = 0; i < N; i++) {
      const subset = [];
      // check every bit of `i`
      for (let j = 0; j < S.length; j++) {
        // if j'th bit of `i` is set, append `S[j]` to the subset
        if (i & (1 << j)) {
          subset.push(S[j]);
        }
      }
  
      // insert the subset into the set
      s.add(subset.slice());
    }
  
    // print all subsets present in the set
    console.log(Array.from(s));
  }
  
  const S = [1, 2, 1];
  findPowerSet(S);
  
  