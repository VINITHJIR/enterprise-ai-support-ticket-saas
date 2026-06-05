import { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import { getComplaints } from "../services/complaintService";

function ComplaintsPage() {

  const [complaints, setComplaints] = useState([]);

  useEffect(() => {
    loadComplaints();
  }, []);

  const loadComplaints = async () => {

    const data = await getComplaints();

    setComplaints(data);
  };

  return (
    <div
      style={{
        display: "flex",
        minHeight: "100vh"
      }}
    >
      <Sidebar />

      <div
        style={{
          flex: 1,
          padding: "30px"
        }}
      >
        <h2>Complaints</h2>

        <table
          border="1"
          cellPadding="10"
          width="100%"
        >
          <thead>
            <tr>
              <th>ID</th>
              <th>Complaint</th>
              <th>Category</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {complaints.map((item) => (
              <tr key={item.id}>
                <td>{item.id}</td>
                <td>{item.complaint}</td>
                <td>{item.category}</td>
                <td>{item.status}</td>
              </tr>
            ))}
          </tbody>

        </table>
      </div>
    </div>
  );
}

export default ComplaintsPage;