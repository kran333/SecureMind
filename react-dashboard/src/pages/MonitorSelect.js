import React, { useState } from "react";
import Table from "../components/Table";

function MonitorSelect() {
  const [tableName, setTableName] = useState("");
  const [databaseName, setDatabaseName] = useState("");
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchData = async () => {
    if (!tableName || !databaseName) {
      alert("Please enter both table name and database name.");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(
        `https://<api-id>.execute-api.<region>.amazonaws.com/prod/monitor/select/?table_name=${tableName}&database_name=${databaseName}`
      );
      const result = await response.json();
      setData(result.body || []);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Monitor Select</h2>
      <div>
        <label>
          Table Name:{" "}
          <input
            type="text"
            value={tableName}
            onChange={(e) => setTableName(e.target.value)}
          />
        </label>
      </div>
      <div>
        <label>
          Database Name:{" "}
          <input
            type="text"
            value={databaseName}
            onChange={(e) => setDatabaseName(e.target.value)}
          />
        </label>
      </div>
      <button onClick={fetchData} disabled={loading}>
        {loading ? "Loading..." : "Fetch Data"}
      </button>
      {data.length > 0 && <Table data={data} />}
    </div>
  );
}

export default MonitorSelect;
