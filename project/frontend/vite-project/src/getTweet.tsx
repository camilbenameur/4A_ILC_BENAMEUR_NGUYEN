const API_URL = 'http://localhost:5000';

export const getTweets = async () => {
  const response = await fetch(`${API_URL}/tweets`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
};

export const postTweet = async (content: string) => {
  await fetch(`${API_URL}/tweet`, {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ content }),
  });
};

export const getTweetsUser = async (email: string) => {
  const response = await fetch(`${API_URL}/user_tweets/${email}`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
};

export const getTweetsTopic = async (topic: string) => {
  const response = await fetch(`${API_URL}/topic_tweets/${topic}`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
};

