import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
function Sidebar() {
  const navigate = useNavigate();

const logout = () => {

    localStorage.removeItem(
        "access_token"
    );

    navigate("/login");
};
  return (
    <div
      style={{
        width: "250px",
        height: "100vh",
        background: "#1e293b",
        color: "white",
        padding: "20px",
        flexShrink: 0,
      }}
    >
      <h2>Support SaaS</h2>

      <hr />

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "20px",
          marginTop: "30px",
        }}
      >
        <Link
          style={{
            color: "white",
            textDecoration: "none",
          }}
          to="/dashboard"
        >
          Dashboard
        </Link>

        <Link
          style={{
            color: "white",
            textDecoration: "none",
          }}
          to="/chat"
        >
          AI Chat
        </Link>

        <Link
          style={{
            color: "white",
            textDecoration: "none",
          }}
          to="/complaints"
        >
          Complaints
        </Link>

        <Link
          style={{
            color: "white",
            textDecoration: "none",
          }}
          to="/tickets"
        >
          Tickets
        </Link>
            <Link
    style={{
        color: "white",
        textDecoration: "none"
          }}
          to="/emails"
      >
          Escalation Emails
      </Link>
            <button
        onClick={logout}
        style={{
            marginTop: "40px",
            padding: "10px",
            background: "#ef4444",
            color: "white",
            border: "none",
            cursor: "pointer",
            borderRadius: "5px"
        }}
    >
        Logout
    </button>
      </div>
    </div>
  );
}

export default Sidebar;