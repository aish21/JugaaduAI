import React, { useState } from "react";
import { firebasestorage } from "../../firebase/initFirebase";
import { uploadBytesResumable, ref as sRef, getDownloadURL } from "firebase/storage";

export default function Input({ onSend }) {
  const [text, setText] = useState("");
  const [file, setFile] = useState();
  const [percent, setPercent] = useState(0);

  const handleInputChange = e => {
    setText(e.target.value);
  };

  const handleFileChange = e => {
    setFile(e.target.files[0]);
    e.preventDefault();
  }

  const handleSend = e => {
    handleUpload();
    e.preventDefault();
    onSend(text);
    setText("");
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
          onChange={handleInputChange}
          value={text}
          placeholder="Enter your message here"
        />
        <input type="file" onChange={handleFileChange}/>
        <button>
          <svg
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="20"
            viewBox="0 0 500 500"
          >
            <g>
              <g>
                <polygon points="0,497.25 535.5,267.75 0,38.25 0,216.75 382.5,267.75 0,318.75" />
              </g>
            </g>
          </svg>
        </button>
      </form>
    </div>
  );
}
