import { useState } from "react";
import Sidebar from "../components/Sidebar";
import api from "../services/api";

function ChatPage() {

    const [message, setMessage] =
        useState("");

    const [response, setResponse] =
        useState("");

    const sendMessage = async () => {

        try {

            const result =
                await api.post(
                    "/api/chat/",
                    {
                        message
                    }
                );

            setResponse(
                result.data
            );

        } catch (error) {

            console.error(error);

            alert("Chat failed");

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

                <h2>
                    AI Support Chat
                </h2>

                <textarea
                    rows="5"
                    style={{
                        width: "100%"
                    }}
                    value={message}
                    onChange={(e) =>
                        setMessage(
                            e.target.value
                        )
                    }
                />

                <br />
                <br />

                <button
                    onClick={
                        sendMessage
                    }
                >
                    Send
                </button>

                <br />
                <br />

                {response && (

                    <div
                        style={{
                            background:
                                "#f4f4f4",
                            padding: "20px",
                            borderRadius:
                                "8px"
                        }}
                    >

                        <h3>
                            Response
                        </h3>

                        <p>
                            {
                                response.response
                            }
                        </p>

                        <hr />

                        <p>
                            Complaint ID:
                            {
                                response.complaint_id
                            }
                        </p>

                        <p>
                            Ticket ID:
                            {
                                response.ticket_id
                            }
                        </p>

                        <p>
                            Category:
                            {
                                response.category
                            }
                        </p>

                        <p>
                            Priority:
                            {
                                response.priority
                            }
                        </p>

                    </div>

                )}

            </div>

        </div>
    );
}

export default ChatPage;