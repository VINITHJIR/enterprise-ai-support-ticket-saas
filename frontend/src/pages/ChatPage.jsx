import {
  useState,
  useEffect,
  useRef,
} from "react";

import Sidebar from "../components/Sidebar";
import api from "../services/api";

function ChatPage() {

  const [message, setMessage] =
    useState("");

  const [messages, setMessages] =
    useState([]);

  const [loading, setLoading] =
    useState(false);

  const messagesEndRef =
    useRef(null);

  useEffect(() => {

    loadHistory();

  }, []);

  useEffect(() => {

    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });

  }, [messages, loading]);

  const loadHistory = async () => {

    try {

      const result =
        await api.get(
          "/api/memory/"
        );

      const history =
        result.data.map(
          (item) => ({
            sender:
              item.role === "user"
                ? "user"
                : "bot",

            text:
              item.content,
          })
        );

      setMessages(
        history
      );

    } catch (error) {

      console.error(
        "History load failed",
        error
      );

    }
  };

  const sendMessage = async () => {

    if (!message.trim()) return;

    const userText = message;

    const userMessage = {
      sender: "user",
      text: userText,
    };

    setMessages((prev) => [
      ...prev,
      userMessage,
    ]);

    setMessage("");

    setLoading(true);

    try {

      const result =
        await api.post(
          "/api/chat/",
          {
            message:
              userText,
          }
        );

      const botMessage = {
        sender: "bot",

        text:
          result.data.response ||
          "No response",

        complaint_id:
          result.data.complaint_id,

        ticket_id:
          result.data.ticket_id,

        category:
          result.data.category,

        priority:
          result.data.priority,
      };

      setMessages((prev) => [
        ...prev,
        botMessage,
      ]);

    } catch (error) {

      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text:
            "Something went wrong.",
        },
      ]);

    } finally {

      setLoading(false);

    }
  };

  return (

    <div
      style={{
        display: "flex",
        height: "100vh",
        overflow: "hidden",
      }}
    >

      <Sidebar />

      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
          height: "100vh",
        }}
      >

        {/* HEADER */}

        <div
          style={{
            padding: "20px",
            borderBottom:
              "1px solid #ddd",
            background: "white",
          }}
        >
          <h1>
            AI Support Chat
          </h1>
        </div>

        {/* CHAT AREA */}

        <div
          style={{
            flex: 1,
            overflowY: "auto",
            padding: "20px",
            background:
              "#f8fafc",
          }}
        >

          {messages.length === 0 && (

            <p
              style={{
                color: "#666",
              }}
            >
              Start a conversation...
            </p>

          )}

          {messages.map(
            (
              msg,
              index
            ) => (

              <div
                key={index}
                style={{
                  display: "flex",

                  justifyContent:
                    msg.sender ===
                    "user"
                      ? "flex-end"
                      : "flex-start",

                  marginBottom:
                    "20px",
                }}
              >

                <div
                  style={{
                    maxWidth:
                      "70%",

                    padding:
                      "15px",

                    borderRadius:
                      "12px",

                    background:
                      msg.sender ===
                      "user"
                        ? "#2563eb"
                        : "white",

                    color:
                      msg.sender ===
                      "user"
                        ? "white"
                        : "black",

                    boxShadow:
                      "0 2px 8px rgba(0,0,0,0.1)",

                    textAlign:
                      "left",
                  }}
                >

                  <p
                    style={{
                      whiteSpace:
                        "pre-wrap",
                    }}
                  >
                    {msg.text}
                  </p>

                  {msg.sender ===
                    "bot" &&
                    (msg.complaint_id ||
                      msg.ticket_id) && (

                      <>
                        <hr
                          style={{
                            margin:
                              "10px 0",
                          }}
                        />

                        <p>
                          Complaint ID:
                          {" "}
                          {
                            msg.complaint_id
                          }
                        </p>

                        <p>
                          Ticket ID:
                          {" "}
                          {
                            msg.ticket_id
                          }
                        </p>

                        <p>
                          Category:
                          {" "}
                          {
                            msg.category
                          }
                        </p>

                        <p>
                          Priority:
                          {" "}
                          {
                            msg.priority
                          }
                        </p>
                      </>

                    )}

                </div>

              </div>

            )
          )}

          {loading && (

            <div
              style={{
                display: "flex",
                justifyContent:
                  "flex-start",
                marginBottom:
                  "20px",
              }}
            >

              <div
                style={{
                  background:
                    "white",

                  padding:
                    "15px",

                  borderRadius:
                    "12px",

                  boxShadow:
                    "0 2px 8px rgba(0,0,0,0.1)",
                }}
              >
                AI is typing...
              </div>

            </div>

          )}

          <div
            ref={
              messagesEndRef
            }
          />

        </div>

        {/* INPUT AREA */}

        <div
          style={{
            borderTop:
              "1px solid #ddd",

            padding:
              "15px",

            background:
              "white",
          }}
        >

          <textarea
            rows="3"
            value={message}
            onChange={(e) =>
              setMessage(
                e.target.value
              )
            }
            placeholder="Type your complaint..."
            style={{
              width: "100%",
              padding:
                "12px",
              borderRadius:
                "8px",
              resize:
                "none",
              fontSize:
                "15px",
            }}
          />

          <button
            onClick={
              sendMessage
            }
            disabled={
              loading
            }
            style={{
              marginTop:
                "10px",

              background:
                "#2563eb",

              color:
                "white",

              border:
                "none",

              padding:
                "10px 20px",

              borderRadius:
                "8px",

              cursor:
                "pointer",
            }}
          >
            {
              loading
                ? "Sending..."
                : "Send"
            }
          </button>

        </div>

      </div>

    </div>

  );
}

export default ChatPage;