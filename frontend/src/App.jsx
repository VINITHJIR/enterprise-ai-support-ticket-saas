import {
    BrowserRouter,
    Routes,
    Route
}
from "react-router-dom";
import TicketsPage from "./pages/TicketsPage";
import Login from "./pages/LoginPage";
import Register from "./pages/RegisterPage";
import DashboardPage from "./pages/DashboardPage";
import ChatPage from "./pages/ChatPage";
import ComplaintsPage from "./pages/ComplaintsPage";
import EmailsPage from "./pages/EmailsPage";
function App() {

    return (

        <BrowserRouter>

            <Routes>
                <Route
                path="/emails"
                element={<EmailsPage />}
                    />
                <Route
                    path="/complaints"
                    element={<ComplaintsPage />}
                    />
                    <Route
                        path="/tickets"
                        element={<TicketsPage />}
                    />
                <Route
                path="/chat"
                element={<ChatPage />}
                />
                <Route
                path="/login"
                element={<Login />}
                />

                <Route
                path="/register"
                element={<Register />}
/>
                <Route
                    path="/dashboard"
                    element={
                        <DashboardPage />
                    }
                />

                <Route
                    path="/chat"
                    element={
                        <ChatPage />
                    }
                />

            </Routes>

        </BrowserRouter>
    );
}

export default App;