import axios from "axios";
import EnvManager from "../config/envConstants";

interface NewsEntry {
  number: number;
  title: string;
  points: number;
  comments: number;
}
const backend = axios.create({
    baseURL: EnvManager.BACKEND_URL,
    withCredentials: true,
  });

  export const getEntries = async (): Promise<NewsEntry[]> => {
    try {
      const response = await backend.get(`/entries`);
      return response.data as NewsEntry[];
    } catch (error) {
      console.error(error);
      return [];
    }
  };
  
  export const filterByComments = async (): Promise<NewsEntry[]> => {
    try {
      const response = await backend.get(`/entries/comments`);
      return response.data as NewsEntry[];
    } catch (error) {
      console.error(error);
      return [];
    }
  };
  
  export const filterByPoints = async (): Promise<NewsEntry[]> => {
    try {
      const response = await backend.get(`/entries/points`);
      return response.data as NewsEntry[];
    } catch (error) {
      console.error(error);
      return [];
    }
  };
