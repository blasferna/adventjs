/**
 * @param {string[]} instructions - The instructions to execute
 * @returns {number} The value of the register A
 */
function compile(instructions) {
  var pointer = 0;
  var registry = {};

  while (pointer < instructions.length) {
    const instruction = instructions[pointer];
    const [action, x, y] = instruction.split(" ");

    if (action === "MOV") {
      if (x in registry) {
        registry[y] = registry[x];
      } else {
        registry[y] = Number(x);
      }
      pointer++;
    }

    if (action === "INC") {
      registry[x] = registry[x] || 0;
      registry[x]++;
      pointer++;
    }

    if (action === "DEC") {
      registry[x] = registry[x] || 0;
      registry[x]--;
      pointer++;
    }

    if (action == "JMP") {
      let value = registry[x] || 0;
      if (value === 0) {
        pointer = Number(y);
      } else {
        pointer++;
      }
    }
  }
  return registry["A"];
}
