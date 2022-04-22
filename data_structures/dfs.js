class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const depthFirstValues = (root) => {
  const stack = [ root ]; 
  while (stack.length > 0) {
    const current = stack.pop();
    console.log(current.val);

    if(current.right) stack.push(current.right);
    if(current.left) stack.push(current.left);
  }
}

const a = new Node('a');
const b = new Node('b');
const c = new Node('c');

a.left = b;
a.right = c;

depthFirstValues(a);
