/************************************************************
"THE WEAKEST LINK" SCOREBOARD APPLICATION
by Jon Ingoglia
************************************************************/

var numPlayers = 8;
var numSteps = 8;
var activePlayer = 0;
var eliminatedPlayers = new Array();
var currentStep = 1;
var banked = 0.00;
var unbanked = 0.00;
var total = 0.00;
var isFinalRound = false;
var stopFlag;
var index;

var step8val = 12.50;
var step7val = 7.50;
var step6val = 5.00;
var step5val = 2.50;
var step4val = 1.00;
var step3val = 0.50;
var step2val = 0.25;
var step1val = 0.10;
var cap = step8val;

// Define keyboard shortcuts
Mousetrap.bind(['b', 'enter'], function () { if (activePlayer) bank(activePlayer); });
Mousetrap.bind(['c', 'up'], function () { if (activePlayer) playerCorrect(activePlayer); });
Mousetrap.bind(['i', 'down'], function () { if (activePlayer) playerIncorrect(activePlayer); });

// Enable or disable a single link
// button = id of the button, minus "Link"
// player = player this should affect
// action = enable, disable, or hide
function setButton(button, player, action) {
  if (action == "enable") {
    if (button == "Stop") {
      document.getElementById("p" + player + button + "Link").innerHTML = "<a href=\"javascript:player" + button + "(" + player + ", 'manual');\">" + button.toUpperCase() + "</a>";
    }
    else {
      document.getElementById("p" + player + button + "Link").innerHTML = "<a href=\"javascript:player" + button + "(" + player + ");\">" + button.toUpperCase() + "</a>";
    }
  }
  else if (action == "disable") {
    document.getElementById("p" + player + button + "Link").innerHTML = button.toUpperCase();
  }
  else if (action == "hide") {
    document.getElementById("p" + player + button + "Link").innerHTML = "&nbsp;";
  }
  else {
    document.getElementById("p" + player + button + "Link").innerHTML = "&nbsp;";
  }
}

// Check if player is eliminated
function isPlayerEliminated(player) {
  if (eliminatedPlayers.indexOf(player) == -1) return false;
  else return true;
}

// Set active player to next in line
function nextPlayer() {
  if (!isPlayerEliminated(activePlayer)) {
    setButton("Correct", activePlayer, "disable");
    setButton("Incorrect", activePlayer, "disable");
    document.getElementById("player" + activePlayer).style.backgroundColor = "#FFFFFF";
  }

  activePlayer++;
  if (activePlayer > numPlayers) activePlayer = 1;

  if (!isPlayerEliminated(activePlayer)) {
    setButton("Correct", activePlayer, "enable");
    setButton("Incorrect", activePlayer, "enable");
    document.getElementById("player" + activePlayer).style.backgroundColor = "yellow";
  }
  else {
    nextPlayer();
  }
}

// When BANK button is pressed
function bank(player) {
  if (activePlayer > 0) {
    if ((banked + unbanked) > cap) {
      unbanked = cap - banked;
    }

    num = parseFloat(document.getElementById("banked" + player).value);
    num += unbanked;
    document.getElementById("banked" + player).value = num.toFixed(2);

    banked += unbanked;
    unbanked = 0.00;

    document.getElementById("banked").innerHTML = "$" + banked.toFixed(2);
    if (banked == cap) { playerStop(player, "auto"); }
    resetToStep(1);
  }
}

// Return the cash value of a step
function getStepVal(step) {
  switch (step) {
    case 8: return step8val; break;
    case 7: return step7val; break;
    case 6: return step6val; break;
    case 5: return step5val; break;
    case 4: return step4val; break;
    case 3: return step3val; break;
    case 2: return step2val; break;
    case 1: return step1val; break;
    default: return 0; break;
  }
}

