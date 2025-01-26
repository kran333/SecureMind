import React, { useState, useEffect } from "react";
import Table from "../components/Table";

function MonitorAll() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const response = await fetch(
          "https://api.restful-api.dev/objects"
        );
        const result = await response.json();
		console.log("Data fetched:", result);
         // Check if the result is an array
        setData(Array.isArray(result) ? result : []);
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>Monitor All</h2>
      {loading ? <p>Loading...</p> : <Table data={data} />}
    </div>
  );
}

export default MonitorAll;
