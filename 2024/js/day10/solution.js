/**
 * @param {string[]} instructions - The instructions to execute
 * @returns {number} The value of the register A
 */
function compile(instructions) {
  var position = 0;
  var vars = {};

  while (position < instructions.length) {
    const instruction = instructions[position];
    const params = instruction.split(" ");
    const action = params[0];
    const x = params[1];
    let y = null;
    if (params.length > 2) {
      y = params[2];
    }

    if (action === "MOV") {
      if (x in vars) {
        vars[y] = vars[x];
      } else {
        vars[y] = Number(x);
      }
      position++;
    }

    if (action === "INC") {
      vars[x]++;
      position++;
    }

    if (action == "JMP") {
      value = vars[x] || 0;
      if (value === 0) {
        position = Number(y);
      } else {
        position++;
      }
    }
  }
  return vars["A"] || "undefined";
}
