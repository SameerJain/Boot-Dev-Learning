function reformat(message, formatter) {
  let mess = formatter(message);
  messformatter(message);
  formatter(message);
  return "TEXTIO" + message;
}

// don't touch below this line

export { reformat };

console.log(reformat("hello",(msg) => msg.toUpperCase()));