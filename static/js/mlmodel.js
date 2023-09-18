function goToHome() {
  window.location.href = "/#college";
}

document.getElementById("yesBtn").addEventListener("click", function () {
  document.getElementById("result").innerHTML =
    "Great! The model was accurately able to identify the wild cat!";
  document.getElementById("result").style.color = "#20dd33";
});

document.getElementById("noBtn").addEventListener("click", function () {
  document.getElementById("result").innerHTML =
    "Oops! The model was not able to identify the wild cat! For better results, try uploading a different image with a clear view of the wild cat.";
  document.getElementById("result").style.color = "red";
});
