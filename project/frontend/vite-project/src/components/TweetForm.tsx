import React, { useState } from 'react';
import { postTweet } from './tweetPage/getTweet';

const TweetForm: React.FC = () => {
  const [content, setContent] = useState('');
  const email = localStorage.getItem('email');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      console.log(content);
      await postTweet(email, content);
      setContent('');
      window.location.reload();
    } catch (error) {
      console.error('Error posting tweet:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea value={content} onChange={e => setContent(e.target.value)} />
      <button type="submit">Tweet</button>
    </form>
  );
};

export default TweetForm;

