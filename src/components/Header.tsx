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
  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

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

          {/* Navigation Links */}
          <nav className="header-nav">
            <button 
              onClick={() => scrollToSection('supported-characters')}
              className="header-nav-link"
            >
              Supported Characters
            </button>
            <button 
              onClick={() => scrollToSection('footer')}
              className="header-nav-link"
            >
              About
            </button>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;
