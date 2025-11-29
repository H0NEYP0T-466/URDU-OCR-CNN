/**
 * Header Component
 * 
 * Application header with navigation.
 */

import { Link, useLocation } from 'react-router-dom';

interface HeaderProps {
  title?: string;
}

const Header: React.FC<HeaderProps> = ({ title = 'Urdu OCR' }) => {
  const location = useLocation();
  
  const navLinks = [
    { path: '/', label: 'Home' },
    { path: '/about', label: 'About' },
    { path: '/how-it-works', label: 'How It Works' },
  ];

  return (
    <header className="bg-gradient-to-r from-blue-600 to-blue-800 text-white shadow-lg">
      <div className="container mx-auto px-4 py-4">
        <div className="flex flex-col md:flex-row items-center justify-between">
          {/* Logo and Title */}
          <Link to="/" className="flex items-center space-x-3 mb-4 md:mb-0">
            <div className="w-10 h-10 bg-white rounded-lg flex items-center justify-center">
              <span className="urdu-text text-2xl text-blue-600 font-bold">ا</span>
            </div>
            <div>
              <h1 className="text-xl font-bold">{title}</h1>
              <p className="text-xs text-blue-200">Handwritten Character Recognition</p>
            </div>
          </Link>

          {/* Navigation */}
          <nav className="flex space-x-1 md:space-x-4">
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`px-4 py-2 rounded-lg transition-all duration-200 ${
                  location.pathname === link.path
                    ? 'bg-white text-blue-600 font-medium'
                    : 'text-white hover:bg-blue-700'
                }`}
              >
                {link.label}
              </Link>
            ))}
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;
