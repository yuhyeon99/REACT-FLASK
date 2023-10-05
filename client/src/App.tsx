import axios from "axios";
import React, { useEffect, useState } from "react";

interface Item {
  id: number;
  name: string;
}

function App() {
  const [items, setItems] = useState<Item[]>([]);
  const [itemName, setItemName] = useState<string>("");

  useEffect(() => {
    axios
      .get<Item[]>("/read")
      .then((response) => {
        setItems(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const createItem = () => {
    if (itemName) {
      axios
        .post("/create", { name: itemName })
        .then(() => {
          setItemName("");
          axios
            .get<Item[]>("/read")
            .then((response) => {
              setItems(response.data);
            })
            .catch((error) => {
              console.error(error);
            });
        })
        .catch((error) => {
          console.error(error);
        });
    }
  };

  const deleteItem = (itemId: number) => {
    axios
      .delete(`/delete/${itemId}`)
      .then(() => {
        axios
          .get<Item[]>("/read")
          .then((response) => {
            setItems(response.data);
          })
          .catch((error) => {
            console.error(error);
          });
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div className="App">
      <h1>Item List</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            {item.name}
            <button onClick={() => deleteItem(item.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <div>
        <input
          type="text"
          placeholder="Item Name"
          value={itemName}
          onChange={(e) => setItemName(e.target.value)}
        />
        <button onClick={createItem}>Create</button>
      </div>
    </div>
  );
}

export default App;
