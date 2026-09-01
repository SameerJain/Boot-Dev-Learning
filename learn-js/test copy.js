function getMessageStatus(message) {
  let messageStatus = "processing";

  function isValidLength(message) {
    let messageStatus = "invalid";

    if (message.length > 0) {
      messageStatus = "valid";
    }

    return messageStatus;
  }

  // don't touch above this line

  isValidLength(message);
  return messageStatus;
}

// don't touch below this line
console.log(getMessageStatus("Tread lightly"))
export { getMessageStatus };