// When GO button is pressed
function playerGo(player) {
  for (index = 1; index <= numPlayers; index++) {
    if (!isPlayerEliminated(index)) {
      document.getElementById("player" + index).style.backgroundColor = "#FFFFFF";

      setButton("Go", index, "disable");
      setButton("Stop", index, "enable");
      setButton("Final", index, "disable");
      setButton("Correct", index, "disable");
      setButton("Incorrect", index, "disable");
      setButton("Eliminate", index, "disable");
    }
  }

  currentStep = 1;
  resetToStep(currentStep);
  resetStats();
  activePlayer = player;

  document.getElementById("player" + player).style.backgroundColor = "yellow";
  setButton("Correct", player, "enable");
  setButton("Incorrect", player, "enable");
}

// When FINAL button is pressed
function playerFinal(player) {
  if (confirm("Begin final round?")) {
    step8val *= 2;
    step7val *= 2;
    step6val *= 2;
    step5val *= 2;
    step4val *= 2;
    step3val *= 2;
    step2val *= 2;
    step1val *= 2;
    cap = step8val;
    init();
    playerGo(player);
    isFinalRound = true;
  }
}

// When STOP button is pressed
function playerStop(player, mode) {
  if (mode == "manual") { stopFlag = confirm("End the round?"); }
  else if (mode == "auto") { stopFlag = 2; alert("Ending the round..."); }
  else { stopFlag = 0; }

  if (stopFlag) {
    for (index = 1; index <= numPlayers; index++) {
      if (!isPlayerEliminated(index)) {
        if (!isFinalRound) {
          document.getElementById("player" + index).style.backgroundColor = "#FFFFFF";

          setButton("Go", index, "enable");
          setButton("Stop", index, "disable");
          setButton("Final", index, "enable");
          setButton("Correct", index, "disable");
          setButton("Incorrect", index, "disable");
          setButton("Eliminate", index, "enable");
        }
        else {
          document.getElementById("player" + index).style.backgroundColor = "#D9D4D8";

          setButton("Go", index, "disable");
          setButton("Stop", index, "disable");
          setButton("Final", index, "disable");
          setButton("Correct", index, "disable");
          setButton("Incorrect", index, "disable");
          setButton("Eliminate", index, "disable");
        }
      }
    }

    currentStep = 1;
    resetToStep(currentStep);
    activePlayer = 0;

    total += banked;
    banked = 0.00;
    unbanked = 0.00;

    document.getElementById("banked").innerHTML = "$" + banked.toFixed(2);
    document.getElementById("total").innerHTML = "$" + total.toFixed(2);
  }
}

// When ELIMINATE button is pressed
function playerEliminate(player) {
  if (confirm("Are you sure you want to eliminate player " + player + "?")) {
    document.getElementById("player" + player).style.backgroundColor = "red";
    setButton("Go", player, "hide");
    setButton("Stop", player, "hide");
    setButton("Final", player, "hide");
    setButton("Correct", player, "hide");
    setButton("Incorrect", player, "hide");
    document.getElementById("p" + player + "Bar").innerHTML = "&nbsp;";
    document.getElementById("p" + player + "EliminateLink").innerHTML = "<strong>ELIMINATED</strong>";

    document.getElementById("numCorrect" + player).style.backgroundColor = "red";
    document.getElementById("numIncorrect" + player).style.backgroundColor = "red";
    document.getElementById("numAnswered" + player).style.backgroundColor = "red";
    document.getElementById("percentCorrect" + player).style.backgroundColor = "red";
    document.getElementById("percentIncorrect" + player).style.backgroundColor = "red";
    document.getElementById("banked" + player).style.backgroundColor = "red";
    document.getElementById("numCorrect" + player).disabled = true;
    document.getElementById("numIncorrect" + player).disabled = true;

    eliminatedPlayers.push(player);
    console.log("Eliminated Players: " + eliminatedPlayers.toString()); //debug

    banked = 0.00;
    unbanked = 0.00;

    resetToStep(1);
    activePlayer = 0;
  }
}

// Increment a stat by 1
function increment(stat, player) {
  num = parseFloat(document.getElementById(stat + player).value);
  num++;
  document.getElementById(stat + player).value = num;

  calculate(player);
}

