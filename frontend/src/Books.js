// Home.js

import { useEffect, useState } from "react";
import './Books.css';

export default function Home() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8080/books')
      .then(response => response.json())
      .then(data => setBooks(data))
      .catch(error => console.error('Error fetching books:', error));
  }, []);

  return (
    <div className="container">
      <h2>Books from API</h2>
      
      {books.length === 0 ? (
        <p className="no-books-message">No books available</p>
      ) : (
        <ul className="book-list">
          {books.map((book) => (
            <li key={book.id} className="book-item">
              <p className="book-title">Title: {book.title}</p>
              <p>Author: {book.author}</p>
              <p>Quantity: {book.quantity}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
