/** @param {string} ornaments
 * @return {number} - The price of the tree
 */
function calculatePrice(ornaments) {
  const prices = { "*": 1, o: 5, "^": 10, "#": 50, "@": 100 };
  let ornaments_prices = [];
  for (let char of ornaments) {
    if (!Object.keys(prices).includes(char)) {
      return undefined;
    }
    ornaments_prices.push(prices[char]);
  }
  for (let i = 0; i < ornaments_prices.length; i++) {
    let current_price = ornaments_prices[i];
    let next_price = ornaments_prices[i + 1];
    if (current_price < next_price) {
      ornaments_prices[i] = current_price * -1;
    }
  }
  return ornaments_prices.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    0,
  );
}
