import React, { useState, useEffect } from "react";
import "./App.css";

const hiraganaToRomaji = {
  "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
  "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
  "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
  "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
  "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
  "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
  "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
  "や": "ya", "ゆ": "yu", "よ": "yo",
  "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
  "わ": "wa", "を": "wo", "ん": "n"
};

const allHiragana = Object.keys(hiraganaToRomaji);
const fullHiraganaList = [...allHiragana, ...allHiragana];

const getRandomQuestions = () => {
  let shuffled = fullHiraganaList.sort(() => 0.5 - Math.random());
  return shuffled.slice(0, 20);
};

const roll3d6 = () => {
  return (
    Math.floor(Math.random() * 6 + 1) +
    Math.floor(Math.random() * 6 + 1) +
    Math.floor(Math.random() * 6 + 1)
  );
};

function App() {
  const [enemyHP, setEnemyHP] = useState(
    parseInt(localStorage.getItem("enemyHP")) || 100
  );
  const [loot, setLoot] = useState(parseInt(localStorage.getItem("loot")) || 0);
  const [hit, setHit] = useState(parseInt(localStorage.getItem("hit")) || 0);
  const [miss, setMiss] = useState(parseInt(localStorage.getItem("miss")) || 0);
  const [streak, setStreak] = useState(parseInt(localStorage.getItem("streak")) || 0);
  const [roundsLeft, setRoundsLeft] = useState(parseInt(localStorage.getItem("roundsLeft")) || 0);

  const [questions, setQuestions] = useState(getRandomQuestions());
  const [currentIndex, setCurrentIndex] = useState(0);
  const [waiting, setWaiting] = useState(false);
  const [hitMessage, setHitMessage] = useState("");

  const currentHiragana = questions[currentIndex];
  const correctAnswer = hiraganaToRomaji[currentHiragana];
  const answerOptions = [
    correctAnswer,
    ...allHiragana.sort(() => 0.5 - Math.random()).slice(0, 3)
  ];

  const handleAnswerClick = (selectedAnswer) => {
    if (waiting) return;
    
    if (selectedAnswer === correctAnswer) {
      console.log("Enemy hit!");
      const damage = roll3d6();
      console.log("Damage dealt:", damage);
      const newHP = Math.max(enemyHP - damage, 0);
      setEnemyHP(newHP);
      localStorage.setItem("enemyHP", newHP);
      setHitMessage(`Hit (${damage})`);

      if (newHP === 0) {
        console.log("Enemy defeated!");
        if ((enemyHP - damage)< -10) {
          console.log(`big overkill detected by ${(enemyHP - damage)}`);
        } else if ((enemyHP - damage)< -5) {
          console.log(`small overkill detected by ${(enemyHP - damage)}`);
        };
        // gibbon, need to set hit, miss, streak, rounds-left
        setLoot(loot + 1);
        localStorage.setItem("loot", loot + 1);
        setEnemyHP(100);
        localStorage.setItem("enemyHP", 100);
      }
    } else {
      setHitMessage("Miss!");
    }
    
    setWaiting(true);
  };

  const handleContinue = () => {
    if (!waiting) return;
    
    if (currentIndex < 19) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setQuestions(getRandomQuestions());
      setCurrentIndex(0);
    }
    setHitMessage("");
    setWaiting(false);
  };

  return (
    <div className="game-container">
      <div className="enemy-panel">
        <div className="enemy-name">Enemy</div>
        <img src="monster.png" alt="Enemy" />
        <div className="health-bar-container">
          <div
            className="health-bar"
            style={{ width: `${enemyHP}%` }}
          ></div>
        </div>
        <div className="stats">
          <span>Loot: {loot}</span>
          <span>Hit: {loot}</span>
          <span>Miss: {loot}</span>
          <span>Streak: {loot}</span>
          <span>rounds left: {loot}</span>
        </div>
        {hitMessage && <div className="hit-message" style={{ color: hitMessage.includes("Hit") ? "red" : "gray", position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)", background: "rgba(0, 0, 0, 0.5)", padding: "10px", borderRadius: "5px" }}>{hitMessage}</div>}
      </div>
      <div 
        className={`quiz-panel ${waiting ? "waiting-phase" : ""}`} 
        onClick={waiting ? handleContinue : undefined}
      >
        <div className="question-header">{currentHiragana}</div>
        <ul>
          {answerOptions.map((answer, index) => (
            <li
              key={index}
              className={`answer-option ${waiting && answer === correctAnswer ? "correct" : ""}`}
              onClick={() => handleAnswerClick(answer)}
            >
              {answer}
            </li>
          ))}
        </ul>
        {waiting && <div className="click-to-continue">Click panel to continue</div>}
      </div>
    </div>
  );
}

export default App;
