import { NavLink, Outlet } from "react-router-dom";


export const Layout = () => {

  const menu = [
    {
      name: "Home",
      path: "/",
    },
    {
      name: "Profile",
      path: "/me",
    },
  ];

  


  return (
    <div className="h-screen flex flex-col">
      <header className="px-6 border-b border-gray-700 font-bold h-20 min-h-20 flex items-center fixed w-full bg-gray-900 z-10">
        The Social Network
      </header>
      <div className="flex-col">
        <nav className="p-8 border-r border-gray-700 w-64 fixed top-20 flex-grow h-screen">
          <ul>
            {menu.map((item, index) => (
              <NavLink
                to={item.path}
                key={index}
                className={({ isActive }) =>
                  "block p-2 " +
                  (isActive ? "font-bold text-white" : "text-gray-100")
                }
              >
                {item.name}
              </NavLink>
            ))}
          </ul>
        </nav>
        <main className="ml-64 mt-20">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
