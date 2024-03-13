import { Link, useParams } from "react-router-dom";
import { Tweet } from "../components/Tweet";
import { SearchInput } from "../components/SearchInput";
import { useTweets } from "../hooks/useTweets";
import { Loader } from "../components/Loader";
import { UserSearch } from "../components/UserSearch";

export const User = () => {
  const userId = useParams().userId as string;
  const {
    data: tweets,
    isLoading,
    isValidating,
    error,
  } = useTweets({ user: userId });
  const isError = error !== null;
  if (isLoading && !error) {
    return (
      <div className="p-4">
        <Loader />
      </div>
    );
  }

  if (isError) {
    return (
      <>
        <div className="p-4">
          <UserSearch />
        </div>
        <div className="p-4 text-center text-gray-300 text-2xl">
          This user cannot be found.
        </div>
        <Link to="/" className="text-blue-500 justify-center flex">
          Go back to home
        </Link>
      </>
    );
  }

  return (
    <>
      <UserSearch />
      {isError && (
        <div className="p-4 text-center text-red-500">
          Error fetching tweets
        </div>
      )}

      {isLoading && !error && (
        <div className="p-4">
          <Loader />
        </div>
      )}

      {tweets && (
        <>
          <div className="p-4 flex gap-4 items-center border-gray-700">
            <div className="rounded-full w-12 h-12 bg-gradient-to-r from-red-400 to-blue-600"></div>
            <h1 className="text-xl font-semibold">@{userId}</h1>
          </div>
          <div>
            {!tweets?.length && (
              <div className="p-4 text-center text-gray-500">
                No tweets found
              </div>
            )}
            {tweets?.map((tweet: any) => {
              return <Tweet key={tweet.id} tweet={tweet} />;
            })}
          </div>
        </>
      )}
    </>
  );
};
