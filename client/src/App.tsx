import axios from "axios";
import React, { useEffect, useState } from "react";

interface dataType {
  id: string;
  name: string;
}

function App() {
  const [data, setData] = useState<dataType[]>([{ id: "", name: "" }]);

  useEffect(() => {
    axios
      .get("/users")
      .then((res) => {
        setData(res.data.members);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  return (
    <div className="App">
      <h1>TEST 하는 중...</h1>
      <div>
        {data.map((member: dataType) => (
          <p key={member.id}>{member.name}</p>
        ))}
      </div>
    </div>
  );
}

export default App;
