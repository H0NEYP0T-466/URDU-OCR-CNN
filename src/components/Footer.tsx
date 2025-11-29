/**
 * Footer Component
 * 
 * Application footer with links and copyright.
 */

import './Footer.css';

interface FooterProps {
  year?: number;
}

const Footer: React.FC<FooterProps> = ({ year = new Date().getFullYear() }) => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-grid">
          {/* About */}
          <div className="footer-section">
            <h3>Urdu OCR</h3>
            <p>
              A deep learning-powered application for recognizing handwritten Urdu characters
              using Convolutional Neural Networks.
            </p>
          </div>

          {/* Quick Links */}
          <div className="footer-section">
            <h3>Quick Links</h3>
            <ul className="footer-links">
              <li>
                <a href="https://github.com" target="_blank" rel="noopener noreferrer">
                  GitHub Repository
                </a>
              </li>
              <li>
                <a href="/docs">
                  API Documentation
                </a>
              </li>
              <li>
                <a href="/about">
                  About the Project
                </a>
              </li>
            </ul>
          </div>

          {/* Technology */}
          <div className="footer-section">
            <h3>Technology</h3>
            <div className="footer-tech-badges">
              {['React', 'FastAPI', 'TensorFlow', 'TypeScript'].map((tech) => (
                <span
                  key={tech}
                  className="footer-tech-badge"
                >
                  {tech}
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* Copyright */}
        <div className="footer-copyright">
          <p>© {year} Urdu OCR. Built with ❤️ for the Urdu language.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
