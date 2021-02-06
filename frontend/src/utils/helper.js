function converToMins(value) {
  let time = parseFloat(value);
  let timeInMins = time * 60;
  return timeInMins;
}

export { converToMins };
