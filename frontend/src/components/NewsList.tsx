import React, { useEffect, useState } from "react";
import {
  getEntries,
  filterByComments,
  filterByPoints,
} from "../services/newsServices";
import "../styles/NewsList.css";
import Card from "./Card";
import Loader from "./Loader";

interface NewsEntry {
  number: number;
  title: string;
  points: number;
  comments: number;
}

const NewsList: React.FC = () => {
  const [entries, setEntries] = useState<NewsEntry[]>([] as NewsEntry[]);
  const [loading, setLoading] = useState<boolean>(false);
  const [currentFilter, setCurrentFilter] = useState<string>("default");

  const fetchEntries = async () => {
    setLoading(true);
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

  useEffect(() => {
    fetchEntries();
  }, []);

  useEffect(() => {
    if (currentFilter === "comments") {
      handleFilterByComments();
    } else if (currentFilter === "points") {
      handleFilterByPoints();
    } else {
      fetchEntries();
    }
  }, [currentFilter]);

  return (
    <main className="main">
      <div className="header-wrapper">
        <header className="header">
          <h1>Entries</h1>
          <select onChange={(e) => setCurrentFilter(e.target.value)}>
            <option value="default">All entries</option>
            <option value="points" onClick={handleFilterByPoints}>
              Filter by points
            </option>
            <option value="comments" onClick={handleFilterByComments}>
              Filter by comments
            </option>
          </select>
        </header>
      </div>
      {loading ? <Loader /> 
        : <div className="container">
          <div className="cards-wrapper">
            {!loading && entries.map((entry) => (
              <Card
                key={entry.number}
                title={entry.title}
                points={entry.points}
                comments={entry.comments}
              />
            ))}
          </div>
        </div>}
    </main>
  );
};

export default NewsList;
