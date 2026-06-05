import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";

import {
    getEmails
} from "../services/emailService";

function EmailsPage() {

    const [emails, setEmails] =
        useState([]);

    useEffect(() => {

        loadEmails();

    }, []);

    const loadEmails = async () => {

        const data =
            await getEmails();

        setEmails(data);
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
                    Escalation Emails
                </h2>

                <table
                    border="1"
                    width="100%"
                    cellPadding="10"
                >

                    <thead>

                        <tr>

                            <th>ID</th>

                            <th>
                                Ticket ID
                            </th>

                            <th>
                                Email Content
                            </th>

                            <th>
                                Sent At
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {emails.map(
                            (email) => (

                                <tr
                                    key={email.id}
                                >

                                    <td>
                                        {email.id}
                                    </td>

                                    <td>
                                        {
                                            email.ticket_id
                                        }
                                    </td>

                                    <td>
                                        {
                                            email.email_content
                                        }
                                    </td>

                                    <td>
                                        {
                                            email.sent_at
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

export default EmailsPage;