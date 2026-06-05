import api from "./api";

export const getEmails = async () => {

    const response =
        await api.get(
            "/api/emails/"
        );

    return response.data;
};