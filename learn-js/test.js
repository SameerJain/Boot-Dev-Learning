function getMonthlyPrice(tier) {
  let dollarCost = 0;

  if (tier === "basic"){
    dollarCost = 100}
  else if (tier === "premium"){
    dollarCost = 150;}
  else if (tier === "enterprise"){
    dollarCost = 500;}
  else{
    return dollarCost;}
  
  let pennyValue = dollarCost * 100
  return pennyValue
}

console.log(getMonthlyPrice("enterprise"))
console.log(getMonthlyPrice("enterprise"));