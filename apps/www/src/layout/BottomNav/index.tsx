import { Home, Search } from 'lucide-react';
import { Link } from '@tanstack/react-router';

export default function BottomNav() {
  return (
    <div className="btm-nav z-50 flex flex-row justify-center">
      <Link to="/" className="text-gray-500 hover:text-primary">
        <Home size={40} />
      </Link>
      <Link to="/search" className="text-gray-500 hover:text-primary">
        <Search size={40} />
      </Link>
    </div>
  );
}
