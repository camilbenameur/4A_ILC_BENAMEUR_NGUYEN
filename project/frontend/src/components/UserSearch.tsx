import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { SearchInput } from "./SearchInput";

export const UserSearch = () => {
  const userdId = useParams().userId;
  const [search, setSearch] = useState(userdId);
  const navigate = useNavigate();

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        navigate(`/user/${search}`);
      }}
    >
      <SearchInput value={search} onChange={setSearch} />
      <button type="submit" className="sr-only">
        Search
      </button>
    </form>
  );
};
