import api from "./api";

export const getTickets = async () => {

    const response =
        await api.get(
            "/api/tickets/"
        );

    return response.data;
};