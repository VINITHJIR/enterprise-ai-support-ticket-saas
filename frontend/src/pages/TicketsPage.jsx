import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";

import {
    getTickets
} from "../services/ticketService";


function TicketsPage() {

    const [tickets, setTickets] =
        useState([]);

    useEffect(() => {

        loadTickets();

    }, []);

    const loadTickets = async () => {

        try {

            const data =
                await getTickets();

            setTickets(data);

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

                <h2>
                    Tickets
                </h2>

                <table
                    border="1"
                    cellPadding="10"
                    width="100%"
                >

                    <thead>

                        <tr>

                            <th>ID</th>

                            <th>
                                Complaint ID
                            </th>

                            <th>
                                Priority
                            </th>

                            <th>
                                Status
                            </th>

                            <th>
                                Assigned Agent
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {tickets.map(
                            (ticket) => (

                                <tr
                                    key={ticket.id}
                                >

                                    <td>
                                        {ticket.id}
                                    </td>

                                    <td>
                                        {
                                            ticket.complaint_id
                                        }
                                    </td>

                                    <td>
                                        {
                                            ticket.priority
                                        }
                                    </td>

                                    <td>
                                        {
                                            ticket.status
                                        }
                                    </td>

                                    <td>
                                        {
                                            ticket.assigned_agent
                                                || "-"
                                        }
                                    </td>

                                </tr>

                            )
                        )}

                    </tbody>

                </table>

            </div>

        </div>

    );
}

export default TicketsPage;