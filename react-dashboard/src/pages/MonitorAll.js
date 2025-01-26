import React, { useState, useEffect } from "react";
import Table from "../components/Table";

function MonitorAll() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const response = await fetch(
          "https://api.restful-api.dev/objects"
        );
        const result = await response.json();
        setData(result.body || []);
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
