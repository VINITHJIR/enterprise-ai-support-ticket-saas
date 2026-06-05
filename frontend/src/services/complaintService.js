import api from "./api";

export const getComplaints = async () => {
  const response = await api.get("/api/complaints/");
  return response.data;
};