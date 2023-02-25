import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";

import BotMessage from "components/ChatBot/BotMessage";
import UserMessage from "components/ChatBot/UserMessage";
import Messages from "components/ChatBot/Messages";
import Input from "components/ChatBot/Input";
//import SpeechRecognition from "components/ChatBot/Dictaphone";

import API from "APICalls/ChatbotAPI";

import "components/ChatBot/botStyles.css";
import BotHeader from "components/ChatBot/BotHeader";

export default function Chatbot() {

  const [messages, setMessages] = useState([]);

  useEffect(() => {
    async function loadWelcomeMessage() {
      setMessages([
        <BotMessage
          key="0"
          fetchMessage={async () => await API.GetChatbotResponse("hi")}
        />
      ]);
    }
    loadWelcomeMessage();
  }, []);

  const send = async text => {
    const newMessages = messages.concat(
      <UserMessage key={messages.length + 1} text={text} />,
      <BotMessage
        key={messages.length + 2}
        fetchMessage={async () => await API.GetChatbotResponse(text)}
      />
    );
    setMessages(newMessages);
  };

  return (
    <div className="chatbot">
      <BotHeader />
      <Messages messages={messages} />
      <Input onSend={send} />
    </div>
  );
}