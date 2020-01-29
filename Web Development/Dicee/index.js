var randomNumber1 = (Math.floor(Math.random() * 6) + 1);
var randomNumber2 = (Math.floor(Math.random() * 6) + 1);

var imgTemp1 = "images/dice" + randomNumber1 + ".png";
var imgTemp2 = "images/dice" + randomNumber2 + ".png";

document.querySelectorAll("img")[0].setAttribute("src", imgTemp1);
document.querySelectorAll("img")[1].setAttribute("src", imgTemp2);

var selectHead = document.querySelector("h1");

if (randomNumber1 > randomNumber2){
  selectHead.innerHTML = "Player 1 Wins!";
} else if (randomNumber1 < randomNumber2) {
  selectHead.innerHTML = "Player 2 Wins!";
} else {
  selectHead.innerHTML = "Draw!";
}
