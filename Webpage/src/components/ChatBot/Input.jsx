import React, { useState } from "react";
import { firebasestorage } from "../../firebase/initFirebase";
import { uploadBytesResumable, ref as sRef, getDownloadURL } from "firebase/storage";
import SpeechRecognition, {useSpeechRecognition} from "react-speech-recognition";

export default function Input({ onSend }) {
  const [text, setText] = useState("");
  const [file, setFile] = useState();
  const [percent, setPercent] = useState(0);
  const { transcript, resetTranscript } = useSpeechRecognition(); 

  const handleChange = (e) => {
    e.preventDefault();
    setText(e.target.value);
  };

  const handleFileChange = e => {
    setFile(e.target.files[0]);
    e.preventDefault();
  }

  const handleSend = e => {
    handleUpload();
    e.preventDefault();
    
    onSend(transcript? transcript:text);
    setText("");
    resetTranscript();
  };

  const handleEnableSpeechClick = () => {
    const permission = navigator.mediaDevices.getUserMedia({
      audio: true,
      video: false
    });
    permission.then(() => {
      SpeechRecognition.startListening({ continuous: true });
      console.log("listening");
      //setText(transcript);
    });
  };

  const handleDisableSpeechClick = () => {
    SpeechRecognition.stopListening().then(() => {
      // const microphone = navigator.permissions.query({ name: "microphone" });
      // navigator.permissions.revoke(microphone);
      navigator.permissions.query({ name: 'microphone' })
  .then(permissionStatus => {
    if (permissionStatus.state === 'granted') {
      permissionStatus.revoke()
        .then(() => {
          console.log('Microphone permissions revoked.');
        })
        .catch((err) => {
          console.error('Failed to revoke microphone permissions:', err);
        });
    }
  })
  .catch((err) => {
    console.error('Failed to query microphone permissions:', err);
  });

      //setText(transcript);
    });
  };

  function handleUpload() {
    if (!file) {
      alert("Please choose a file first!");
    }
    const storageRef = sRef(firebasestorage, '/input/' + file.name);
    const uploadTask = uploadBytesResumable(storageRef, file);
    uploadTask.on(
      "state_changed",
      (snapshot) => {
        const percent = Math.round(
          (snapshot.bytesTransferred / snapshot.totalBytes) * 100
        );

        setPercent(percent);
      },
      (err) => console.log(err),
      () => {
      // download url
      getDownloadURL(uploadTask.snapshot.ref).then((url) => {
      console.log(url);
    });
  }
  ); 
  }


  return (
    <div className="input">
      <form onSubmit={handleSend} className="side-by-side">
        <input
          type="text"
          onChange={handleChange}
          value={transcript? transcript:text}
          placeholder="Enter your message here"
        />
        <input type="file" onChange={handleFileChange} className="fileChosen"/>
        <button>
          <svg
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            width="25"
            height="25"
            viewBox="0 0 500 500"
            fill="white"
          >
            <g>
              <g>
                <polygon points="0,497.25 535.5,267.75 0,38.25 0,216.75 382.5,267.75 0,318.75" />
              </g>
            </g>
          </svg>
        </button>
      </form>
      <div>
        <button className = "testButton" onClick={handleEnableSpeechClick}>Start Listening</button>
        <button className = "testButton" onClick={handleDisableSpeechClick}>Stop Listening</button>
        </div>
    </div>
  );
}