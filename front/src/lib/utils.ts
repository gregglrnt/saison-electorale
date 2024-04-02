export const mostFrequent = (arr: string[]) => {
    const store:  {[key: string] : number} = {}
    arr.forEach((i) => {
     store[i] = store[i] ? store[i] + 1 : 1;
    })
    let res : string = arr[0];
    let max = 0
    for(const item in store) {
      if(store[item] > max) {
        res = item;
        max = store[item]
      }
    }
    return res;
  }

  export const getDepartmentName = (txt: string) => {
    return txt.replace(/^'|'$/g, '');
  }