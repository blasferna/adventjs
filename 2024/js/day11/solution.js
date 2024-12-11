/**
 * @param {string} filename - The filename to decode.
 * @returns {string} The decoded filename.
 */
function decodeFilename(filename) {
  const left_part = filename.split("_")[0];
  const right_part = filename.split(".").slice(-1)[0];
  return filename.replace(`${left_part}_`, "").replace(`.${right_part}`, "")
}
