import useSWR from "swr";
import { API_URL } from "../config";

export const getAllTopics = async () => {
    const response = await fetch(`${API_URL}/topics`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.json();
  };

export const useTopics = () => {
    return useSWR('topics', getAllTopics);
}