function drawTable(data) {
  if (!data || !data.length) return "";

  let columns = [];

  data.forEach((row, i) => {
    if (columns.length === 0) {
      columns = Object.keys(row).map((c) => [
        c.charAt(0).toUpperCase() + c.slice(1),
        c.length,
      ]);
    }

    let j = 0;
    for (const [key, value] of Object.entries(row)) {
      columns[j][1] = Math.max(String(value).length, columns[j][1]);
      j++;
    }
  });

  const divider =
    "+" + columns.map((col) => "-".repeat(col[1] + 2) + "+").join("");

  const table = [];
  table.push(divider);

  const header =
    "|" +
    columns.map(([col, width]) => ` ${String(col).padEnd(width)} |`).join("");
  table.push(header);
  table.push(divider);

  data.forEach((line) => {
    const row =
      "|" +
      Object.values(line)
        .map((v, i) => ` ${String(v).padEnd(columns[i][1])} |`)
        .join("");
    table.push(row);
  });

  table.push(divider);
  return table.join("\n");
}
