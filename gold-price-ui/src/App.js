import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [goldData, setGoldData] = useState(null); // لتخزين بيانات الذهب
  const [loading, setLoading] = useState(true); // لتحديد حالة التحميل

  useEffect(() => {
 
    const fetchGoldPrice = () => {
      fetch("http://127.0.0.1:5000/gold")
        .then((res) => res.json())
        .then((data) => {
          setGoldData(data);  
          setLoading(false);  
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    };

  
    const interval = setInterval(fetchGoldPrice, 10000);


    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <h1>Gold Prices</h1>
      {loading ? (
        <p>Loading gold prices...</p>
      ) : (
        <div>
          <p>Metal: {goldData.metal}</p>
          <p>Gram 24K: {goldData.price_gram_24k} {goldData.currency}</p>
          <p>Gram 21K: {goldData.price_gram_21k} {goldData.currency}</p>
          <p>Gram 18K: {goldData.price_gram_18k} {goldData.currency}</p>
          <p>Timestamp: {goldData.timestamp}</p>
        </div>
      )}
    </div>
  );
}

export default App;
