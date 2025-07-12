import { Outlet } from "@tanstack/react-router";
import BottomNav from "./BottomNav";

export default function Layout() {
    return (
        <div className="min-h-screen flex flex-col p-4 items-center">
            <main className="flex-grow">
                <Outlet />
            </main>

            <footer className="flex flex-row">
                <BottomNav />
            </footer>
        </div>
    )
}