function calculate(player) {
  if (player > 0) {
    if (!isPlayerEliminated(player)) {
      numCorrect = parseFloat(document.getElementById("numCorrect" + player).value)
      numIncorrect = parseFloat(document.getElementById("numIncorrect" + player).value)
      numAnswered = parseFloat(document.getElementById("numAnswered" + player).value)

      numAnswered = numCorrect + numIncorrect;
      document.getElementById("numAnswered" + player).value = numAnswered;

      if (numAnswered != 0) {
        num = (numCorrect / numAnswered);
        document.getElementById("percentCorrect" + player).value = (num * 100).toFixed(2);

        num = (numIncorrect / numAnswered);
        document.getElementById("percentIncorrect" + player).value = (num * 100).toFixed(2);
      }
    }
  }
  else {
    for (index = 1; index <= numPlayers; index++) {
      if (!isPlayerEliminated(index)) {
        numCorrect = parseFloat(document.getElementById("numCorrect" + index).value)
        numIncorrect = parseFloat(document.getElementById("numIncorrect" + index).value)
        numAnswered = parseFloat(document.getElementById("numAnswered" + index).value)

        numAnswered = parseFloat(numCorrect) + parseFloat(numIncorrect);
        document.getElementById("numAnswered" + index).value = parseFloat(numAnswered);

        if (numAnswered != 0) {
          num = (numCorrect / numAnswered);
          document.getElementById("percentCorrect" + index).value = (num * 100).toFixed(2);

          num = (numIncorrect / numAnswered);
          document.getElementById("percentIncorrect" + index).value = (num * 100).toFixed(2);
        }
      }
    }
  }
}

function resetStats() {
  for (index = 1; index <= numPlayers; index++) {
    document.getElementById("numCorrect" + index).value = 0;
    document.getElementById("numIncorrect" + index).value = 0;
    document.getElementById("numAnswered" + index).value = 0;
    document.getElementById("percentCorrect" + index).value = "0.00";
    document.getElementById("percentIncorrect" + index).value = "0.00";
    document.getElementById("banked" + index).value = "0.00";
  }
}

// When CORRECT button is pressed
function playerCorrect(player) {
  currentStep++;
  if (currentStep - 1 > numSteps) currentStep = numSteps + 1;
  console.log("currentStep = " + currentStep); //debug

  resetToStep(currentStep);
  unbanked = getStepVal(currentStep - 1);

  increment("numCorrect", player);

  nextPlayer();
}

// When INCORRECT button is pressed
function playerIncorrect(player) {
  resetToStep(1);
  unbanked = 0.00;

  increment("numIncorrect", player);

  nextPlayer();
}

// Reset the board to a step, any steps that put a bank over the cap will turn red
function resetToStep(step) {
  currentStep = step;

  for (index = numSteps; index > 0; index--) {
    if (step < index) {
      document.getElementById("step" + index).style.backgroundColor = "#FFFFFF";
    }
    else if (step == index) {
      document.getElementById("step" + index).style.backgroundColor = "#43D1B9";
    }
    else {
      document.getElementById("step" + index).style.backgroundColor = "yellow";
    }
  }
}

function toggleStatsSection() {
  if (document.getElementById("statsSection").style.display == "none") {
    document.getElementById("statsSection").style.display = "block";
  }
  else {
    document.getElementById("statsSection").style.display = "none";
  }
}

// ON WINDOW LOAD - Initialize the board & step values
function init() {
  document.getElementById("step8").innerHTML = "$" + step8val.toFixed(2);
  document.getElementById("step7").innerHTML = "$" + step7val.toFixed(2);
  document.getElementById("step6").innerHTML = "$" + step6val.toFixed(2);
  document.getElementById("step5").innerHTML = "$" + step5val.toFixed(2);
  document.getElementById("step4").innerHTML = "$" + step4val.toFixed(2);
  document.getElementById("step3").innerHTML = "$" + step3val.toFixed(2);
  document.getElementById("step2").innerHTML = "$" + step2val.toFixed(2);
  document.getElementById("step1").innerHTML = "$" + step1val.toFixed(2);
  document.getElementById("banked").innerHTML = "$" + banked.toFixed(2);
  document.getElementById("total").innerHTML = "$" + total.toFixed(2);
}

window.onload = init;