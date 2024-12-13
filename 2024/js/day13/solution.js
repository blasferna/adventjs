function isRobotBack(moves) {
  const modifiers = ["*", "!", "?"];
  const commands = {
    R: [0, 1, "L"],
    L: [0, -1, "R"],
    U: [1, 1, "D"],
    D: [1, -1, "U"],
  };

  const done = [];
  let modifier = null;
  const position = [0, 0];

  for (let i = 0; i < moves.length; i++) {
    const mov = moves[i];

    if (modifiers.includes(mov)) {
      modifier = mov;
      continue;
    }

    let command = mov;

    if (modifier) {
      if (modifier === "*") {
        command = command.repeat(2);
      }
      if (modifier === "!") {
        command = commands[mov][2];
      }
      if (modifier === "?") {
        if (done.includes(command)) {
          command = null;
        }
      }
      modifier = null;
    }

    if (command) {
      for (const movement of command) {
        const [index, increment] = commands[movement];
        position[index] = position[index] + increment;
      }
      done.push(command[0]);
    }
  }

  return position[0] === 0 && position[1] === 0 ? true : position;
}

