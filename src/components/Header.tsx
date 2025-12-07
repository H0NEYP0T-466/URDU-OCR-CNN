/**
 * Header Component
 * 
 * Application header.
 */

import { Link } from 'react-router-dom';
import './Header.css';

interface HeaderProps {
  title?: string;
}

const Header: React.FC<HeaderProps> = ({ title = 'Urdu OCR' }) => {
  return (
    <header className="header">
      <div className="header-container">
        <div className="header-content">
          {/* Logo and Title */}
          <Link to="/" className="header-logo">
            <div className="header-logo-icon">
              <span className="urdu-text">ا</span>
            </div>
            <div>
              <h1 className="header-title">{title}</h1>
              <p className="header-subtitle">Handwritten Character Recognition</p>
            </div>
          </Link>
        </div>
      </div>
    </header>
  );
};

export default Header;
