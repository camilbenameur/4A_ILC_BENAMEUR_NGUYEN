import { API_URL } from '../config';
import useSWR from 'swr';

export type GetTweetsOptions = {
  topic?: string;
  user?: string;
};

export const getTweets = async (
  options: GetTweetsOptions
) => {

  let query = '';
  if (options.topic) {
    query = `?topic=${options.topic}`;
  } else if (options.user) {
    query = `?user=${options.user}`;
  }

  const response = await fetch(`${API_URL}/tweets${query}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return response.json();
};

export const useTweets = (options: GetTweetsOptions) => {
  return useSWR(options, getTweets);
}
