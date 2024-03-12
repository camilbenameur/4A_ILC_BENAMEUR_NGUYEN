const API_URL = 'http://localhost:5000';

export const getTweets = async () => {
  const response = await fetch(`${API_URL}/tweet/get_tweets`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
};

export const postTweet = async (email: string | null, content: string) => {
  try {
    const response = await fetch(`${API_URL}/tweet/post`, {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email,
        tweet: content,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error);
    }
  } catch (error) {
    throw error;
  }
};

export const getTweetsUser = async (email: string) => {
  const response = await fetch(`${API_URL}/tweet/get_user_tweets/${email}`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
};

export const getTweetsTopic = async (topic: string) => {
  const response = await fetch(`${API_URL}/tweet/get_topic_tweets/${topic}`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
};

export const getAllTopics = async () => {
  const response = await fetch(`${API_URL}/topic/get_topics`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
};