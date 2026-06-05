import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";

import {
  getAnalytics
} from "../services/analyticsService";

function DashboardPage() {

  const [metrics, setMetrics] =
    useState(null);

  useEffect(() => {

    loadAnalytics();

  }, []);

  const loadAnalytics = async () => {

    try {

      const data =
        await getAnalytics();

      setMetrics(data);

    } catch (error) {

      console.error(error);

    }
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

        <h1>
          Dashboard
        </h1>

        {!metrics ? (

          <p>
            Loading...
          </p>

        ) : (

          <div
            style={{
              display: "grid",
              gridTemplateColumns:
                "repeat(3, 1fr)",
              gap: "20px",
              marginTop: "30px"
            }}
          >

            <Card
              title="Complaints"
              value={
                metrics.total_complaints
              }
            />

            <Card
              title="Tickets"
              value={
                metrics.total_tickets
              }
            />

            <Card
              title="Escalations"
              value={
                metrics.total_escalations
              }
            />

            <Card
              title="Invoice"
              value={
                metrics.invoice_complaints
              }
            />

            <Card
              title="HR"
              value={
                metrics.hr_complaints
              }
            />

            <Card
              title="Reviews"
              value={
                metrics.review_complaints
              }
            />

          </div>

        )}

      </div>

    </div>
  );
}

function Card({
  title,
  value
}) {

  return (

    <div
      style={{
        background: "#ffffff",
        padding: "25px",
        borderRadius: "10px",
        boxShadow:
          "0 2px 8px rgba(0,0,0,0.1)"
      }}
    >

      <h3>
        {title}
      </h3>

      <h1>
        {value}
      </h1>

    </div>

  );
}

export default DashboardPage;