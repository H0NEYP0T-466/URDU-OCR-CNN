/**
 * Header Component
 * 
 * Application header with navigation.
 */

import { Link, useLocation } from 'react-router-dom';
import './Header.css';

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
    <header className="header">
      <div className="header-container">
        <div className="header-content">
          {/* Logo and Title */}
          <Link to="/" className="header-logo-link">
            <div className="header-logo-icon">
              <span className="urdu-text">ا</span>
            </div>
            <div>
              <h1 className="header-title">{title}</h1>
              <p className="header-subtitle">Handwritten Character Recognition</p>
            </div>
          </Link>

          {/* Navigation */}
          <nav className="header-nav">
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`header-nav-link ${
                  location.pathname === link.path ? 'active' : ''
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
