export const SearchInput = ({ onChange, value, defaultValue }: { onChange?: (v: string) => void; value?: string, defaultValue?: string }) => {
    return <div className="w-full">
        <label htmlFor="search" className="sr-only">
            Search
        </label>
        <div className="relative">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                <svg
                    className="h-5 w-5 text-gray-400"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                >
                    <path
                        fillRule="evenodd"
                        d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z"
                        clipRule="evenodd"
                    />
                </svg>
            </div>
            <input
                value={value}
                onChange={(e) => onChange?.(e.target.value)}
                defaultValue={defaultValue}
                id="search"
                name="search"
                className="block w-full rounded-md border-0 bg-gray-700 py-1.5 pl-10 pr-3 text-gray-300 placeholder:text-gray-400 focus:bg-white focus:text-gray-900 focus:ring-0 focus:placeholder:text-gray-500 sm:text-sm sm:leading-6"
                placeholder="Search"
                type="search"
            />
        </div>
    </div>;
}