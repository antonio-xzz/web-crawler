import React, { useState } from "react";
import {
  getEntries,
  filterByComments,
  filterByPoints,
} from "../services/newsServices";
import "../styles/NewsList.css";

interface NewsEntry {
  number: number;
  title: string;
  points: number;
  comments: number;
}

const NewsList: React.FC = () => {
  const [entries, setEntries] = useState<NewsEntry[]>([] as NewsEntry[]);
  const [loading, setLoading] = useState<boolean>(false);
  const [currentFilter, setCurrentFilter] = useState<string>("");

  const fetchEntries = async () => {
    setLoading(true);
    setCurrentFilter("entries");
    try {
      const data = await getEntries();
      if (Array.isArray(data)) {
        setEntries(data as NewsEntry[]);
      } else {
        setEntries([] as NewsEntry[]);
      }
    } catch (error) {
      console.error("Error fetching entries:", error);
      setEntries([] as NewsEntry[]);
    }
    setLoading(false);
  };
  
  const handleFilterByComments = async () => {
    setLoading(true);
    setCurrentFilter("comments");
    try {
      const data = await filterByComments();
      if (Array.isArray(data)) {
        setEntries(data as NewsEntry[]);
      } else {
        setEntries([] as NewsEntry[]);
      }
    } catch (error) {
      console.error("Error filtering by comments:", error);
      setEntries([] as NewsEntry[]);
    }
    setLoading(false);
  };
  
  const handleFilterByPoints = async () => {
    setLoading(true);
    setCurrentFilter("points");
    try {
      const data = await filterByPoints();
      if (Array.isArray(data)) {
        setEntries(data as NewsEntry[]);
      } else {
        setEntries([] as NewsEntry[]);
      }
    } catch (error) {
      console.error("Error filtering by points:", error);
      setEntries([] as NewsEntry[]);
    }
    setLoading(false);
  };

  return (
    <div className="news-list">
      <div className="button-box">
        <button onClick={fetchEntries}>Get Entries</button>
        {currentFilter === "entries" && !loading && (
          <div className="response-box">
            {entries.map((entry) => (
              <div key={entry.number} className="entry-box">
                <h3>{entry.title}</h3>
                <p>Points: {entry.points}</p>
                <p>Comments: {entry.comments}</p>
              </div>
            ))}
          </div>
        )}
      </div>
      <div className="button-box">
        <button onClick={handleFilterByComments}>Filter by Comments</button>
        {currentFilter === "comments" && !loading && (
          <div className="response-box">
            {entries.map((entry) => (
              <div key={entry.number} className="entry-box">
                <h3>{entry.title}</h3>
                <p>Points: {entry.points}</p>
                <p>Comments: {entry.comments}</p>
              </div>
            ))}
          </div>
        )}
      </div>
      <div className="button-box">
        <button onClick={handleFilterByPoints}>Filter by Points</button>
        {currentFilter === "points" && !loading && (
          <div className="response-box">
            {entries.map((entry) => (
              <div key={entry.number} className="entry-box">
                <h3>{entry.title}</h3>
                <p>Points: {entry.points}</p>
                <p>Comments: {entry.comments}</p>
              </div>
            ))}
          </div>
        )}
      </div>
      {loading && (
        <div className="spinner-container">
          <div className="spinner"></div>
        </div>
      )}
    </div>
  );
};

export default NewsList;
