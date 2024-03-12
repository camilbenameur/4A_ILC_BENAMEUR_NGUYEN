import React, { useState } from 'react';
import {postTweet} from './getTweet'

const TweetForm: React.FC = () => {
  const [content, setContent] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await postTweet(content);
      setContent('');
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
